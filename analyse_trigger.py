import ROOT
import json
import os
import pickle
import operator
from helper import deltaR
from configure import *

from ROOT import TFile, TTree, gRandom
from array import array

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--year", dest="year", default="2016", action="store", help="can be 2016,2017,2018")
parser.add_option("--sname", dest="sname", default="SinglePhoton", action="store", help="can be QCD , GJets_Pt ... ")
parser.add_option("--stype", dest="stype", default="data", action="store", help="can be data or signal or bkg")
parser.add_option("--letter", dest="letter", default="B", action="store", help="if data can be B,C,D,E,F,G,H;if signal GJets_Pt_100To200")
parser.add_option("--filename", dest="filename", default="sample.root", action="store", help="should be the individual root file name")
parser.add_option("--ndiv", dest="ndiv", default="1", action="store", help="number of divitions for one root file")
parser.add_option("--divIndex", dest="divIndex", default="0", action="store", help="index of divitions for one root file")
parser.add_option("--trigname", dest="trigname", default="HLT_Photon36_R9Id90_HE10_IsoM_prescale1_2016_36p12.json", action="store", help="can be any json file from Json directory")
(options, args) = parser.parse_args()

data_letter = options.letter
f = options.filename
exec("year="+options.year)
exec("ndiv="+options.ndiv)
exec("divIndex="+options.divIndex)
stype = options.stype
sname = options.sname
trigname = options.trigname

#afs_dir = os.environ["afs_dir"]
#targetdir_mainpath = os.environ["cern_box"] 
#pfile = afs_dir+"/samples_orig.pkl"
afs_dir = "/afs/cern.ch/user/m/myalvac/GPlusbJets/"
targetdir_mainpath = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/"
pfile = afs_dir+"/samples_orig.pkl"
sample_dic = pickle.load(open(pfile,'rb'))
sdict = sample_dic[year][stype][sname][data_letter]
print("Trigname:",trigname)
split_name = trigname.split("_")[-1]
#print(split_name)
eff_lumi = split_name.split(".")[0]
print("eff_Lumi:",eff_lumi)
eff_lumi = eff_lumi.replace("p",".")
eff_lumi = float(eff_lumi)
print("eff_Lumi:",eff_lumi)
#orig_dir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied_HLT_Photon175_MetFilters/SinglePhoton/Run2016"+data_letter+"_02Apr2020-v1/"
cert_json = afs_dir+"json/prescale_jsons/"+trigname
if year == 2016:
   act_Lumi = 36.47
   trigger_list = ["HLT_Photon36_R9Id90_HE10_IsoM","HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM"]
   offline_pt_dict = {"HLT_Photon36_R9Id90_HE10_IsoM":(40,60),"HLT_Photon50_R9Id90_HE10_IsoM":(60,90),"HLT_Photon75_R9Id90_HE10_IsoM":(90,100),"HLT_Photon90_R9Id90_HE10_IsoM":(100,145),"HLT_Photon120_R9Id90_HE10_IsoM":(145,180),"HLT_Photon165_R9Id90_HE10_IsoM":(180,225)}

   #cert_json = afs_dir+"/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
   print("working on 2016")
elif year == 2017:
   act_Lumi = 41.54
   trigger_list = ["HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon200"]
   offline_pt_dict = {"HLT_Photon50_R9Id90_HE10_IsoM":(60,90),"HLT_Photon75_R9Id90_HE10_IsoM":(90,100),"HLT_Photon90_R9Id90_HE10_IsoM":(100,145),"HLT_Photon120_R9Id90_HE10_IsoM":(145,180),"HLT_Photon165_R9Id90_HE10_IsoM":(180,225),"HLT_Photon200":(225,2000)}
   #cert_json = afs_dir+"/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
   print("working on 2017")
elif year == 2018:
   act_Lumi = 59.96
   trigger_list = ["HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon200"]
   offline_pt_dict = {"HLT_Photon50_R9Id90_HE10_IsoM":(60,90),"HLT_Photon75_R9Id90_HE10_IsoM":(90,100),"HLT_Photon90_R9Id90_HE10_IsoM":(100,145),"HLT_Photon120_R9Id90_HE10_IsoM":(145,180),"HLT_Photon165_R9Id90_HE10_IsoM":(180,225),"HLT_Photon200":(225,2000)}
   #cert_json = afs_dir+"/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"   
   print("working on 2018")

probed_trigger = trigname.split("_prescale")[0]
trigger_list.remove(probed_trigger)
veto_trigger_cut = ""
for trigger in trigger_list:
   veto_trigger_cut += "&& !("+trigger+")"

targetdir_suffix = "Low_PT"
orig_dir = sdict["dir"]+"/"
targetdir = targetdir_mainpath+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict["dir"].split("/")[-2]+"/"
data = json.load(open(cert_json))
print("Working on data ",data_letter)

targetfilePath = targetdir+trigname.split("prescale")[0]+trigname.split("_")[-3]+"_"+f.split(".")[0]+"_"+str(divIndex)+".root"
origFilePath = orig_dir+f
print("Target path:" , targetfilePath)
ch = ROOT.TChain("Events")
ch.Add(origFilePath)
number_events = ch.GetEntries()
nEventsPerChunk = number_events/float(ndiv)
print(nEventsPerChunk)
ini_event = divIndex*int(nEventsPerChunk)
fin_event = min((divIndex+1)*int(nEventsPerChunk),number_events)
print(ini_event,fin_event)
#elist_cut = probed_trigger+veto_trigger_cut
#elist_cut = probed_trigger
#elist_cut = elist_cut+"&&goodPhoton_pt[0]>="+str(offline_pt_dict[probed_trigger][0])+"&&goodPhoton_pt[0]<"+str(offline_pt_dict[probed_trigger][1])  
#print("elis_cut:",elist_cut)
#ch.Draw(">>eList",elist_cut)
#ch.Draw(">>eList",("1"))
#elist = ROOT.gDirectory.Get("eList")
#number_events = elist.GetN()
print("Working on: " , probed_trigger)
print(" Creating new root-file ...")
newFile = ROOT.TFile(targetfilePath,"recreate")
print(" Creating new tree ...")
newchain = ch.CloneTree(0)
tree = newchain.GetTree()
xsec = array('f',[0])
weight  = array('f',[0])
puweight  = array('f',[0])
PhotonSF  = array('f',[0])
ngoodPhoton  = array('i',[0])
goodPhoton_pt = array( 'd', 10*[ 0. ] )
goodPhoton_eta = array( 'd', 10*[ 0. ] )
goodPhoton_phi = array( 'd', 10*[ 0. ] )
goodPhoton_minDR = array( 'd', 10*[ 0. ] )
goodPhoton_sieie = array( 'd', 10*[ 0. ] )
goodPhoton_r9 = array( 'd', 10*[ 0. ] )
goodPhoton_hoe = array( 'd', 10*[ 0. ] )
goodPhoton_pfRelIso03_all = array( 'd', 10*[ 0. ] )
goodPhoton_pfRelIso03_chg = array( 'd', 10*[ 0. ] )
tree.Branch("xsec",xsec,"xsec/F")
tree.Branch("weight",weight,"weight/F")
tree.Branch("puweight",puweight,"puweight/F")
tree.Branch("PhotonSF",PhotonSF,"PhotonSF/F")

tree.Branch("ngoodPhoton",ngoodPhoton,"ngoodPhoton/I")
tree.Branch("goodPhoton_pt", goodPhoton_pt, "goodPhoton_pt[ngoodPhoton]/D")
tree.Branch("goodPhoton_eta", goodPhoton_eta, "goodPhoton_eta[ngoodPhoton]/D")
tree.Branch("goodPhoton_phi", goodPhoton_phi, "goodPhoton_phi[ngoodPhoton]/D")
tree.Branch("goodPhoton_minDR", goodPhoton_minDR, "goodPhoton_minDR[ngoodPhoton]/D")
tree.Branch("goodPhoton_sieie", goodPhoton_sieie, "goodPhoton_sieie[ngoodPhoton]/D")
tree.Branch("goodPhoton_r9", goodPhoton_r9, "goodPhoton_r9[ngoodPhoton]/D")
tree.Branch("goodPhoton_hoe", goodPhoton_hoe, "goodPhoton_hoe[ngoodPhoton]/D")
tree.Branch("goodPhoton_pfRelIso03_all", goodPhoton_pfRelIso03_all, "goodPhoton_pfRelIso03_all[ngoodPhoton]/D")
tree.Branch("goodPhoton_pfRelIso03_chg", goodPhoton_pfRelIso03_chg, "goodPhoton_pfRelIso03_chg[ngoodPhoton]/D")
ngoodJet = array('i',[0])
goodJet_pt = array( 'd', 25*[ 0. ] )
goodJet_eta = array( 'd', 25*[ 0. ] )
goodJet_phi = array( 'd', 25*[ 0. ] )
goodJet_btagDeepFlavB = array( 'd', 25*[ 0. ] )
goodJet_btagDeepFlavC = array( 'd', 25*[ 0. ] )
tree.Branch("ngoodJet",ngoodJet,"ngoodJet/I")
tree.Branch("goodJet_pt", goodJet_pt, "goodJet_pt[ngoodJet]/D")
tree.Branch("goodJet_eta", goodJet_eta, "goodJet_eta[ngoodJet]/D")
tree.Branch("goodJet_phi", goodJet_phi, "goodJet_phi[ngoodJet]/D")
tree.Branch("goodJet_btagDeepFlavB", goodJet_btagDeepFlavB, "goodJet_btagDeepFlavB[ngoodJet]/D")
tree.Branch("goodJet_btagDeepFlavC", goodJet_btagDeepFlavC, "goodJet_btagDeepFlavC[ngoodJet]/D")

ngoodbJet = array('i',[0])
goodbJet_pt = array( 'd', 25*[ 0. ] )
goodbJet_eta = array( 'd', 25*[ 0. ] )
goodbJet_phi = array( 'd', 25*[ 0. ] )
goodbJet_btagDeepFlavB = array( 'd', 25*[ 0. ] )
goodbJet_btagDeepFlavC = array( 'd', 25*[ 0. ] )
tree.Branch("ngoodbJet",ngoodbJet,"ngoodbJet/I")
tree.Branch("goodbJet_pt", goodbJet_pt, "goodbJet_pt[ngoodbJet]/D")
tree.Branch("goodbJet_eta", goodbJet_eta, "goodbJet_eta[ngoodbJet]/D")
tree.Branch("goodbJet_phi", goodbJet_phi, "goodbJet_phi[ngoodbJet]/D")
tree.Branch("goodbJet_btagDeepFlavB", goodbJet_btagDeepFlavB, "goodbJet_btagDeepFlavB[ngoodbJet]/D")
tree.Branch("goodbJet_btagDeepFlavC", goodbJet_btagDeepFlavC, "goodbJet_btagDeepFlavC[ngoodbJet]/D")

weight_trig_HLT_Photon36  = array('f',[0])
weight_trig_HLT_Photon50  = array('f',[0])
weight_trig_HLT_Photon75  = array('f',[0])
weight_trig_HLT_Photon90  = array('f',[0])
weight_trig_HLT_Photon120 = array('f',[0])
weight_trig_HLT_Photon165 = array('f',[0])

tree.Branch("weight_trig_HLT_Photon36",weight_trig_HLT_Photon36 ,"weight_trig_HLT_Photon36/F")
tree.Branch("weight_trig_HLT_Photon50",weight_trig_HLT_Photon50 ,"weight_trig_HLT_Photon50/F")
tree.Branch("weight_trig_HLT_Photon75",weight_trig_HLT_Photon75 ,"weight_trig_HLT_Photon75/F")
tree.Branch("weight_trig_HLT_Photon90",weight_trig_HLT_Photon90 ,"weight_trig_HLT_Photon90/F")
tree.Branch("weight_trig_HLT_Photon120",weight_trig_HLT_Photon120,"weight_trig_HLT_Photon120/F")
tree.Branch("weight_trig_HLT_Photon165",weight_trig_HLT_Photon165,"weight_trig_HLT_Photon165/F")

print("number of events:",number_events)
weight_v=-999.
weight_xsec_v=1.0
xsec_v = 1.0
for jentry in range(ini_event,fin_event):
   ch.GetEntry(jentry)
   run = ch.GetLeaf('run').GetValue()
   event = ch.GetLeaf('event').GetValue()
   lumi = ch.GetLeaf('luminosityBlock').GetValue()
   nPhoton = ch.GetLeaf('nPhoton').GetValue()
   nJet = ch.GetLeaf('nJet').GetValue()
   PV_npvsGood = ch.GetLeaf('PV_npvsGood').GetValue()
   if not PV_npvsGood >= 1: continue
   if not options.stype=="data":Pileup_nTrueInt = ch.GetLeaf('Pileup_nTrueInt').GetValue()
   Flag_goodVertices = ch.GetLeaf('Flag_goodVertices').GetValue()
   Flag_1 = ch.GetLeaf('Flag_globalSuperTightHalo2016Filter').GetValue()
   Flag_2 = ch.GetLeaf('Flag_HBHENoiseFilter').GetValue()
   Flag_3 = ch.GetLeaf('Flag_HBHENoiseIsoFilter').GetValue()
   Flag_4 = ch.GetLeaf('Flag_EcalDeadCellTriggerPrimitiveFilter').GetValue()
   Flag_5 = ch.GetLeaf('Flag_BadPFMuonFilter').GetValue()
   Flag_6 = ch.GetLeaf('Flag_eeBadScFilter').GetValue()
   Flag_7 = 1.0
   if not year == 2016:
      Flag_7 = ch.GetLeaf('Flag_ecalBadCalibFilter').GetValue()
   if (jentry%50000 == 0) : print(jentry,run,lumi)
   if options.stype == "data":
	if not str(int(run)) in data.keys(): continue
	if str(int(run)) in data.keys():
		for lumiBlock in data[str(int(run))]:
			if eff_lumi <= 0.00: continue
              		elif (lumi >= lumiBlock[0] and lumi <= lumiBlock[1] ) : weight_v = float(trigname.split("_")[-3].split("prescale")[1])
	if not Flag_6 : continue
   exec("weight_trig_"+probed_trigger.split("_R9Id90")[0]+"[0]=weight_v")
   if not (Flag_goodVertices and Flag_1 and Flag_2 and Flag_3 and Flag_4 and Flag_5 and Flag_7): continue
   xsec[0] = xsec_v
   weight[0] = weight_xsec_v
   puweight[0] = 1.0
   if not options.stype=="data": puweight[0] = pu68p6.GetBinContent(pu68p6.FindBin(Pileup_nTrueInt))
   photons = []
   for ph in range(int(nPhoton)):
        if ch.GetLeaf('Photon_cutBased').GetValue(ph)>=3 and ch.GetLeaf('Photon_pt').GetValue(ph)>=40 and (abs(ch.GetLeaf('Photon_eta').GetValue(ph))<1.4) :
                #print("found good photon")
                photons.append({'index':ph,'phi':ch.GetLeaf('Photon_phi').GetValue(ph),'eta':ch.GetLeaf('Photon_eta').GetValue(ph),'pt':ch.GetLeaf('Photon_pt').GetValue(ph)})


   jets = []
   bjets = []
   for j in range(int(nJet)):
        if ch.GetLeaf('Jet_pt').GetValue(j)>40 and abs(ch.GetLeaf('Jet_eta').GetValue(j))<2.4 and ch.GetLeaf('Jet_jetId').GetValue(j)>=6 and ch.GetLeaf('Jet_puId').GetValue(j)>=7:
                jets.append({'index':j,'pt':ch.GetLeaf('Jet_pt').GetValue(j),'phi':ch.GetLeaf('Jet_phi').GetValue(j),'eta':ch.GetLeaf('Jet_eta').GetValue(j)})
                if ch.GetLeaf('Jet_btagDeepFlavB').GetValue(j)>=0.7221 :
                        bjets.append({'index':j})
   ngoodJet[0] = len(jets)
   ngoodbJet[0] = len(bjets)
   ngoodJet[0] = len(jets)
   ngoodbJet[0] = len(bjets)
   for i,jet in enumerate(jets):
        goodJet_pt[i] = ch.GetLeaf('Jet_pt').GetValue(jet["index"])
        goodJet_eta[i] = ch.GetLeaf('Jet_eta').GetValue(jet["index"])
        goodJet_phi[i] = ch.GetLeaf('Jet_phi').GetValue(jet["index"])
        goodJet_btagDeepFlavB[i] = ch.GetLeaf('Jet_btagDeepFlavB').GetValue(jet["index"])
        goodJet_btagDeepFlavC[i] = ch.GetLeaf('Jet_btagDeepFlavC').GetValue(jet["index"])
   for i,bjet in enumerate(bjets):
        goodbJet_pt[i] = ch.GetLeaf('Jet_pt').GetValue(bjet["index"])
        goodbJet_eta[i] = ch.GetLeaf('Jet_eta').GetValue(bjet["index"])
        goodbJet_phi[i] = ch.GetLeaf('Jet_phi').GetValue(bjet["index"])
        goodbJet_btagDeepFlavB[i] = ch.GetLeaf('Jet_btagDeepFlavB').GetValue(bjet["index"])
        goodbJet_btagDeepFlavC[i] = ch.GetLeaf('Jet_btagDeepFlavC').GetValue(bjet["index"])

   sel_photons = []
   for i,photon in enumerate(photons):
        dRs = []
        for jet in jets:
                dR_Pho_Jet = deltaR(photon["phi"],jet["phi"],photon["eta"],jet["eta"])
                dRs.append(dR_Pho_Jet)
        if len(dRs) and min(dRs) >= 0.5 :
                #print("found good photon isolated from jets")
                goodPhoton_pt[i] = ch.GetLeaf('Photon_pt').GetValue(photon["index"])
                goodPhoton_eta[i] = ch.GetLeaf('Photon_eta').GetValue(photon["index"])
                goodPhoton_phi[i] = ch.GetLeaf('Photon_phi').GetValue(photon["index"])
                goodPhoton_minDR[i] = min(dRs)
                goodPhoton_sieie[i] = ch.GetLeaf('Photon_sieie').GetValue(photon["index"])
                goodPhoton_r9[i] = ch.GetLeaf('Photon_r9').GetValue(photon["index"])
                goodPhoton_hoe[i] = ch.GetLeaf('Photon_hoe').GetValue(photon["index"])
                goodPhoton_pfRelIso03_all[i] = ch.GetLeaf('Photon_pfRelIso03_all').GetValue(photon["index"])
                goodPhoton_pfRelIso03_chg[i] = ch.GetLeaf('Photon_pfRelIso03_chg').GetValue(photon["index"])
                sel_photons.append(photon)
   ngoodPhoton[0] = len(sel_photons)
   #print("Before the photon cut")
   if len(sel_photons) < 1 : continue
   #print("After the photon cut")
   PhotonSF_ = 1.0
   if not options.stype == "data":
        PhotonSF_ = SF_MC.GetBinContent(SF_MC.FindBin(sel_photons[0]["eta"],sel_photons[0]["pt"]))
        if PhotonSF_ < 0.01 : PhotonSF_ = 1.0
   PhotonSF[0] = PhotonSF_ 
    
   tree.Fill()

newFile.cd()
tree.Write()
newFile.Write()
newFile.Close()
print("CIMBOM")
