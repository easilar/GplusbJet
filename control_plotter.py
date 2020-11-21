import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header
import ROOT

plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Control_Plots/'
plotlist = [
{"var":"Photon_pt[0]","binning":(100,0,2000),"x_axis":"p_{T}(#gamma)[GeV]","y_axis":"Events","plot_limits":(),"histoname":"Leading Photon Pt[GeV]","title":"LPhotonPt"}
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
print('Plot loop starting......')
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
        
        #leg = ROOT.TLegend(0.65,0.5,0.93,0.925)
        #leg.SetBorderSize(1)
        #leg_sig = ROOT.TLegend(0.3,0.8,0.6,0.925)
        #leg_sig.SetBorderSize(1)
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
	print('BKG loop starting........')
	for bkg in bkg_list:
		print(bkg['tex'])
		color = bkg['color']
		htmp = "h_tmp"
		h = ROOT.TH1D(htmp, htmp, *plot['binning'])
		bkg["chain"][0].Draw(plot['var']+">>%s"%htmp, bkg['weight']+"*("+single_photon_TIGHT+")", 'goff')	 
		h.SetFillColor(color)
		h.SetLineColor(ROOT.kBlack)
		h.SetLineWidth(1)
		h.GetXaxis().SetNdivisions(505)
		h.GetYaxis().SetTitle(plot['y_axis'])
		h.SetTitle("")
		Set_axis_pad1(h)
		h_Stack.Add(h)
		#leg.AddEntry(h, bkg['tex'],"f")
		del h
	print('BKG loop finished.......')
	stack_hist=ROOT.TH1F("stack_hist","stack_hist",plot['binning'][0],plot['binning'][1],plot['binning'][2])
	stack_hist.Merge(h_Stack.GetHists())
	max_bin = stack_hist.GetMaximum()*10000
	h_Stack.SetMaximum(max_bin)	
	h_Stack.SetMinimum(0.00001)
	h_Stack.SetTitle("")
	h_Stack.Draw("Histo")
	htmp = "h_tmp"
        h = ROOT.TH1D(htmp, htmp, *plot['binning'])
	signal_dict["chain"][0].Draw(plot['var']+">>%s"%htmp, signal_dict['weight']+"*("+single_photon_TIGHT+")", 'goff')
       # h.SetFillColor(color)
        h.SetLineColor(color)
        h.SetLineWidth(3)
        h.GetXaxis().SetNdivisions(505)
        h.GetYaxis().SetTitle(plot['y_axis'])
	h.SetTitle("")
	h.Draw("Histo Same")
	h.Draw("Histo Same")
	#leg_sig.AddEntry(h, signal_dict['tex'],"l")
	print("Integral of BKG:" , stack_hist.Integral())	
	print("Integral of Signal:" , h.Integral())	
	del h
	#leg.SetFillColor(0)
        #leg.SetLineColor(0)
        #leg.Draw()
        #leg_sig.SetFillColor(0)
        #leg_sig.SetLineColor(0)
        #leg_sig.Draw()
	Draw_CMS_header()
	#Pad1.RedrawAxis()
	cb.cd()
	Pad2 = ROOT.TPad("Pad2", "Pad2",  0, 0, 1, 0.31)
        Pad2.Draw()
        Pad2.cd()
        #Pad2.Range(-0.7248462,-0.8571429,3.302077,2)
        Pad2.SetFillColor(0)
        Pad2.SetFillStyle(4000)
        Pad2.SetBorderMode(0)
        Pad2.SetBorderSize(2)
        Pad2.SetTickx(1)
        Pad2.SetTicky(1)
        Pad2.SetLeftMargin(0.18)
        Pad2.SetRightMargin(0.04)
        Pad2.SetTopMargin(0)
        Pad2.SetBottomMargin(0.3)
        Pad2.SetFrameFillStyle(0)
        Pad2.SetFrameBorderMode(0)
        Pad2.SetFrameFillStyle(0)
        Pad2.SetFrameBorderMode(0)
	Func = ROOT.TF1('Func',"[0]",plot['binning'][1],plot['binning'][2])
        Func.SetParameter(0,1)
        Func.SetLineColor(58)
        Func.SetLineWidth(2)
	h_ratio = stack_hist.Clone('h_ratio')
        h_ratio.Sumw2()
        h_ratio.SetStats(0)
        h_ratio.Divide(stack_hist)
	h_ratio.SetMaximum(2)
        h_ratio.SetMinimum(0.01)
	h_ratio.SetMarkerStyle(20)
        h_ratio.SetMarkerSize(1.1)
        h_ratio.SetMarkerColor(ROOT.kBlack)
        h_ratio.SetTitle("")
	Set_axis_pad2(h_ratio)
        h_ratio.GetYaxis().SetTitle("Data/Pred. ")
        h_ratio.GetXaxis().SetTitle(plot['x_axis'])
        h_ratio.GetYaxis().SetNdivisions(505)
	h_ratio.Draw("E1")
        Func.Draw("same")
        h_ratio.Draw("E1 Same")
	cb.cd()
	cb.Draw()
	cb.SaveAs(plots_path+plot['title']+'.png')
	cb.SaveAs(plots_path+plot['title']+'.pdf')
	cb.SaveAs(plots_path+plot['title']+'.root')
	cb.Clear()
	del h_Stack
	#define btag cuts

	#define general(MET,vb) cuts
	#define preselection cuts
	#plot for loop yap

	#canvas al
	#chain.draw(var)
	#save canvas

