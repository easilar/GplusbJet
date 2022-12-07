import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist, Draw_era_tag, obtain_bin_sys
import ROOT
import os
import operator

import configure
from configure import *

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--test", dest="test", default=False, action="store", help="can be true or false")
parser.add_option("--plot", dest="plot", default="Photon_pt", action="store", help="can be Photon_eta , LPhoton_pt ... ")
parser.add_option("--region", dest="region", default="single_photon", action="store", help="can be 0b, 1b, 2b, presel ")
parser.add_option("--s_samp", dest="s_samp", default="G1Jet_Pt", action="store", help="can be G1Jet_Pt , GJets_Pt ")
parser.add_option("--divIndex", dest="divIndex", default="0", action="store", help="index of divitions for one root file")
parser.add_option("--ndiv", dest="ndiv", default="10", action="store", help="number of divitions for one root file")
parser.add_option("--blind", dest="blind", default=False, action="store", help="Blinding data for signal region")
(options, args) = parser.parse_args()
exec("ndiv="+options.ndiv)
exec("divIndex="+options.divIndex)
plot_index = options.plot
blind=options.blind
#ROOT.setTDRStyle()
ROOT.gStyle.SetOptStat(0)


plot = plotlist[plot_index]
if not plot["bin_set"][0]: plot["bin"] = plot["binning"]

region = options.region

signal_samp = options.s_samp

pfile = "/afs/cern.ch/user/m/myalvac/GPlusbJets_UL/samples_ana.pkl"

year = 2018
era_tag = "UL 2018"
target_lumi_dict = {"UL 2016 PreVFP":19.52,"UL 2016 PostVFP":16.81,"UL 2017":41.48,"UL 2018":59.83}
lumi_weight = float(target_lumi_dict[era_tag])/100 

test = options.test
plots_path ='/eos/user/m/myalvac/www/MC_GEN_study/'
#plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/UL/'+era_tag.replace(' ','_')+'/Control_Plots/G1Jet/CR_Plots/'
#plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/UL/'+era_tag.replace(' ','_')+'/Control_Plots/GJets/CR_Plots/'
print(plots_path)
if not os.path.exists(plots_path):
  os.makedirs(plots_path)

plot_sig_stack = True

#bkg chain al 
#bkg listof dicts  olustur
bkg_list = [
{"sample":"TGJets_UL_2018", "weight":"(1)","bjet_cut":"(1)", "tex":"TGJets", "color":ROOT.kViolet-3},
{"sample":"TTGJets_UL_2018", "weight":"(1)","bjet_cut":"(1)", "tex":"TTGJets", "color":ROOT.kGreen-3},
{"sample":"WZG_UL_2018", "weight":"(1)","bjet_cut":"(1)", "tex":"WZG", "color":ROOT.kYellow-3},
{"sample":"ZGToLLG_UL_2018", "weight":"(1)","bjet_cut":"(1)", "tex":"ZGToLLg", "color":ROOT.kOrange-3},
#{"sample":"WJetsToLNu_HT", "weight":"(1)","bjet_cut":"(ngoodGenPhoton==0)", "tex":"WJets", "color":ROOT.kCyan-3},
{"sample":"WJetsToLNu_HT", "weight":"(1)","bjet_cut":"(1)", "tex":"WJets", "color":ROOT.kCyan-3},
#{"sample":"DYJetsToLL_M_50_HT", "weight":"(1)","bjet_cut":"(ngoodGenPhoton==0)", "tex":"DYJets", "color":ROOT.kOrange+3},
{"sample":"DYJetsToLL_M_50_HT", "weight":"(1)","bjet_cut":"(1)", "tex":"DYJets", "color":ROOT.kOrange+3},
{"sample":"QCD_HT_UL2018", "weight":"(1)","bjet_cut":"(ngoodGenPhoton==0)&&(ngoodbJet==0)", "tex":"QCD", "color":ROOT.kBlue-3},
#{"sample":"QCD_HT_UL2018", "weight":"(1)","bjet_cut":"(ngoodGenPhoton==0)", "tex":"QCD", "color":ROOT.kBlue-3}
{"sample":"QCD_bEnriched_HT_UL2018", "weight":"(1)","bjet_cut":"(ngoodGenPhoton==0)&&(ngoodbJet==1||ngoodbJet==2)", "tex":"QCD_bEnriched", "color":ROOT.kBlue-3}
]


#signal chain al
'''
if signal_samp == "G1Jet_Pt":
	signal_dict = {"sample":"G1Jet_LHEGpt", "weight":"(1)", "chain_all":getChain(year=year,stype="signal",sname="G1Jet_LHEGpt",pfile=pfile,test=test), "tex":"G+1Jet", "color":ROOT.kAzure+6}
	signal_dict["weight"] = str(lumi_weight)+"*(weight*puweight*PhotonSF)"


print(signal_dict["sample"],signal_dict["chain_all"][1],signal_dict["chain_all"][2])
'''
if signal_samp == "GJets_DR_0p4_HT":
	signal_dict = {"sample":"GJets_DR_0p4_HT", "weight":"(1)", "chain_all":getChain(year=year,stype="signal",sname="GJets_DR_0p4_HT",pfile=pfile,test=test), "tex":"GJets_DR_0p4_HT", "color":ROOT.kAzure+6}
	signal_dict["weight"] = str(lumi_weight)+"*(weight*puweight*PhotonSF)"


print(signal_dict["sample"],signal_dict["chain_all"][1],signal_dict["chain_all"][2])

#data dict al
#data_dict = {"sample":"SinglePhoton_UL", "weight":"(1)", "chain":getChain(year=year,stype="data",sname="SinglePhoton_UL",pfile=pfile,test=test)[0], "tex":"SinglePhoton", "color":ROOT.kBlack}
data_dict = {"sample":"EGamma_UL", "weight":"(1)", "chain":getChain(year=year,stype="data",sname="EGamma_UL",pfile=pfile,test=test)[0], "tex":"Egamma", "color":ROOT.kBlack, "blind_cut":"(goodPhoton_hoe>0.04)"}
if year == 2016:
	HLT_Trigger = "HLT_Photon175"
else: 
	HLT_Trigger = "HLT_Photon200"
#define photon cuts
selections={
"jetphoton": jet_photon_cut,\
"jet_cut":jet_cut,\
"no_cut":"(1)",\
"vtx_cut":ngood_vtx_cut,\
"met_filters": "&&".join([ngood_vtx_cut,met_filters]),\
"single_photon":"ngoodPhoton==1&&(goodPhoton_pt>=225)",\
"presel":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225"+"&&"+HLT_Trigger,\
"1b":"ngoodbJet==1&&ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225"+"&&"+HLT_Trigger,\
"2b":"ngoodbJet==2&&ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225"+"&&"+HLT_Trigger,\
"0b":"ngoodbJet==0&&ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225"+"&&"+HLT_Trigger,\
"1b_inc":"ngoodbJet>=1&&ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225"+"&&"+HLT_Trigger,\
"2b_inc":"ngoodbJet>=2&&ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225"+"&&"+HLT_Trigger,\
"0b_inc":"ngoodbJet>=0&&ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225"+"&&"+HLT_Trigger,\
}

hightweightcut="!(event==50233261||event==171503688||event==331789209)"
plot_cut = selections[region]

bkg_Int = 0
for bkg in bkg_list:
    bkg["chain_all"] = getChain(year=year,stype="bkg",sname=bkg["sample"],pfile=pfile,test=test)
    print(bkg["sample"],bkg["chain_all"][1],bkg["chain_all"][2])
    bkg["chain"] = bkg["chain_all"][0]
    bkg["weight"] = str(lumi_weight)+"*(weight*puweight*PhotonSF)"
    print(bkg["weight"])
    h = getPlotFromChain(bkg['chain'], plot['var'], plot['bin'], cutString = plot_cut+"&&"+bkg["bjet_cut"]+"&&("+hightweightcut+")", weight = bkg["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
    bkg["histo"] = h
    bkg_Int+=bkg["histo"].Integral()
    del h
    print(bkg["chain"].GetEntries())
print(bkg_Int)
signal_dict["chain"] = signal_dict["chain_all"][0]
print(signal_dict["chain"].GetEntries())
data_dict["chain"] = data_dict["chain"]
if plot_sig_stack : bkg_list.append(signal_dict)
print('Ploting starts......')
if not blind: data_dict["blind_cut"]="(1)"
data_dict["histo"] = getPlotFromChain(data_dict["chain"], plot['var'], plot['bin'], cutString = "&&".join(["(1)",plot_cut,data_dict["blind_cut"]]), weight = data_dict["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
print("data is taken")

signal_dict["histo"] = getPlotFromChain(signal_dict["chain"], plot['var'], plot['bin'], cutString = plot_cut, weight = signal_dict["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])

SF=1
signalPlusbkg = bkg_Int+signal_dict["histo"].Integral()
if not blind: SF = data_dict["histo"].Integral()/signalPlusbkg
print("MC Scale Factor: ", SF)
print(plot["title"])
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

leg = ROOT.TLegend(0.6,0.65,0.93,0.925)
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
	h = bkg["histo"]
	h.Scale(SF)
	h.SetFillColor(color)
	h.SetLineColor(ROOT.kBlack)
	h.SetLineWidth(1)
	h.GetXaxis().SetNdivisions(505)
	h.GetYaxis().SetTitle(plot['y_axis'])
	h.SetTitle("")
	Set_axis_pad1(h)
	leg.AddEntry(h, bkg['tex']+" "+str(round(h.Integral())),"f")
	#leg.AddEntry(h, "SF "+str(SF),"f")
	print("Integral of"+bkg['tex']+":" , h.Integral())
	h_Stack.Add(bkg["histo"])
	del h
print('BKG loop finished.......')
h_Stack.Draw("histo")
if plot["bin_set"][0]: stack_hist=ROOT.TH1F("stack_hist","stack_hist", plot['bin'][0],plot['bin'][1]) 
else: stack_hist=ROOT.TH1F("stack_hist","stack_hist",plot['bin'][0],plot['bin'][1],plot['bin'][2])
stack_hist.Merge(h_Stack.GetHists())
print("#ofbins:",stack_hist.GetNbinsX())
for i in range(1, stack_hist.GetNbinsX()+1):
#for i in range(1, 10):
	print("binnumber:",i)
    	bincontent=stack_hist.GetBinContent(i)
	binerror=obtain_bin_sys(bincontent,i)
	#binerror=(bincontent*0.5)
        if bincontent!=0:
 		print("binnumber:",i,"bincontent:",bincontent,"binerror:",binerror)
	stack_hist.SetBinError(i,binerror)
stack_hist.SetFillColor(14)
stack_hist.SetFillStyle(3001)
stack_hist.Draw("Same E2")
#h_Stack=stack_hist.Clone()
max_bin = stack_hist.GetMaximum()*10000
h_Stack.SetMaximum(max_bin) 
h_Stack.SetMinimum(0.00001)
h_Stack.SetTitle("")
#start data
color = ROOT.kBlack
h_data = data_dict["histo"]
h_data.SetMarkerStyle(20)
h_data.SetMarkerSize(1.1)
h_data.SetLineColor(color)
h_data.GetXaxis().SetTitle(plot['x_axis'])
h_data.GetYaxis().SetTitle(plot['y_axis'])
h_data.SetTitle("")
#h_data.GetYaxis().SetTitleSize(0.05)
#h_data.GetYaxis().SetLabelSize(0.05)
Set_axis_pad1(h_data)
h_data.Draw(" Same E1")
h_data.SetMaximum(max_bin)
h_data.SetMinimum(0.11)
#h_Stack.Draw("HistoSame")
htmp = "h_tmp"
#h_sig = ROOT.TH1D(htmp, htmp, *plot['binning'])
#signal_dict["chain"][0].Draw(plot['var']+">>%s"%htmp, signal_dict['weight']+"*("+plot_cut+")", 'goff')
if not plot_sig_stack :
	h_sig = getPlotFromChain(signal_dict["chain"], plot['var'], plot['bin'], cutString = plot_cut, weight = signal_dict["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
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
h_data.Draw("E1 Same")
stack_hist.Draw("Same E2")
leg.AddEntry(h_data, "Data "+str(h_data.Integral()),"PL")
leg.AddEntry(h_data, "Data/MC "+str(SF),"L")
print("Integral of BKG:" , stack_hist.Integral())   
print("Integral of DATA:" , h_data.Integral())
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.Draw()
Draw_CMS_header(lumi_label=target_lumi_dict[era_tag])
Draw_era_tag(era_tag=era_tag)
Pad1.RedrawAxis()
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
h_ratio = h_data.Clone('h_ratio')
h_ratio.Sumw2()
h_ratio.SetStats(0)
h_ratio.Divide(stack_hist)
h_ratio.SetMaximum(2.0)
h_ratio.SetMinimum(0.0)
#h_ratio.SetMaximum(min(1.7,((h_ratio.GetMaximum()+h_ratio.GetMinimum())/2e+8)))
#h_ratio.SetMinimum(max(0.7,h_ratio.GetMinimum()-0.3))
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

h_err=ROOT.TH1F("h_err","h_err", *plot['binning'])
for i in range(1, h_ratio.GetNbinsX()+1):
        bincontent=stack_hist.GetBinContent(i)
        print("binerror:",binerror)
	binerror=obtain_bin_sys(1)
	#binerror=(bincontent*0.5)
        if h_ratio.GetBinContent(i)!=0:
		binerror=(stack_hist.GetBinError(i)/stack_hist.GetBinContent(i))
	#binerror2=stack_hist.GetBinError(i)
        #print("stack_hist_BINCONTENT:",stack_hist.GetBinContent(i),"bincontent:",h_err.GetBinContent(i),"binerror:",binerror)
        h_err.SetBinError(i,binerror)
h_err.SetFillColor(14)
h_err.SetFillStyle(3001)
h_err.Draw("same e2")

cb.cd()
cb.Draw()
#cb.SaveAs("/eos/user/m/myalvac/www/G1Jets_withUNC/mtntestsamplesNEW.png")
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+signal_samp+'_High_pt_test.png')
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+signal_samp+'_High_pt_test.pdf')
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+signal_samp+'_High_pt_test.root')
cb.Clear()
del h_Stack
