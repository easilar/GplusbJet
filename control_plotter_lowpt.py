import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist
import ROOT
import os
import operator

import configure
from configure import *

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--test", dest="test", default=False, action="store", help="can be true or false")
parser.add_option("--plot", dest="plot", default="Photon_bin_pt", action="store", help="can be Photon_eta , LPhoton_pt ... ")
parser.add_option("--region", dest="region", default="single_photon", action="store", help="can be 0b, 1b, 2b, presel ")
(options, args) = parser.parse_args()

plot_index = options.plot

#ROOT.setTDRStyle()
ROOT.gStyle.SetOptStat(0)


plot = plotlist[plot_index]
if not plot["bin_set"][0]: plot["bin"] = plot["binning"]

region = options.region

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl"

test = options.test
plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Control_Plots/G1Jet/'
if test: 
	plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/WithData/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)

plot_sig_stack = True


#bkg chain al 
#bkg listof dicts  olustur
bkg_list = [
{"sample":"QCD_HT", "weight":"(1)",  "tex":"QCD", "color":ROOT.kBlue-3}
]

#signal chain al
signal_dict = {"sample":"G1Jet_Pt", "weight":"(1)", "chain_all":getChain(stype="signal",sname="G1Jet_Pt",pfile=pfile,test=test), "tex":"GJets", "color":ROOT.kAzure+6}
signal_dict["weight"] = "(weight*puweight*PhotonSF)"


print(signal_dict["sample"],signal_dict["chain_all"][1],signal_dict["chain_all"][2])
#data dict al
#data_dict = {"sample":"SinglePhoton", "weight":"(1)", "chain":getChain(stype="data",sname="SinglePhoton",pfile=pfile,test=test)[0], "tex":"SinglePhoton", "color":ROOT.kBlack}

print("start taking chain.")
chain_165 = ROOT.TChain("Events")
chain_165.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/High_PT/Run2016B_02Apr2020-v1/merged/*.root")
chain_165.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/High_PT/Run2016C_02Apr2020-v1/merged/*.root")
chain_165.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/High_PT/Run2016D_02Apr2020-v1/merged/*.root")
chain_165.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/High_PT/Run2016E_02Apr2020-v1/merged/*.root")
chain_165.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/High_PT/Run2016F_02Apr2020-v1/merged/*.root")
chain_165.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/High_PT/Run2016G_02Apr2020-v1/merged/*.root")
chain_165.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/High_PT/Run2016H_02Apr2020-v1/merged/*.root")
data_dict_165 = {"sample":"SinglePhoton", "weight":"(1)", "chain":chain_165, "tex":"SinglePhoton", "color":ROOT.kBlack}
print("chain 165 is sobtained")
'''
chain_120 = ROOT.TChain("Events")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#print(getYieldFromChain(chain_120, cutString = "&&".join(["ngoodPhoton==1","(goodPhoton_pt>=145&&goodPhoton_pt<180)","(HLT_Photon120_R9Id90_HE10_IsoM)"]), weight = "1"))
data_dict_120 = {"sample":"SinglePhoton", "weight":"weight_trig_HLT_Photon120", "chain":chain_120, "tex":"SinglePhoton", "color":ROOT.kBlack}
print("chain 120 is obtained")
'''
chain_90 = ROOT.TChain("Events")
chain_90.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_90/HLT_Photon90_R9Id90_*.root")
chain_90.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_90/HLT_Photon90_R9Id90_*.root")
chain_90.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_90/HLT_Photon90_R9Id90_*.root")
chain_90.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_90/HLT_Photon90_R9Id90_*.root")
chain_90.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_90/HLT_Photon90_R9Id90_*.root")
chain_90.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_90/HLT_Photon90_R9Id90_*.root")
chain_90.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_90/HLT_Photon90_R9Id90_*.root")
data_dict_90 = {"sample":"SinglePhoton", "weight":"weight_trig_HLT_Photon90", "chain":chain_90, "tex":"SinglePhoton", "color":ROOT.kBlack}
print("chain 90 is obtained")

chain_75 = ROOT.TChain("Events")
chain_75.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_75/HLT_Photon75_R9Id90_*.root")
chain_75.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_75/HLT_Photon75_R9Id90_*.root")
chain_75.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_75/HLT_Photon75_R9Id90_*.root")
chain_75.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_75/HLT_Photon75_R9Id90_*.root")
chain_75.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_75/HLT_Photon75_R9Id90_*.root")
chain_75.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_75/HLT_Photon75_R9Id90_*.root")
chain_75.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_75/HLT_Photon75_R9Id90_*.root")
data_dict_75 = {"sample":"SinglePhoton", "weight":"weight_trig_HLT_Photon75", "chain":chain_75, "tex":"SinglePhoton", "color":ROOT.kBlack}
print("chain 75 is obtained")

chain_50 = ROOT.TChain("Events")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
data_dict_50 = {"sample":"SinglePhoton", "weight":"weight_trig_HLT_Photon50", "chain":chain_50, "tex":"SinglePhoton", "color":ROOT.kBlack}
print("chain 50 is obtained")

chain_36 = ROOT.TChain("Events")
chain_36.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_36/HLT_Photon36_R9Id90_*.root")
chain_36.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_36/HLT_Photon36_R9Id90_*.root")
chain_36.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_36/HLT_Photon36_R9Id90_*.root")
chain_36.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_36/HLT_Photon36_R9Id90_*.root")
chain_36.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_36/HLT_Photon36_R9Id90_*.root")
chain_36.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_36/HLT_Photon36_R9Id90_*.root")
chain_36.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_36/HLT_Photon36_R9Id90_*.root")
data_dict_36 = {"sample":"SinglePhoton", "weight":"weight_trig_HLT_Photon36", "chain":chain_36, "tex":"SinglePhoton", "color":ROOT.kBlack}
print("chain 36 is obtained")


#define photon cuts
selections={
"jetphoton": jet_photon_cut,\
"jet_cut":jet_cut,\
"no_cut":"(1)",\
"vtx_cut":ngood_vtx_cut,\
"met_filters": "&&".join([ngood_vtx_cut,met_filters]),\
"single_photon":"ngoodPhoton==1&&(goodPhoton_pt<225)",\
"presel":"&&".join([ngood_vtx_cut,met_filters,single_photon_tight_cut,muon_veto,electron_veto]),\
"1b":sel_1b,\
"2b":sel_2b,\
"0b":sel_0b,\
}

plot_cut = selections[region]
bkg_Int = 0
for bkg in bkg_list:
    bkg["chain_all"] = getChain(stype="bkg",sname=bkg["sample"],pfile=pfile,test=test)
    print(bkg["sample"],bkg["chain_all"][1],bkg["chain_all"][2])
    bkg["chain"] = bkg["chain_all"][0]
    bkg["weight"] = "(weight*puweight*PhotonSF)"
    h = getPlotFromChain(bkg['chain'], plot['var'], plot['bin'], cutString = plot_cut+"&&ngoodGenPhoton==0&&(abs(goodGenPhoton_pt-goodPhoton_pt)/goodPhoton_pt>0.1)&&!(event==2599441)", weight = bkg["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
    bkg["histo"] = h
    bkg_Int+=bkg["histo"].Integral()
    del h
    print(bkg["chain"].GetEntries())

signal_dict["chain"] = signal_dict["chain_all"][0]
print(signal_dict["chain"].GetEntries())
#data_dict["chain"] = data_dict["chain"]
if plot_sig_stack : bkg_list.append(signal_dict)
print('Ploting starts......')

data_dict_165["histo"] = getPlotFromChain(data_dict_165["chain"], plot['var'], plot['bin'], cutString = "&&".join(["ngoodPhoton==1&&goodPhoton_pt<225","(goodPhoton_pt>=180&&goodPhoton_pt<225)","(HLT_Photon165_R9Id90_HE10_IsoM)"]), weight = data_dict_165["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
print("165 is taken")
#data_dict_120["histo"] = getPlotFromChain(data_dict_120["chain"], plot['var'], plot['bin'], cutString = "&&".join(["ngoodPhoton==1&&goodPhoton_pt<225","(goodPhoton_pt>=145&&goodPhoton_pt<180)","(weight_trig_HLT_Photon120>0)","(HLT_Photon120_R9Id90_HE10_IsoM)"]), weight = data_dict_120["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
#print("120 is taken")
data_dict_90["histo"] = getPlotFromChain(data_dict_90["chain"], plot['var'], plot['bin'], cutString = "&&".join(["ngoodPhoton==1&&goodPhoton_pt<225","(goodPhoton_pt>=100&&goodPhoton_pt<145)","(weight_trig_HLT_Photon90>0)","HLT_Photon90_R9Id90_HE10_IsoM"]), weight = data_dict_90["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
print("90 is taken")
data_dict_75["histo"] = getPlotFromChain(data_dict_75["chain"], plot['var'], plot['bin'], cutString = "&&".join(["ngoodPhoton==1&&goodPhoton_pt<225","(goodPhoton_pt>=90&&goodPhoton_pt<100)","(weight_trig_HLT_Photon75>0)","HLT_Photon75_R9Id90_HE10_IsoM"]), weight = data_dict_75["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
print("75 is taken")
data_dict_50["histo"] = getPlotFromChain(data_dict_50["chain"], plot['var'], plot['bin'], cutString = "&&".join(["ngoodPhoton==1&&goodPhoton_pt<225","(goodPhoton_pt>=60&&goodPhoton_pt<90)","(weight_trig_HLT_Photon50>0)","HLT_Photon50_R9Id90_HE10_IsoM"]), weight = data_dict_50["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
print("50 is taken")
data_dict_36["histo"] = getPlotFromChain(data_dict_36["chain"], plot['var'], plot['bin'], cutString = "&&".join(["ngoodPhoton==1&&goodPhoton_pt<225","(goodPhoton_pt>=40&&goodPhoton_pt<60)","(weight_trig_HLT_Photon36>0)","HLT_Photon36_R9Id90_HE10_IsoM"]), weight = data_dict_36["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
print("36 is taken")

signal_dict["histo"] = getPlotFromChain(signal_dict["chain"], plot['var'], plot['bin'], cutString = plot_cut+"&&(abs(goodGenPhoton_pt-goodPhoton_pt)/goodPhoton_pt<0.1)", weight = signal_dict["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
signalPlusbkg = bkg_Int+signal_dict["histo"].Integral()
#SF = data_dict["histo"].Integral()/signalPlusbkg
#print("MC Scale Factor: ", SF)
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
	#h.Scale(SF)
	h.SetFillColor(color)
	h.SetLineColor(ROOT.kBlack)
	h.SetLineWidth(1)
	h.GetXaxis().SetNdivisions(505)
	h.GetYaxis().SetTitle(plot['y_axis'])
	h.SetTitle("")
	Set_axis_pad1(h)
	leg.AddEntry(h, bkg['tex']+" "+str(round(h.Integral())),"f")
	print("Integral of"+bkg['tex']+":" , h.Integral()) 
        h_Stack.Add(bkg["histo"])
        #leg_sig.AddEntry(bkg["histo"], bkg['tex'],"f")
	del h
print('BKG loop finished.......')
if plot["bin_set"][0]: stack_hist=ROOT.TH1F("stack_hist","stack_hist", plot['bin'][0],plot['bin'][1]) 
else: stack_hist=ROOT.TH1F("stack_hist","stack_hist",plot['bin'][0],plot['bin'][1],plot['bin'][2])
stack_hist.Merge(h_Stack.GetHists())
max_bin = stack_hist.GetMaximum()*10000
h_Stack.SetMaximum(max_bin) 
h_Stack.SetMinimum(0.00001)
h_Stack.SetTitle("")
#start data
color = ROOT.kBlack
h_data = data_dict_165["histo"]
#h_data.Add(data_dict_120["histo"])
h_data.Add(data_dict_90["histo"])
h_data.SetMarkerStyle(20)
h_data.SetMarkerSize(1.1)
h_data.SetLineColor(color)
h_data.GetXaxis().SetTitle(plot['x_axis'])
h_data.GetYaxis().SetTitle(plot['y_axis'])
h_data.SetTitle("")
#h_data.GetYaxis().SetTitleSize(0.05)
#h_data.GetYaxis().SetLabelSize(0.05)
Set_axis_pad1(h_data)
h_data.Draw("E1")
h_data.SetMaximum(max_bin)
h_data.SetMinimum(0.11)
h_Stack.Draw("HistoSame")
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
leg.AddEntry(h_data, "Data "+str(h_data.Integral()),"PL")
print("Integral of BKG:" , stack_hist.Integral())   
print("Integral of DATA:" , h_data.Integral())
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
h_ratio = h_data.Clone('h_ratio')
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
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+'Low_pt_weight.png')
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+'Low_pt_weight.pdf')
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+'Low_pt_weight.root')
cb.Clear()
del h_Stack
