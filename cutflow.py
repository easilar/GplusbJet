import ROOT
import helper
from helper import *

target_lumi = 35.9
single_photon_cut = "Sum$(Photon_pdgId==22)==1"
photon_cut = "Photon_pt>40 && abs(Photon_eta)<1.4442 && Photon_hoe<0.08 && Photon_sieie<0.0103 &&Photon_pfRelIso03_all <15 && Photon_pfRelIso03_chg < 10"
complex_cut = "Photon_pt>40 && abs(Photon_eta)<1.4442 && Photon_hoe<0.08 && Photon_sieie<0.0103 && Photon_pfRelIso03_all <15 && Photon_pfRelIso03_chg < 10 && Sum$(Jet_pt>40 && abs(Jet_eta)<2.4 && Jet_jetId>=6 && Jet_puId>=7)>=1 && Jet_pt[0]>100 && Jet_pt>40&&Jet_btagDeepFlavB>=07221"
#cutlist = photon_cut.split("&&")
cutlist = complex_cut.split("&&")

#Retrieve an example chain
#ch = getChain()
signal_chain = getChain(year=2016,stype='signal',sname='G1Jet_LHEGPt_PreVFP',pfile='samples_ana.pkl',datatype='all',test=True)
#bkg_chain = getChain(year=2016,stype='bkg',sname='QCD_HT_UL2016_PreVFP',pfile='samples_ana.pkl',datatype='all',test=False)

#current_cut = single_photon_cut
current_cut = complex_cut
cut_yield = getYieldFromChain(signal_chain[0],current_cut,str(target_lumi/float(signal_chain[1])))
print(signal_chain[1])
print(str(target_lumi/float(signal_chain[1])))
print(current_cut)
print(cut_yield)
#cut_yield = getYieldFromChain(bkg_ch[0],current_cut,str(target_lumi/float(bkg_chain[1])))
#for i,cut in enumerate(cutlist):
#	#Her bir loopta bir sonraki cut'i ekliyor 
#	print(i, cut)
#	current_cut += "&&"+current_cut  
#	cut_yield = getYieldFromChain(signal_chain[0],current_cut,str(target_lumi/float(signal_chain[1])))
##	cut_yield = getYieldFromChain(bkg_chain[0],current_cut,str(target_lumi/float(bkg_ch[1])))
#	print(cut_yield)
