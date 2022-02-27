import ROOT
import json
import os
import pickle
import operator
from helper import deltaR , matching , getbTagSF
from configure import *

from ROOT import TFile, TTree, gRandom
from array import array

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--year", dest="year", default="2016", action="store", help="can be 2016,2017,2018")
parser.add_option("--sname", dest="sname", default="SinglePhoton", action="store", help="can be QCD , GJets_Pt ... ")
parser.add_option("--stype", dest="stype", default="data", action="store", help="can be data or signal or bkg")
parser.add_option("--letter", dest="letter", default="B", action="store", help="if data can be B,C,D,E,F,G,H;if signal GJets_Pt_100To200")
parser.add_option("--ndiv", dest="ndiv", default="10", action="store", help="number of divitions for one root file")
parser.add_option("--divIndex", dest="divIndex", default="0", action="store", help="index of divitions for one root file")
parser.add_option("--filename", dest="filename", default="sample.root", action="store", help="should be the individual root file name")
(options, args) = parser.parse_args()

data_letter = options.letter
f = options.filename
exec("year="+options.year)
exec("ndiv="+options.ndiv)
exec("divIndex="+options.divIndex)
stype = options.stype
sname = options.sname

#afs_dir = os.environ["afs_dir"]
afs_dir = "/afs/cern.ch/work/e/ecasilar/GplusbJets_UL/"
targetdir_mainpath = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/"
#targetdir_mainpath = "/eos/user/m/myalvac/UL_data/"
pfile = afs_dir+"/samples_orig.pkl"
sample_dic = pickle.load(open(pfile,'rb'))
sdict = sample_dic[year][stype][sname][data_letter]

if options.stype == "data":
   if year == 2016:
      cert_json = afs_dir+"/json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"
      print("working on 2016")
   elif year == 2017:
      cert_json = afs_dir+"/json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt"
      print("working on 2017")
   elif year == 2018:
      cert_json = afs_dir+"/json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"   
      print("working on 2018")
   orig_dir = sdict["dir"]+"/"

   targetdir_suffix = "High_PT_Tight"
   #targetdir_suffix = "High_PT_LooseNotTight"
   targetdir = targetdir_mainpath+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict["dir"].split("/")[-2]+"/"


   data = json.load(open(cert_json))
   xsec_v = 1.0
   weight_v = 1.0
   print("Working on data ",data_letter)
else:
   print("Working on MC")
   print(sdict.keys()) 
   xsec_v = sdict["xsec"]*1000 #femtobarn
   weight_v = xsec_v*target_lumi*(1/float(sdict["nevents"]))
   orig_dir = sdict["dir"]
   #targetdir_suffix = "GenMatching"
   targetdir_suffix = "High_PT_Tight"
   targetdir = targetdir_mainpath+"/MC/"+sname+"/"+targetdir_suffix+"/"+sdict["dir"].split("/")[-2]+"/"
   if year == 2016:
	   if "HIPM" in sdict["das_path"]: photon_SF_file = ROOT.TFile(afs_dir+"/SF_files/egammaEffi.txt_EGM2D_Pho_Tight_UL16.root")
	   else : photon_SF_file = ROOT.TFile(afs_dir+"/SF_files/egammaEffi.txt_EGM2D_Pho_Tight_UL16_postVFP.root")
   elif year == 2017:
      photon_SF_file = ROOT.TFile(afs_dir+"/SF_files/egammaEffi.txt_EGM2D_Tight_UL17.root")
   elif year == 2018:
      photon_SF_file = ROOT.TFile(afs_dir+"/SF_files/egammaEffi.txt_EGM2D_Pho_Tight.root_UL18.root")
   #For Photon Scale Factor
   SF_MC = photon_SF_file.Get("EGamma_SF2D")

puweight_file = ROOT.TFile(afs_dir+"/PUfiles/puCorrection.root")
pu68p6 = puweight_file.Get("h_ratio")


#For btagging Scale Factor
btagging_dict = pickle.load(open(afs_dir+"/SF_files/btag_SF.pkl",'rb'))

targetfilePath = targetdir+f.split(".")[0]+"_"+str(divIndex)+".root"
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
#ch.Draw(">>eList", "(PV_npvsGood>=1)")
#elist = ROOT.gDirectory.Get("eList")
#number_events = elist.GetN()
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
goodJet_btagDeepFlavCvL = array( 'd', 25*[ 0. ] )
goodJet_btagSF  = array('d', 25*[0. ])
goodJet_hadronFlavour  = array('d', 25*[0. ])
tree.Branch("ngoodJet",ngoodJet,"ngoodJet/I")
tree.Branch("goodJet_pt", goodJet_pt, "goodJet_pt[ngoodJet]/D")
tree.Branch("goodJet_eta", goodJet_eta, "goodJet_eta[ngoodJet]/D")
tree.Branch("goodJet_phi", goodJet_phi, "goodJet_phi[ngoodJet]/D")
tree.Branch("goodJet_btagDeepFlavB", goodJet_btagDeepFlavB, "goodJet_btagDeepFlavB[ngoodJet]/D")
tree.Branch("goodJet_btagDeepFlavCvL", goodJet_btagDeepFlavCvL, "goodJet_btagDeepFlavCvL[ngoodJet]/D")
tree.Branch("goodJet_hadronFlavour", goodJet_hadronFlavour, "goodJet_hadronFlavour[ngoodJet]/D")
tree.Branch("goodJet_btagSF", goodJet_btagSF, "goodJet_btagSF[ngoodJet]/D")
ngoodbJet = array('i',[0])
goodbJet_pt = array( 'd', 25*[ 0. ] )
goodbJet_eta = array( 'd', 25*[ 0. ] )
goodbJet_phi = array( 'd', 25*[ 0. ] )
goodbJet_btagDeepFlavB = array( 'd', 25*[ 0. ] )
goodbJet_btagDeepFlavCvL = array( 'd', 25*[ 0. ] )
goodbJet_btagSF  = array('d', 25*[0. ])
goodbJet_hadronFlavour  = array('d', 25*[0. ])
tree.Branch("ngoodbJet",ngoodbJet,"ngoodbJet/I")
tree.Branch("goodbJet_pt", goodbJet_pt, "goodbJet_pt[ngoodbJet]/D")
tree.Branch("goodbJet_eta", goodbJet_eta, "goodbJet_eta[ngoodbJet]/D")
tree.Branch("goodbJet_phi", goodbJet_phi, "goodbJet_phi[ngoodbJet]/D")
tree.Branch("goodbJet_btagDeepFlavB", goodbJet_btagDeepFlavB, "goodbJet_btagDeepFlavB[ngoodbJet]/D")
tree.Branch("goodbJet_btagDeepFlavCvL", goodbJet_btagDeepFlavCvL, "goodbJet_btagDeepFlavCvL[ngoodbJet]/D")
tree.Branch("goodbJet_btagSF", goodbJet_btagSF, "goodbJet_btagSF[ngoodbJet]/D")
tree.Branch("goodbJet_hadronFlavour", goodbJet_hadronFlavour, "goodbJet_hadronFlavour[ngoodbJet]/D")
ngoodGenPhoton  = array('i',[0])
goodGenPhoton_pt = array( 'd', [ 0. ] )
goodGenPhoton_eta = array( 'd', [ 0. ] )
goodGenPhoton_phi = array( 'd', [ 0. ] )
goodGenPhoton_GenPartIndex = array( 'd', [ 0. ] )
goodGenPhoton_dr = array( 'd', [ 0. ] )
tree.Branch("ngoodGenPhoton",ngoodGenPhoton,"ngoodGenPhoton/I")
tree.Branch("goodGenPhoton_pt", goodGenPhoton_pt, "goodGenPhoton_pt/D")
tree.Branch("goodGenPhoton_eta", goodGenPhoton_eta, "goodGenPhoton_eta/D")
tree.Branch("goodGenPhoton_phi", goodGenPhoton_phi, "goodGenPhoton_phi/D")
tree.Branch("goodGenPhoton_dr", goodGenPhoton_dr, "goodGenPhoton_dr/D")
print(number_events)
for jentry in range(ini_event,fin_event):
   ch.GetEntry(jentry)
   #ch.GetEntry(elist.GetEntry(jentry))
   run = ch.GetLeaf('run').GetValue()
   lumi = ch.GetLeaf('luminosityBlock').GetValue()
   nPhoton = ch.GetLeaf('nPhoton').GetValue()
   nJet = ch.GetLeaf('nJet').GetValue()
   if not options.stype=="data": nGenPart=int(ch.GetLeaf('nGenPart').GetValue())
   PV_npvsGood = ch.GetLeaf('PV_npvsGood').GetValue()
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
   #print(jentry,run,lumi)
   if options.stype == "data":
   	if not str(int(run)) in data.keys(): continue
   	if str(int(run)) in data.keys():
        	for lumiBlock in data[str(int(run))]:
                	if not (lumi >= lumiBlock[0] and lumi <= lumiBlock[1] ) : continue
	if not Flag_6 : continue
   if not PV_npvsGood >= 1: continue
   if not (Flag_goodVertices and Flag_1 and Flag_2 and Flag_3 and Flag_4 and Flag_5 and Flag_7): continue
   #print("Event passed json and met filters")
   xsec[0] = xsec_v 
   weight[0] = weight_v 
   puweight[0] = 1.0
   if not options.stype=="data": puweight[0] = pu68p6.GetBinContent(pu68p6.FindBin(Pileup_nTrueInt))
   photons = []
   if "LooseNotTight" in targetdir_suffix:
   	for ph in range(int(nPhoton)):
		if ch.GetLeaf('Photon_cutBased').GetValue(ph)>=1 and ch.GetLeaf('Photon_cutBased').GetValue(ph)<3 and ch.GetLeaf('Photon_pt').GetValue(ph)>=40 and (abs(ch.GetLeaf('Photon_eta').GetValue(ph))<1.4) :
			photons.append({'index':ph,'phi':ch.GetLeaf('Photon_phi').GetValue(ph),'eta':ch.GetLeaf('Photon_eta').GetValue(ph),'pt':ch.GetLeaf('Photon_pt').GetValue(ph)})
   else:
	   for ph in range(int(nPhoton)):
		if ch.GetLeaf('Photon_cutBased').GetValue(ph)>=3 and ch.GetLeaf('Photon_pt').GetValue(ph)>=40 and (abs(ch.GetLeaf('Photon_eta').GetValue(ph))<1.4) :
			photons.append({'index':ph,'phi':ch.GetLeaf('Photon_phi').GetValue(ph),'eta':ch.GetLeaf('Photon_eta').GetValue(ph),'pt':ch.GetLeaf('Photon_pt').GetValue(ph)})
		
   jets = []
   bjets = []
   for j in range(int(nJet)):
	if ch.GetLeaf('Jet_pt').GetValue(j)>40 and abs(ch.GetLeaf('Jet_eta').GetValue(j))<2.4 and ch.GetLeaf('Jet_jetId').GetValue(j)>=6 and ch.GetLeaf('Jet_puId').GetValue(j)>=7:
		jets.append({'index':j,'pt':ch.GetLeaf('Jet_pt').GetValue(j),'phi':ch.GetLeaf('Jet_phi').GetValue(j),'eta':ch.GetLeaf('Jet_eta').GetValue(j)})
		if ch.GetLeaf('Jet_btagDeepFlavB').GetValue(j)>=0.6502 : 
			bjets.append({'index':j})
   ngoodJet[0] = len(jets)
   ngoodbJet[0] = len(bjets)
   for i,jet in enumerate(jets):
	goodJet_pt[i] = ch.GetLeaf('Jet_pt').GetValue(jet["index"])
	goodJet_eta[i] = ch.GetLeaf('Jet_eta').GetValue(jet["index"])
	goodJet_phi[i] = ch.GetLeaf('Jet_phi').GetValue(jet["index"])
	goodJet_btagDeepFlavB[i] = ch.GetLeaf('Jet_btagDeepFlavB').GetValue(jet["index"])
	goodJet_btagDeepFlavCvL[i] = ch.GetLeaf('Jet_btagDeepFlavCvL').GetValue(jet["index"])
	goodJet_hadronFlavour[i] = 0.0
	#For btag SF
	if not options.stype == "data": 
		goodJet_hadronFlavour[i] = ch.GetLeaf('Jet_hadronFlavour').GetValue(jet["index"])
		goodJet_flavor = ch.GetLeaf('Jet_hadronFlavour').GetValue(jet["index"])
		if goodJet_flavor==5 : btagSF = getbTagSF(bdict=btagging_dict,flavor=0,pt=goodJet_pt[i],eta=goodJet_eta[i] ,disc=goodJet_btagDeepFlavB[i])
		elif goodJet_flavor==4 : btagSF = getbTagSF(bdict=btagging_dict,flavor=1,pt=goodJet_pt[i],eta=goodJet_eta[i] ,disc=goodJet_btagDeepFlavB[i])
		else : btagSF = getbTagSF(bdict=btagging_dict,flavor=2,pt=goodJet_pt[i],eta=goodJet_eta[i] ,disc=goodJet_btagDeepFlavB[i]) 
		goodJet_btagSF[i] = btagSF

   for i,bjet in enumerate(bjets):
	goodbJet_pt[i] = ch.GetLeaf('Jet_pt').GetValue(bjet["index"])
	goodbJet_eta[i] = ch.GetLeaf('Jet_eta').GetValue(bjet["index"])
	goodbJet_phi[i] = ch.GetLeaf('Jet_phi').GetValue(bjet["index"])
	goodbJet_btagDeepFlavB[i] = ch.GetLeaf('Jet_btagDeepFlavB').GetValue(bjet["index"])
	goodbJet_btagDeepFlavCvL[i] = ch.GetLeaf('Jet_btagDeepFlavCvL').GetValue(bjet["index"])
	goodbJet_hadronFlavour[i] = 0.0
	#For btag SF
	if not options.stype == "data": 
		goodbJet_hadronFlavour[i] = ch.GetLeaf('Jet_hadronFlavour').GetValue(bjet["index"])
		goodJet_flavor = ch.GetLeaf('Jet_hadronFlavour').GetValue(bjet["index"])
		if goodJet_flavor==5 : btagSF = getbTagSF(bdict=btagging_dict,flavor=0,pt=goodJet_pt[i],eta=goodJet_eta[i] ,disc=goodJet_btagDeepFlavB[i])
		elif goodJet_flavor==4 : btagSF = getbTagSF(bdict=btagging_dict,flavor=1,pt=goodJet_pt[i],eta=goodJet_eta[i] ,disc=goodJet_btagDeepFlavB[i])
		else : btagSF = getbTagSF(bdict=btagging_dict,flavor=2,pt=goodJet_pt[i],eta=goodJet_eta[i] ,disc=goodJet_btagDeepFlavB[i]) 
		goodbJet_btagSF[i] = btagSF
		
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

   #Matching starts for Photons in MC
   if not options.stype == "data":
	GenPhotons=[]
	for igen in range(nGenPart):
		if ch.GetLeaf('GenPart_pdgId').GetValue(igen)==22:
			GenPhoton = {'orig_index':igen,'pt':ch.GetLeaf('GenPart_pt').GetValue(igen),'eta':ch.GetLeaf('GenPart_eta').GetValue(igen),'phi':ch.GetLeaf('GenPart_phi').GetValue(igen)}
			RecoPhoton = sel_photons[0]
			match = matching(RecoPhoton=RecoPhoton, GenPhoton=GenPhoton, pt_ratio=0.10, dr_cone=0.5)
			if match[1] : GenPhotons.append(match[0])
	
	ngoodGenPhoton[0] = 0
	goodGenPhoton_pt[0] = -999
	goodGenPhoton_eta[0] =  -999
	goodGenPhoton_phi[0] = -999
	goodGenPhoton_GenPartIndex[0] = -999
	goodGenPhoton_dr[0] = -999
	if len(GenPhotons) > 0 :
		dRm = sorted(GenPhotons, key=lambda x: x['dR'])
		matched_genPhoton = dRm[0]
		ngoodGenPhoton[0] = 1
		goodGenPhoton_pt[0] = matched_genPhoton["pt"]
		goodGenPhoton_eta[0] =  matched_genPhoton["eta"]
		goodGenPhoton_phi[0] = matched_genPhoton["phi"]
		goodGenPhoton_GenPartIndex[0] = matched_genPhoton["orig_index"]
		goodGenPhoton_dr[0] = matched_genPhoton["dR"]
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
print("CIMBOM")
