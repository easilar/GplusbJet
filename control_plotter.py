import helper
from helper import getChain
import ROOT

plotlist = [
{"var":"Photon_pt[0]","binning":(100,0,800),"x_axis":"p_{T}(#Gamma)[GeV]","y_axis":"Events","plot_limits":(),"histoname":"Leading Photon Pt[GeV]","title":"LPhotonPt"}
#{"var":"","binning":(),"x_axis":"","y_axis":"","plot_limits":(),"histoname":"","title":""},
#{"var":"","binning":(),"x_axis":"","y_axis":"","plot_limits":(),"histoname":"","title":""},
#{"var":"","binning":(),"x_axis":"","y_axis":"","plot_limits":(),"histoname":"","title":""},
#{"var":"","binning":(),"x_axis":"","y_axis":"","plot_limits":(),"histoname":"","title":""},
#{"var":"","binning":(),"x_axis":"","y_axis":"","plot_limits":(),"histoname":"","title":""},
#{"var":"","binning":(),"x_axis":"","y_axis":"","plot_limits":(),"histoname":"","title":""}


]

#bkg chain al 
#bkg listof dicts  olustur
bkg_list = [
{"sample":"QCD", "weight":"(1)", "chain":getChain(stype="bkg",sname="QCD"), "tex":"QCD", "color":ROOT.kCyan-6},
{"sample":"TGJets", "weight":"(1)", "chain":getChain(stype="bkg",sname="TGJets"), "tex":"TGets", "color":ROOT.kRed+3},
{"sample":"TTGets", "weight":"(1)", "chain":getChain(stype="bkg",sname="TTGJets"), "tex":"TTGJets", "color":ROOT.kBlue-7}
]
#signal chain al
signal_dict = {"sample":"GJets", "weight":"(1)", "chain":getChain(stype="signal",sname="GJets"), "tex":"GJets", "color":ROOT.kYellow}
#define photon cuts

single_photon_cut = "Sum$(Photon_pdgId==22)==1"
photon_cut = "(Photon_pt[0]>40 && abs(Photon_eta)<1.4442 && Photon_hoe<0.08 && Photon_sieie<0.0103 &&Photon_pfRelIso03_all <15 && Photon_pfRelIso03_chg < 10 && Photon_electronVeto)"
single_photon_TIGHT = single_photon_cut + "&&" +photon_cut


signal_dict["chain"][0].Draw(plotlist[0]["var"],single_photon_TIGHT)


#define btag cuts
#define general(MET,vb) cuts
#define preselection cuts
#plot for loop yap
#canvas al
#chain.draw(var)
#save canvas

