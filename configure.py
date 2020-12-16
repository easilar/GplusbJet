from array import array
from math import pi, sqrt, cos, sin, sinh, log

#Here we put plot configurations
target_lumi = 35.9  #fb^{-1}

#gamma Pt bins
gPtBins  = array('d', [float(x) for x in range(60,85,25)\
                                        +range(85,105,20)\
                                        +range(105,130,25)\
                                        +range(130,190,60)\
                                        +range(190,220,30)\
                                        +range(220,250,30)\
                                        +range(250,300,50)\
                                        +range(300,350,50)\
                                        +range(350,400,50)\
                                        +range(400,500,100)\
                                        +range(500,700,200)\
                                        +range(700,1000,300)\
                                        +range(1000,2000,1000)\
                                        ])

ngood_vtx_cut = "(PV_npvsGood>=1)"
single_photon_cut = "(nPhoton==1)"
photon_cut = "(Photon_pt>40 && abs(Photon_eta)<1.4442 && Photon_hoe<0.08 && Photon_sieie<0.0103 &&Photon_pfRelIso03_all <15 && Photon_pfRelIso03_chg < 10 && Photon_electronVeto)"
single_photon_tight_cut = single_photon_cut + "&&" +"Sum$"+photon_cut+"==1"

nJet_tight = "Sum$(Jet_pt>30 && abs(Jet_eta)<2.4 && Jet_jetId>=7 && Jet_puId>=7)"
ntightDeepBJets = "Sum$(Jet_pt>30 && abs(Jet_eta)<2.4 && Jet_jetId>=7 && Jet_puId>=7 && Jet_btagDeepFlavB>=0.7221)"
nJet_tight_cut = "("+nJet_tight+">=1)"
cut_0b = ntightDeepBJets+"==0"
cut_1b = ntightDeepBJets+"==1"
cut_2b = ntightDeepBJets+"==2"

muon_veto = "Sum$(Muon_pt>10&&abs(Muon_eta)<2.4&&Muon_looseId&&Muon_isPFcand&&(Muon_isGlobal||Muon_isTracker))==0"
electron_veto = "Sum$(Electron_pt>10&&abs(Electron_eta)<2.5&&Electron_cutBased_Sum16>=1)==0"

presel = "&&".join([ngood_vtx_cut,single_photon_tight_cut,nJet_tight_cut,muon_veto,electron_veto])
sel_0b = "&&".join([presel,cut_0b])
sel_1b = "&&".join([presel,cut_1b])
sel_2b = "&&".join([presel,cut_2b])

trigger = "(HLT_Photon30)"
prob_trigger_1 = "(HLT_Photon30||HLT_Photon36||HLT_Photon50||HLT_Photon75||HLT_Photon90||HLT_Photon120||HLT_Photon175)"
prob_trigger_2 = "(\
HLT_Photon30_R9Id90_HE10_IsoM\
||HLT_Photon36_R9Id90_HE10_IsoM\
||HLT_Photon50_R9Id90_HE10_IsoM\
||HLT_Photon75_R9Id90_HE10_IsoM\
||HLT_Photon90_R9Id90_HE10_IsoM\
||HLT_Photon120_R9Id90_HE10_IsoM\
||HLT_Photon165_R9Id90_HE10_IsoM\
)"
prob_trigger_3 = "(HLT_Photon165_HE10)"
#ref_trigger = "(HLT_PFJet40)"
ref_trigger = "(HLT_IsoMu24)"

