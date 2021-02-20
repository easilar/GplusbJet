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
parser.add_option("--year", dest="year", default=2016, action="store", help="can be 2016,2017,2018")
parser.add_option("--sname", dest="sname", default="SinglePhoton", action="store", help="can be QCD , GJets_Pt ... ")
parser.add_option("--stype", dest="stype", default="data", action="store", help="can be data or signal or bkg")
parser.add_option("--letter", dest="letter", default="B", action="store", help="if data can be B,C,D,E,F,G,H;if signal GJets_Pt_100To200")
parser.add_option("--filename", dest="filename", default="sample.root", action="store", help="should be the individual root file name")
(options, args) = parser.parse_args()

data_letter = options.letter
f = options.filename
year = options.year
stype = options.stype
sname = options.sname

afs_dir = "/afs/cern.ch/work/e/ecasilar/GplusbJets/"
targetdir_mainpath = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/"

pfile = afs_dir+"/samples_orig.pkl"
#pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl"
sample_dic = pickle.load(open(pfile,'rb'))
sdict = sample_dic[year][stype][sname][data_letter]


#orig_dir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied_HLT_Photon175_MetFilters/SinglePhoton/Run2016"+data_letter+"_02Apr2020-v1/"
if options.stype == "data":
	cert_json = afs_dir+"/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
	orig_dir = sdict["dir"]+"/"
	targetdir = targetdir_mainpath+"/data/"+sname+"/"+sdict["dir"].split("/")[-1]+"/"
	data = json.load(open(cert_json))
	xsec_v = 1.0
	weight_v = 1.0
	print("Working on data ",data_letter)
else:
	print("Working on MC", data_letter)
	xsec_v = sdict["xsec"]*1000 #femtobarn
	weight_v = xsec_v*target_lumi*(1/float(sdict["nevents"]))
	orig_dir = sdict["dir"]
	targetdir = targetdir_mainpath+"/MC/"+sname+"/"+sdict["dir"].split("/")[-2]+"/"

#For PU
puweight_file = ROOT.TFile(afs_dir+"/PUfiles/puCorrection.root")
pu68p6 = puweight_file.Get("h_ratio")

#For Photon Scale Factor
photon_SF_file = ROOT.TFile(afs_dir+"/SF_files/Fall17V2_2016_Tight_photons.root")
SF_MC = photon_SF_file.Get("EGamma_SF2D")

targetfilePath = targetdir+f
origFilePath = orig_dir+f
print("Target path:" , targetfilePath)
ch = ROOT.TChain("Events")
ch.Add(origFilePath)
#number_events = ch.GetEntries()
ch.Draw(">>eList", "(PV_npvsGood>=1)")
elist = ROOT.gDirectory.Get("eList")
number_events = elist.GetN()
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
goodPhoton_pt = array( 'd', 3*[ 0. ] )
goodPhoton_eta = array( 'd', 3*[ 0. ] )
goodPhoton_phi = array( 'd', 3*[ 0. ] )
goodPhoton_minDR = array( 'd', 3*[ 0. ] )
goodPhoton_sieie = array( 'd', 3*[ 0. ] )
goodPhoton_r9 = array( 'd', 3*[ 0. ] )
goodPhoton_hoe = array( 'd', 3*[ 0. ] )
goodPhoton_pfRelIso03_all = array( 'd', 3*[ 0. ] )
goodPhoton_pfRelIso03_chg = array( 'd', 3*[ 0. ] )
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
print(number_events)
for jentry in range(number_events):
   #ch.GetEntry(elist.GetEntry(jentry))
   ch.GetEntry(jentry)
   run = ch.GetLeaf('run').GetValue()
   lumi = ch.GetLeaf('luminosityBlock').GetValue()
   nPhoton = ch.GetLeaf('nPhoton').GetValue()
   nJet = ch.GetLeaf('nJet').GetValue()
   #lJetpT = ch.GetLeaf('Jet_pt').GetValue(0)
   HLT_Photon175 = ch.GetLeaf('HLT_Photon175').GetValue()
   PV_npvsGood = ch.GetLeaf('PV_npvsGood').GetValue()
   Pileup_nTrueInt = ch.GetLeaf('Pileup_nTrueInt').GetValue()
   Flag_goodVertices = ch.GetLeaf('Flag_goodVertices').GetValue()
   Flag_1 = ch.GetLeaf('Flag_globalSuperTightHalo2016Filter').GetValue()
   Flag_2 = ch.GetLeaf('Flag_HBHENoiseFilter').GetValue()
   Flag_3 = ch.GetLeaf('Flag_HBHENoiseIsoFilter').GetValue()
   Flag_4 = ch.GetLeaf('Flag_EcalDeadCellTriggerPrimitiveFilter').GetValue()
   Flag_5 = ch.GetLeaf('Flag_BadPFMuonFilter').GetValue()
   Flag_6 = ch.GetLeaf('Flag_eeBadScFilter').GetValue()
   if (jentry%50000 == 0) : print(jentry,run,lumi)
   if options.stype == "data":
   	if not str(int(run)) in data.keys(): continue
   	if str(int(run)) in data.keys():
        	for lumiBlock in data[str(int(run))]:
                	if not (lumi >= lumiBlock[0] and lumi <= lumiBlock[1] ) : continue
   	#if not HLT_Photon175 : continue
	if not Flag_6 : continue
   if not (Flag_goodVertices and Flag_1 and Flag_2 and Flag_3 and Flag_4 and Flag_5): continue
   xsec[0] = xsec_v 
   weight[0] = weight_v 
   puweight[0] = pu68p6.GetBinContent(pu68p6.FindBin(Pileup_nTrueInt))
   photons = []
   for ph in range(int(nPhoton)):
	if ch.GetLeaf('Photon_cutBased').GetValue(ph)>=3 and ch.GetLeaf('Photon_pt').GetValue(ph)>=40 and (abs(ch.GetLeaf('Photon_eta').GetValue(ph))<1.4) :
		photons.append({'index':ph,'phi':ch.GetLeaf('Photon_phi').GetValue(ph),'eta':ch.GetLeaf('Photon_eta').GetValue(ph),'pt':ch.GetLeaf('Photon_pt').GetValue(ph)})
		
   jets = []
   bjets = []
   for j in range(int(nJet)):
	if ch.GetLeaf('Jet_pt').GetValue(j)>40 and abs(ch.GetLeaf('Jet_eta').GetValue(j))<2.4 and ch.GetLeaf('Jet_jetId').GetValue(j)>=7 and ch.GetLeaf('Jet_puId').GetValue(j)>=7:
		jets.append({'index':j,'pt':ch.GetLeaf('Jet_pt').GetValue(j),'phi':ch.GetLeaf('Jet_phi').GetValue(j),'eta':ch.GetLeaf('Jet_eta').GetValue(j)})
		if ch.GetLeaf('Jet_btagDeepFlavB').GetValue(j)>=0.7221 : 
			bjets.append({'index':j})
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
   if len(sel_photons) < 1 : continue
   PhotonSF_ = 1.0 
   if not options.stype == "data":
   	PhotonSF_ = SF_MC.GetBinContent(SF_MC.FindBin(sel_photons[0]["eta"],sel_photons[0]["pt"]))
   	if PhotonSF_ < 0.01 : PhotonSF_ = 1.0
   PhotonSF[0] = PhotonSF_
   tree.Fill()
newFile.cd()
tree.Write()
newFile.Write()
#newFile.Map()
newFile.Close()
