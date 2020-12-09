import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain
import ROOT
import os
import operator

import configure
from configure import gPtBins , target_lumi

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--test", dest="test", default=False, action="store", help="can be true or false")
(options, args) = parser.parse_args()


test = options.test
plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Control_Plots/'
if test: 
	plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)

plot_sig_stack = True

plotlist = [
{"var":"Photon_pt[0]","binning":(100,0,2000),"x_axis":"p_{T}(#gamma)[GeV]","y_axis":"Events","bin":(len(gPtBins)-1,gPtBins),"histoname":"Leading Photon Pt[GeV]","title":"LPhotonPt","bin_set":(True , 25)},
{"var":"Photon_eta[0]","binning":(10,-2,2),"x_axis":"#eta(#gamma)","y_axis":"Events","bin":(),"histoname":"Leading Photon Eta","title":"LPhotonEta","bin_set":(False , 1)},
{"var":"Photon_r9","binning":(100,0,1.5),"x_axis":"R9(#gamma)","y_axis":"Events","bin":(),"histoname":"Photon R9","title":"PhotonR9","bin_set":(False , 1)},
{"var":"Photon_hoe","binning":(100,0,0.085),"x_axis":"HoverE(#gamma)","y_axis":"Events","bin":(),"histoname":"Photon HoverE","title":"Photonhoe","bin_set":(False , 1)},
{"var":"Photon_sieie","binning":(100,0,0.015),"x_axis":"#sigmai#etai#eta(#gamma)","y_axis":"Events","bin":(),"histoname":"Photon Sigmaietaieta","title":"Photonsieie","bin_set":(False , 1)},
{"var":"Jet_pt[0]","binning":(100,0,3000),"x_axis":"Jet_p_{T}[GeV]","y_axis":"Events","bin":(),"histoname":"Leading Jet Pt[GeV]","title":"Jet_Pt","bin_set":(False , 1)},
{"var":"Jet_eta[0]","binning":(10,-2.5,2.5),"x_axis":"Jet_#eta","y_axis":"Events","bin":(),"histoname":"Leading Jet #eta","title":"Jet_#eta","bin_set":(False , 1)},
{"var":"nJet","binning":(10,0,10),"x_axis":"Jet Multiplicity","y_axis":"Events","bin":(),"histoname":"Leading Jet Multiplicity","title":"Jet Multiplicity","bin_set":(False , 1)}

]

#bkg chain al 
#bkg listof dicts  olustur
bkg_list = [
{"sample":"TTJets", "weight":"(1)",  "tex":"TTJets", "color":ROOT.kGray},
{"sample":"QCD", "weight":"(1)",  "tex":"QCD", "color":ROOT.kCyan-6},
{"sample":"TGJets", "weight":"(1)", "tex":"TGJets", "color":ROOT.kRed+3},
{"sample":"TTGets", "weight":"(1)", "tex":"TTGJets", "color":ROOT.kBlue-7},
{"sample":"ST_tW_antitop", "weight":"(1)","tex":"ST_tW_antitop", "color":ROOT.kMagenta-4},
{"sample":"ST_tW_top", "weight":"(1)", "tex":"ST_tW_top", "color":ROOT.kSpring+7},
{"sample":"ST_s_channel", "weight":"(1)", "tex":"ST_s_channel", "color":ROOT.kViolet-6},
{"sample":"ST_t_channel_antitop", "weight":"(1)", "tex":"ST_t_channel_antitop", "color":ROOT.kPink},
{"sample":"ST_t_channel_top", "weight":"(1)","tex":"ST_t_channel_top", "color":ROOT.kGreen-1}
]

#signal chain al
signal_dict = {"sample":"GJets", "weight":"(1)", "chain":getChain(stype="signal",sname="GJets"), "tex":"GJets", "color":ROOT.kYellow}
signal_dict["weight"] = "("+str(signal_dict["chain"][2])+"*1000""*"+str(target_lumi/float(signal_dict["chain"][1]))+"*genWeight)"
#define photon cuts
print(signal_dict["sample"],signal_dict["chain"][1],signal_dict["chain"][2])
single_photon_cut = "Sum$(Photon_pdgId==22)==1"
photon_cut = "(Photon_pt>40 && abs(Photon_eta)<1.4442 && Photon_hoe<0.08 && Photon_sieie<0.0103 &&Photon_pfRelIso03_all <15 && Photon_pfRelIso03_chg < 10 && Photon_electronVeto)"
single_photon_tight_cut = single_photon_cut + "&&" +"Sum$"+photon_cut+"==1"
trigger = "(HLT_Photon30)"
nJet_loose = "Sum$(Jet_pt>30 && abs(Jet_eta)<2.4 && Jet_jetId>=1)"
nJet_tight = "Sum$(Jet_pt>30 && abs(Jet_eta)<2.4 && Jet_jetId>=7)"
nlooseDeepBJets = "Sum$(Jet_pt>30 && abs(Jet_eta)<2.4 && Jet_jetId>=1 && Jet_puId>=4 && Jet_btagDeepB>=0.3093)"
nlooseDeepBJets_cut = nlooseDeepBJets+">=1"
nJet_tight_cut = nJet_tight+">=1"
event_cut = "&&".join([single_photon_tight_cut,trigger, nJet_tight_cut, nlooseDeepBJets_cut])
plot_cut = event_cut
plotlist = [plotlist[0]]
bkg_list = [bkg_list[1]]
for bkg in bkg_list:
    bkg["chain"] = getChain(stype="bkg",sname=bkg["sample"])
    print(bkg["sample"],bkg["chain"][1],bkg["chain"][2])
    bkg["weight"] = "("+str(bkg["chain"][2])+"*1000""*"+str(target_lumi/float(bkg["chain"][1]))+"*genWeight)"
if plot_sig_stack : bkg_list.append(signal_dict)
print(bkg_list)
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
	print('BKG loop starting........')
	#for bkg in  reversed(bkg_list):
	for bkg in bkg_list:
		print(bkg['tex'])
		color = bkg['color']
		#htmp = "h_tmp"
		#h = ROOT.TH1D(htmp, htmp, *plot['binning'])
		#bkg["chain"][0].Draw(plot['var']+">>%s"%htmp, bkg['weight']+"*("+plot_cut+")", 'goff')    
		h = getPlotFromChain(bkg['chain'][0], plot['var'], plot['bin'], cutString = plot_cut, weight = bkg["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
		h.SetFillColor(color)
		h.SetLineColor(ROOT.kBlack)
		h.SetLineWidth(1)
		h.GetXaxis().SetNdivisions(505)
		h.GetYaxis().SetTitle(plot['y_axis'])
		h.SetTitle("")
		Set_axis_pad1(h)
		h_Stack.Add(h)
		leg.AddEntry(h, bkg['tex'],"f")
		print("Integral of"+bkg['tex']+":" , h.Integral()) 
		del h
	print('BKG loop finished.......')
	if plot["bin_set"][0]: stack_hist=ROOT.TH1F("stack_hist","stack_hist", plot['bin'][0],plot['bin'][1]) 
        else: stack_hist=ROOT.TH1F("stack_hist","stack_hist",plot['bin'][0],plot['bin'][1],plot['bin'][2])
	stack_hist.Merge(h_Stack.GetHists())
	max_bin = stack_hist.GetMaximum()*10000
	h_Stack.SetMaximum(max_bin) 
	h_Stack.SetMinimum(0.00001)
	h_Stack.SetTitle("")
	h_Stack.Draw("Histo")
	htmp = "h_tmp"
	#h_sig = ROOT.TH1D(htmp, htmp, *plot['binning'])
	#signal_dict["chain"][0].Draw(plot['var']+">>%s"%htmp, signal_dict['weight']+"*("+plot_cut+")", 'goff')
	if not plot_sig_stack :
		h_sig = getPlotFromChain(signal_dict["chain"][0], plot['var'], plot['bin'], cutString = plot_cut, weight = signal_dict["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
		h_sig.SetFillColor(signal_dict["color"])
		h_sig.SetLineColor(ROOT.kBlack)
		h_sig.SetLineWidth(1)
		h_sig.GetXaxis().SetNdivisions(505)
		h_sig.GetYaxis().SetTitle(plot['y_axis'])
		h_sig.SetTitle("")
		h_sig.Draw("Histo Same")
		leg_sig.AddEntry(h_sig, signal_dict['tex'],"l")
		leg_sig.SetFillColor(0)
		leg_sig.SetLineColor(0)
		leg_sig.Draw()
		print("Integral of Signal:" , h_sig.Integral()) 
	print("Integral of BKG:" , stack_hist.Integral())   
	leg.SetFillColor(0)
	leg.SetLineColor(0)
	leg.Draw()
	Draw_CMS_header(lumi_label=target_lumi)
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
	h_ratio.GetYaxis().SetTitle("Data/MC")
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
