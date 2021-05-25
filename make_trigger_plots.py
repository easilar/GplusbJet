import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist
import ROOT
import os
import operator

import configure
from configure import *
#ROOT.gROOT.Reset()


from optparse import OptionParser
parser = OptionParser()
parser.add_option("--trig", dest="trig", default="0", action="store", help="can be 0 , 1 ,2...8")
(options, args) = parser.parse_args()

exec("tmp_index="+options.trig)
index = tmp_index
#ref_trigger = "HLT_Photon165_R9Id90_HE10_IsoM"
#ref_trigger = "(1)"

#ROOT.gStyle.SetOptStat(0)
plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Efficiency_Plots/Test/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)
pfile="samples_ana.pkl"
#data_dict = {"sample":"SinglePhoton", "weight":"(weight_trig*(weight_trig>0.0))", "chain":getChain(stype="data",sname="SinglePhoton_prescaled_NoPtCut_merged",pfile=pfile)[0], "tex":"SinglePhoton", "color":ROOT.kBlack}
#data dict al
#data_dict = {"sample":"SinglePhoton", "weight":"(1)", "chain":getChain(stype="data",sname="SinglePhoton",pfile=pfile)[0], "tex":"SinglePhoton", "color":ROOT.kBlack}
#data_dict = {"sample":"SingleMuon", "weight":"(1)", "chain":getChain(stype="data",sname="SingleMuon",pfile=pfile)[0], "tex":"SingleMuon", "color":ROOT.kBlack}
print("start taking chain.")

chain_50 = ROOT.TChain("Events")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
chain_50.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_50/HLT_Photon50_R9Id90_*.root")
data_dict_50 = {"sample":"SinglePhoton", "weight":"(1)", "chain":chain_50, "tex":"SinglePhoton", "color":ROOT.kBlack}
#data_dict_50 = {"sample":"SinglePhoton", "weight":"(weight_trig_HLT_Photon50)", "chain":chain_50, "tex":"SinglePhoton", "color":ROOT.kBlack}
print("chain 50 is obtained")
'''
chain_120 = ROOT.TChain("Events")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
data_dict_120 = {"sample":"SinglePhoton", "weight":"(1)", "chain":chain_120, "tex":"SinglePhoton", "color":ROOT.kBlack}
#data_dict_120 = {"sample":"SinglePhoton", "weight":"(weight_trig_HLT_Photon120)", "chain":chain_120, "tex":"SinglePhoton", "color":ROOT.kBlack}

#chain_120 = ROOT.TChain("Events")
#chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#data_dict_120 = {"sample":"SingleMuon", "weight":"(1)", "chain":chain_120, "tex":"SingleMuon", "color":ROOT.kBlack}
#data_dict_120 = {"sample":"SingleMuon", "weight":"(weight_trig_HLT_Photon120)", "chain":chain_120, "tex":"SingleMuon", "color":ROOT.kBlack}
#print("chain 120 is obtained")

chain_120 = ROOT.TChain("Events")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016B_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016C_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016D_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016E_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016F_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016G_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
chain_120.Add("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SingleMuon/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_120/HLT_Photon120_R9Id90_*.root")
#data_dict_120 = {"sample":"SingleMuon", "weight":"(1)", "chain":chain_90, "tex":"SingleMuon", "color":ROOT.kBlack}
data_dict_120 = {"sample":"SingleMuon", "weight":"(weight_trig_HLT_Photon120)", "chain":chain_120, "tex":"SingleMuon", "color":ROOT.kBlack}

print("chain 165 is obtained")
'''
prob_trigger = prob_triggers[index]
#ref_trigger = prob_triggers[index-1]
#define photon cuts
#presel_event_cut = presel
num_cut = "&&".join(["ngoodPhoton==1",ref_trigger,"weight_trig_HLT_Photon50>0",prob_trigger])
den_cut = "&&".join(["ngoodPhoton==1",ref_trigger,"weight_trig_HLT_Photon50>0"])
print(num_cut)
print(den_cut)
#c = data_dict["chain"]
#c = data_dict_120["chain"]
c = data_dict_50["chain"]
print('Plot loop starting......')
plot = plotlist["Photon_pt"]
if not plot["bin_set"][0]: plot["bin"] = plot["binning"]
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

ROOT.gStyle.SetErrorX(.5)
#start data
h_data_den = getPlotFromChain(c, plot['var'], plot['bin'], cutString =den_cut , weight = "(1)" ,addOverFlowBin='both',variableBinning=plot["bin_set"]) 
#h_data_den = getPlotFromChain(c, plot['var'], plot['bin'], cutString =den_cut ,addOverFlowBin='both',variableBinning=plot["bin_set"]) 
h_data_num = getPlotFromChain(c, plot['var'], plot['bin'], cutString =num_cut , weight = data_dict_50["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"]) 
#h_data_num = getPlotFromChain(c, plot['var'], plot['bin'], cutString =num_cut ,addOverFlowBin='both',variableBinning=plot["bin_set"]) 
Func = ROOT.TF1('Func',"[0]",plot['binning'][1],plot['binning'][2])
Func.SetParameter(0,1)
Func.SetLineColor(58)
Func.SetLineWidth(2)

#func = ROOT.TF1('func', '[0]*TMath::Erf((x-[1])/[2])', 40., 500.)  # non def pos erf
func = ROOT.TF1("func", "([0]/(1+ TMath::Exp(-[1]*(x-[2]))))", 0., 1700.) 
# func = ROOT.TF1('func', '0.5 * ([0]*TMath::Erf((x-[1])/[2]) + 1)', 25., 180.) # def pos erf
func.SetParameter(0,  1.0)
func.SetParameter(1,  0.01)
func.SetParameter(2,60)

func.SetLineColor(ROOT.kRed)
func.SetParName(0, 'plateau')
func.SetParName(1, 'width')
func.SetParName(2, 'threshold')

h_ratio = h_data_num.Clone('h_ratio')
h_ratio.Sumw2()
h_ratio.SetStats(0)
h_ratio.Divide(h_data_den)
h_ratio.SetMaximum(0.03)
h_ratio.SetMinimum(0.001)
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerSize(1.1)
h_ratio.SetMarkerColor(ROOT.kBlack)
h_ratio.SetTitle("")
h_ratio.GetXaxis().SetNdivisions(505)
h_ratio.GetYaxis().SetTitle("Efficiency")
h_ratio.GetXaxis().SetTitle(plot['x_axis'])
h_ratio.GetYaxis().SetNdivisions(505)
h_ratio.Draw("E1")
h_ratio.Fit(func,"R")
fitResult = h_ratio.GetFunction("func")
threshold = fitResult.GetParameter(2)
print(threshold)
platho = round(fitResult.GetParameter(0),3)
print(platho)
plato_X = 0
for i in range(500):
	print(round(fitResult(threshold+i*1),3))
	if round(fitResult(threshold+i*1),3) == platho :
		print(threshold+i*1,fitResult(threshold+i*0.5))
		plato_X = threshold+i*0.5
		break
#Func.Draw("same")
h_ratio.Draw("E1 Same")

tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextFont(61)
tex.SetTextSize(0.05)
tex.SetLineWidth(2)
tex.DrawLatex(0.18,0.96,"CMS")
tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextFont(52)
tex.SetTextSize(0.05)
tex.SetLineWidth(2)
tex.DrawLatex(0.29,0.96,"Preliminary")
tex = ROOT.TLatex()
tex.SetNDC()
tex.SetTextFont(61)
tex.SetTextSize(0.03)
tex.SetLineWidth(2)
#tex.DrawLatex(0.2,0.9,"SingleMuon Run 2016 BCDEFGH ")
tex.DrawLatex(0.2,0.9,"SinglePhoton Run 2016")
tex.DrawLatex(0.2,0.85,"Ref. Trig.: "+ref_trigger)
tex.DrawLatex(0.2,0.8,"Prob. Trig.: "+prob_trigger)
tex.DrawLatex(0.2,0.75,"Plateau: "+str(round(platho,2))+", Reached at "+str(round(plato_X,2))+" GeV")
#tex.DrawLatex(0.2,0.7,"weight = HLT_Photon_50_R9Id90_HE10_IsoM")
tex.DrawLatex(0.2,0.7,"weight = 1")
cb.cd()
cb.Draw()
#cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+prob_trigger+'Eff.png')
#cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+prob_trigger+'Eff.pdf')
#cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+prob_trigger+'Eff.root')
cb.SaveAs(plots_path+plot['title']+data_dict_50["tex"]+'_trig_'+prob_trigger+'_Trig_Weight_Val.png')
cb.SaveAs(plots_path+plot['title']+data_dict_50["tex"]+'_trig_'+prob_trigger+'_Trig_Weight_Val.pdf')
cb.SaveAs(plots_path+plot['title']+data_dict_50["tex"]+'_trig_'+prob_trigger+'_Trig_Weight_Val.root')
cb.Clear()
