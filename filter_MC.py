import ROOT
import json
import os
import operator

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--path", dest="path", default="data_path", action="store", help="should be original sample path")
parser.add_option("--filename", dest="filename", default="sample.root", action="store", help="should be the individual root file name")
(options, args) = parser.parse_args()

mc_sample = options.path
f = options.filename

orig_dir = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/MC/"+mc_sample

targetdir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/MC_filtered_loose/"+mc_sample

targetfilePath = targetdir+f
origFilePath = orig_dir+f
print("Working on data ", mc_sample)

origFilePath = origFilePath
ch = ROOT.TChain("Events")
ch.Add(origFilePath)
nentries = ch.GetEntries()
ch.Draw(">>eList", "(PV_npvsGood>=1&&nPhoton>=1)&&Sum$(Photon_pt>40 && abs(Photon_eta)<1.4442 && Photon_hoe<0.08 && Photon_sieie<0.0103 &&Photon_pfRelIso03_all <15 && Photon_pfRelIso03_chg < 10 && Photon_electronVeto)==1")
elist = ROOT.gDirectory.Get("eList")
number_events = elist.GetN()
print(" Creating new root-file ...")
newFile = ROOT.TFile(targetfilePath,"recreate")
print(" Creating new tree ...")
newchain = ch.CloneTree(0)
tree = newchain.GetTree()
#print(nentries)
for jentry in range(number_events):
   ch.GetEntry(elist.GetEntry(jentry))
   #ch.GetEntry(jentry)
   #nPhoton = ch.GetLeaf('nPhoton').GetValue()
   #nJet = ch.GetLeaf('nJet').GetValue()
   #lJetpt = ch.GetLeaf('Jet_pt').GetValue(0)
   PV_npvsGood = ch.GetLeaf('PV_npvsGood').GetValue()
   Flag_goodVertices = ch.GetLeaf('Flag_goodVertices').GetValue()
   Flag_1 = ch.GetLeaf('Flag_globalSuperTightHalo2016Filter').GetValue()
   Flag_2 = ch.GetLeaf('Flag_HBHENoiseFilter').GetValue()
   Flag_3 = ch.GetLeaf('Flag_HBHENoiseIsoFilter').GetValue()
   Flag_4 = ch.GetLeaf('Flag_EcalDeadCellTriggerPrimitiveFilter').GetValue()
   Flag_5 = ch.GetLeaf('Flag_BadPFMuonFilter').GetValue()
   #Flag_6 = ch.GetLeaf('Flag_eeBadScFilter').GetValue()
   if (jentry%50000 == 0) : print(jentry)
   #if not (PV_npvsGood>=1 and nPhoton>=1 and nJet>=1): continue
   if not (Flag_goodVertices and Flag_1 and Flag_2 and Flag_3 and Flag_4 and Flag_5): continue
   tree.Fill()
newFile.cd()
tree.Write()
newFile.Write()
#newFile.Map()
newFile.Close()
