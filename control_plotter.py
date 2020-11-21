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

for plot in plotlist:
	
	cb = ROOT.TCanvas("cb","cb",564,232,600,600)
	cb.SetHighLightColor(2)
        cb.Range(0,0,1,1)
        cb.SetFillColor(0)
        cb.SetBorderMode(0)
        cb.SetBorderSize(2)
        cb.SetTickx(1)
        cb.SetTicky(1)
        cb.SetLeftMargin(0.18)
        cb.SetRightMargin(0.04)
        cb.SetTopMargin(0.05)
        cb.SetBottomMargin(0.13)
        cb.SetFrameFillStyle(0)
        cb.SetFrameBorderMode(0)
        cb.SetFrameFillStyle(0)
        cb.cd()
	
	latex = ROOT.TLatex()
        latex.SetNDC()
        latex.SetTextSize(0.05)
        latex.SetTextAlign(11)
        
        leg = ROOT.TLegend(0.65,0.5,0.93,0.925)
        leg.SetBorderSize(1)
        leg_sig = ROOT.TLegend(0.3,0.8,0.6,0.925)
        leg_sig.SetBorderSize(1)
        Pad1 = ROOT.TPad("Pad1", "Pad1", 0,0.31,1,1)
        Pad1.Draw()
        Pad1.cd()
        #Pad1.Range(-0.7248462,-1.30103,3.302077,3.159352)
        Pad1.SetFillColor(0)
        Pad1.SetBorderMode(0)
        Pad1.SetBorderSize(2)
        Pad1.SetLogy()
        Pad1.SetTickx(1)
        Pad1.SetTicky(1)
        Pad1.SetLeftMargin(0.18)
        Pad1.SetRightMargin(0.04)
        Pad1.SetTopMargin(0.055)
        Pad1.SetBottomMargin(0)
        Pad1.SetFrameFillStyle(0)
        Pad1.SetFrameBorderMode(0)
        Pad1.SetFrameFillStyle(0)
        Pad1.SetFrameBorderMode(0)
        Pad1.SetLogy()
        #Pad1.Draw()
        #Pad1.cd()
        #ROOT.gStyle.SetHistMinimumZero()
        ROOT.gStyle.SetErrorX(.5)
        h_Stack = ROOT.THStack('h_Stack','h_Stack')
	for bkg in bkg_list:
		color = bkg['color']
		htmp = "h_tmp"
		h = ROOT.TH1D(htmp, htmp, *plot['binning'])
		bkg["chain"][0].Draw(plot['var']+">>%s"%htmp, bkg['weight']+"*("+single_photon_TIGHT+")", 'goff')	 
		h.SetFillColor(color)
		h.SetLineColor(ROOT.kBlack)
		h.SetLineWidth(1)
		h.GetXaxis().SetNdivisions(505)
		h.GetYaxis().SetTitle(p['yaxis'])
		h_Stack.Add(h)
		del h	
	Signal_dict["chain"][0].Draw(plot["var"],single_photon_TIGHT)
	cb.Draw()
	cb.SaveAs(plots/pngs/n+'.png')
	cb.SaveAs(plots/pdfs/n+'.pdf')
	cb.SaveAs(plots/roots/n+'.root')
	#define btag cuts

	#define general(MET,vb) cuts
	#define preselection cuts
	#plot for loop yap

	#canvas al
	#chain.draw(var)
	#save canvas

