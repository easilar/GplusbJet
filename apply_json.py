import ROOT
import json
import os
import operator

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--letter", dest="letter", default="B", action="store", help="can be B,C,D,E,F,G,H")
parser.add_option("--filename", dest="filename", default="sample.root", action="store", help="should be the individual root file name")
(options, args) = parser.parse_args()

data_letter = options.letter
f = options.filename

cert_json = "/afs/cern.ch/work/e/ecasilar/GplusbJets/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"

orig_dir = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/data/SinglePhoton/data/Run2016"+data_letter+"_02Apr2020-v1/"

targetdir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied/SinglePhoton/Run2016"+data_letter+"_02Apr2020-v1/"

targetfilePath = targetdir+f
origFilePath = orig_dir+f
print("Working on data ",data_letter)

data = json.load(open(cert_json))
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
for jentry in range(nentries):
   ch.GetEntry(jentry)
   run = ch.GetLeaf('run').GetValue()
   lumi = ch.GetLeaf('luminosityBlock').GetValue()
   nPhoton = ch.GetLeaf('nPhoton').GetValue()
   nJet = ch.GetLeaf('nJet').GetValue()
   lJetpT = ch.GetLeaf('Jet_pt').GetValue(0)
   PV_npvsGood = ch.GetLeaf('PV_npvsGood').GetValue()
   Flag_goodVertices = ch.GetLeaf('Flag_goodVertices').GetValue()
   Flag_1 = ch.GetLeaf('Flag_globalSuperTightHalo2016Filter').GetValue()
   Flag_2 = ch.GetLeaf('Flag_HBHENoiseFilter').GetValue()
   Flag_3 = ch.GetLeaf('Flag_HBHENoiseIsoFilter').GetValue()
   Flag_4 = ch.GetLeaf('Flag_EcalDeadCellTriggerPrimitiveFilter').GetValue()
   Flag_5 = ch.GetLeaf('Flag_BadPFMuonFilter').GetValue()
   Flag_6 = ch.GetLeaf('Flag_eeBadScFilter').GetValue()
   if (jentry%50000 == 0) : print(jentry,run,lumi)
   if not str(int(run)) in data.keys(): continue
   if not (PV_npvsGood>=1 and nPhoton==1 and nJet>=1 and lJetpT >=30): continue
   if not (Flag_goodVertices and Flag_1 and Flag_2 and Flag_3 and Flag_4 and Flag_5 and Flag_6): continue
   if str(int(run)) in data.keys():
        for lumiBlock in data[str(int(run))]:
                if (lumi >= lumiBlock[0] and lumi <= lumiBlock[1] ) : tree.Fill()
newFile.cd()
tree.Write()
newFile.Write()
#newFile.Map()
newFile.Close()
