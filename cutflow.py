import ROOT
import helper
from helper import *

target_lumi = 35.9
single_photon_cut = "Sum$(Photon_pdgId==22)==1"
photon_cut = "Photon_pt>40 && abs(Photon_eta)<1.4442 && Photon_hoe<0.08 && Photon_sieie<0.0103 &&Photon_pfRelIso03_all <15 && Photon_pfRelIso03_chg < 10"
cutlist = photon_cut.split("&&")

#Retrieve an example chain
ch = getChain()

current_cut = single_photon_cut
cut_yield = getYieldFromChain(ch[0],current_cut,str(target_lumi/float(ch[1])))
for i,cut in enumerate(cutlist):
	#Her bir loopta bir sonraki cut'i ekliyor 
	print(i, cut)
	current_cut += "&&"+current_cut  
	cut_yield = getYieldFromChain(ch[0],current_cut,str(target_lumi/float(ch[1])))
	print(cut_yield)
