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

targetdir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/MC_filtered/"+mc_sample

targetfilePath = targetdir+f
origFilePath = orig_dir+f
print("Working on data ", mc_sample)

origFilePath = origFilePath
ch = ROOT.TChain("Events")
ch.Add(origFilePath)
nentries = ch.GetEntries()
print(" Creating new root-file ...")
newFile = ROOT.TFile(targetfilePath,"recreate")
print(" Creating new tree ...")
newchain = ch.CloneTree(0)
tree = newchain.GetTree()
print(nentries)
for jentry in range(500):
   ch.GetEntry(jentry)
   nPhoton = ch.GetLeaf('nPhoton').GetValue()
   nJet = ch.GetLeaf('nJet').GetValue()
   lJetpt = ch.GetLeaf('Jet_pt').GetValue(0)
   PV_npvsGood = ch.GetLeaf('PV_npvsGood').GetValue()
   Flag_goodVertices = ch.GetLeaf('Flag_goodVertices').GetValue()
   Flag_1 = ch.GetLeaf('Flag_globalSuperTightHalo2016Filter').GetValue()
   Flag_2 = ch.GetLeaf('Flag_HBHENoiseFilter').GetValue()
   Flag_3 = ch.GetLeaf('Flag_HBHENoiseIsoFilter').GetValue()
   Flag_4 = ch.GetLeaf('Flag_EcalDeadCellTriggerPrimitiveFilter').GetValue()
   Flag_5 = ch.GetLeaf('Flag_BadPFMuonFilter').GetValue()
   #Flag_6 = ch.GetLeaf('Flag_eeBadScFilter').GetValue()
   if (jentry%50000 == 0) : print(jentry)
   if not (PV_npvsGood>=1 and nPhoton==1 and nJet>=1 and lJetpt>30): continue
   if not (Flag_goodVertices and Flag_1 and Flag_2 and Flag_3 and Flag_4 and Flag_5): continue
   tree.Fill()
newFile.cd()
tree.Write()
newFile.Write()
#newFile.Map()
newFile.Close()
