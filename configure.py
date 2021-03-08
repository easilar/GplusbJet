from array import array
from math import pi, sqrt, cos, sin, sinh, log

#Here we put plot configurations
#target_lumi = 35.9  #fb^{-1}
target_lumi = 41.53  #fb^{-1}
#gamma Pt bins
gPtBins  = array('d', [float(x) for x in range(40,160,5)\
					+range(160,500,40)\
					+range(500,660,160)\
                                        #+range(1500,2500,1000)\
                                        #+range(60,100,10)\
                                       # +range(100,160,20)\
                                       # +range(160,260,40)\
                                        #+range(200,300,50)\
                                       # +range(250,300,50)\
                                        #+range(300,350,50)\
                                        #+range(300,400,100)\
                                        #+range(400,500,100)\
                                        #+range(500,700,200)\
                                        #+range(700,1000,300)\
                                        #+range(1000,2000,1000)\
                                        #+range(2000,3000,1000)\
                                        ])

ngood_vtx_cut = "(PV_npvsGood>=1)"
met_filters= "(Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)"
single_photon_cut = "(nPhoton>=1)"
photon_cut = "(Photon_pt>40 && abs(Photon_eta)<1.4442 && Photon_hoe<0.08 && Photon_sieie<0.0103 &&Photon_pfRelIso03_all <15 && Photon_pfRelIso03_chg < 10 && Photon_electronVeto)"
nPhoton = "Sum$"+photon_cut
single_photon_tight_cut = single_photon_cut+"&&"+"(Sum$"+photon_cut+"==1)"

nJet_tight = "Sum$(Jet_pt>30 && abs(Jet_eta)<2.4 && Jet_jetId>=7 && Jet_puId>=7)"
ntightDeepBJets = "Sum$(Jet_pt>30 && abs(Jet_eta)<2.4 && Jet_jetId>=7 && Jet_puId>=7 && Jet_btagDeepFlavB>=0.7221)"
nJet_tight_cut = "("+nJet_tight+">=1)"
cut_0b = ntightDeepBJets+"==0"
cut_1b = ntightDeepBJets+"==1"
cut_2b = ntightDeepBJets+"==2"

muon_veto = "Sum$(Muon_pt>10&&abs(Muon_eta)<2.4&&Muon_looseId&&Muon_isPFcand&&(Muon_isGlobal||Muon_isTracker))==0"
electron_veto = "Sum$(Electron_pt>10&&abs(Electron_eta)<2.5&&Electron_cutBased_Sum16>=1)==0"

presel = "&&".join([ngood_vtx_cut,met_filters,single_photon_tight_cut,muon_veto,electron_veto])
sel_0b = "&&".join([presel,cut_0b])
sel_1b = "&&".join([presel,cut_1b])
sel_2b = "&&".join([presel,cut_2b])

trigger = "(HLT_Photon30)"
#prob_triggers = ["HLT_Photon33","HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon200"]
prob_triggers = ["HLT_Photon33","HLT_Photon50","HLT_Photon75","HLT_Photon90","HLT_Photon120","HLT_Photon150","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon175","HLT_Photon200"]
#prob_triggers = ["HLT_Photon30","HLT_Photon36","HLT_Photon50","HLT_Photon75","HLT_Photon90","HLT_Photon120","HLT_Photon150","HLT_Photon165_HE10","HLT_Photon175"]
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
#ref_trigger = "(HLT_IsoMu27)"
ref_trigger = "(HLT_IsoMu24)"
#jet_photon_cut = "Photon_cutBased>=3&&Photon_pt>200&&abs(Photon_eta)<1.4&&Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=1&&Jet_pt[0]>100"
jet_photon_cut = "Sum$(Photon_cutBased>=3&&Photon_pt>200&&abs(Photon_eta)<1.4)==1" #&&Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=1&&Jet_pt[0]>100"
jet_cut = "(ngoodPhoton==1&&abs(goodPhoton_eta)<=1.4&&goodJet_pt[0]>100)"
jet_cut_trig = "(ngoodPhoton==1&&abs(goodPhoton_eta)<=1.4&&goodJet_pt[0]>100&&HLT_Photon175)"


#Plots
plotlist = {
"Photon_pt":{"var":"Photon_pt","binning":(100,0,3000),"x_axis":"p_{T}(#gamma)[GeV]","y_axis":"Events","bin":(len(gPtBins)-1,gPtBins),"histoname":"Photon Pt[GeV]","title":"PhotonPt","bin_set":(True , 25)},
"Photon_eta":{"var":"goodPhoton_eta","binning":(10,-2,2),"x_axis":"#eta(#gamma)","y_axis":"Events","bin":(),"histoname":"Photon Eta","title":"PhotonEta","bin_set":(False , 1)},
"Photon_phi":{"var":"goodPhoton_phi","binning":(20,-4,4),"x_axis":"#phi(#gamma)","y_axis":"Events","bin":(),"histoname":"Photon Phi","title":"PhotonPhi","bin_set":(False , 1)},
"Pileup_nTrueInt":{"var":"Pileup_nTrueInt","binning":(20,0,100),"x_axis":"N True Int.","y_axis":"Events","bin":(),"histoname":"Pileup_nTrueInt","title":"Pileup_nTrueInt","bin_set":(False , 1)},
"PV_npvsGood":{"var":"PV_npvsGood","binning":(100,0,100),"x_axis":"npvsGood","y_axis":"Events","bin":(),"histoname":"PV_npvsGood","title":"PV_npvsGood","bin_set":(False , 1)},
"LPhoton_pt":{"var":"goodPhoton_pt[0]","binning":(100,0,2000),"x_axis":"p_{T}(#gamma)[GeV]","y_axis":"Events","bin":(len(gPtBins)-1,gPtBins),"histoname":"Leading Photon Pt[GeV]","title":"LPhotonPt","bin_set":(True , 25)},
"LPhoton_eta":{"var":"goodPhoton_eta[0]","binning":(10,-2,2),"x_axis":"#eta(#gamma)","y_axis":"Events","bin":(),"histoname":"Leading Photon Eta","title":"LPhotonEta","bin_set":(False , 1)},
"Photon_pfRelIso03_all":{"var":"goodPhoton_pfRelIso03_all","binning":(40,0,0.06),"x_axis":"Rel Iso All #gamma","y_axis":"Events","bin":(),"histoname":"Photon_pfRelIso03_all","title":"Photon_pfRelIso03_all","bin_set":(False , 1)},
"Photon_pfRelIso03_chg":{"var":"goodPhoton_pfRelIso03_chg","binning":(40,0,0.006),"x_axis":"Rel Iso Chg #gamma","y_axis":"Events","bin":(),"histoname":"Photon_pfRelIso03_chg","title":"Photon_pfRelIso03_chg","bin_set":(False , 1)},
"Photon_r9":{"var":"goodPhoton_r9","binning":(20,0,2),"x_axis":"R9(#gamma)","y_axis":"Events","bin":(),"histoname":"Photon R9","title":"PhotonR9","bin_set":(False , 1)},
"Photon_hoe":{"var":"goodPhoton_hoe","binning":(20,0,0.1),"x_axis":"HoverE(#gamma)","y_axis":"Events","bin":(),"histoname":"Photon HoverE","title":"Photonhoe","bin_set":(False , 1)},
"Photon_sieie":{"var":"goodPhoton_sieie","binning":(20,0,0.02),"x_axis":"#sigmai#etai#eta(#gamma)","y_axis":"Events","bin":(),"histoname":"Photon Sigmaietaieta","title":"Photonsieie","bin_set":(False , 1)},
"LJet_pt":{"var":"goodJet_pt[0]","binning":(50,0,1000),"x_axis":"Jet_p_{T}[GeV]","y_axis":"Events","bin":(),"histoname":"Leading Jet Pt[GeV]","title":"Jet_Pt","bin_set":(False , 1)},
"LJet_eta":{"var":"goodJet_eta[0]","binning":(30,-3,3),"x_axis":"Jet_#eta","y_axis":"Events","bin":(),"histoname":"Leading Jet #eta","title":"Jet_eta","bin_set":(False , 1)},
"nJet":{"var":"ngoodJet","binning":(10,0,10),"x_axis":"Jet Multiplicity","y_axis":"Events","bin":(),"histoname":"Jet Multiplicity","title":"nJet","bin_set":(False , 1)},
"nBJet":{"var":"ngoodbJet","binning":(10,0,10),"x_axis":"b Jet Multiplicity","y_axis":"Events","bin":(),"histoname":"b Jet Multiplicity","title":"nbJet","bin_set":(False , 1)},
"ngoodPhoton":{"var":"ngoodPhoton","binning":(10,0,10),"x_axis":"n #gamma","y_axis":"Events","bin":(),"histoname":"Photon Multiplicity","title":"ngoodPhoton","bin_set":(False , 1)},
"MET_pt":{"var":"MET_pt","binning":(30,0,600),"x_axis":"#slash{E}_{T}","y_axis":"Events","bin":(),"histoname":"Missing Et","title":"MET","bin_set":(False , 1)}
        }

