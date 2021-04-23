import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist
import ROOT
import os
import operator

import configure
from configure import *


from optparse import OptionParser
parser = OptionParser()
parser.add_option("--trig", dest="trig", default="0", action="store", help="can be 0 , 1 ,2...8")
(options, args) = parser.parse_args()

exec("tmp_index="+options.trig)
print type(tmp_index)
index = tmp_index


ROOT.gStyle.SetOptStat(0)
plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Efficiency_Plots/Test/2017/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)

pfile="samples_ana.pkl"

data_dict = {"sample":"SingleMuon", "weight":"(1)", "chain":getChain(year=2017,stype="data",sname="SingleMuon",pfile=pfile)[0], "tex":"SingleMuon", "color":ROOT.kBlack}
prob_triggers = prob_triggers
prob_trigger = prob_triggers[index]

#define photon cuts
num_cut = "&&".join(["Sum$(Photon_cutBased>=3&&Photon_pt>40&&abs(Photon_eta)<1.4)==1",ref_trigger,prob_trigger])
#den_cut = "&&".join(["ngoodPhoton==1",ref_trigger])
den_cut = "&&".join(["Sum$(Photon_cutBased>=3&&Photon_pt>40&&abs(Photon_eta)<1.4)==1",ref_trigger])
print(num_cut)
print(den_cut)
c = data_dict["chain"]
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
h_data_num = getPlotFromChain(c, plot['var'], plot['bin'], cutString =num_cut , weight = "(1)" ,addOverFlowBin='both',variableBinning=plot["bin_set"]) 
Func = ROOT.TF1('Func',"[0]",plot['binning'][1],plot['binning'][2])
Func.SetParameter(0,0.1)
Func.SetLineColor(58)
Func.SetLineWidth(2)

#func = ROOT.TF1('func', '[0]*TMath::Erf((x-[1])/[2])', 40., 500.)  # non def pos erf
func = ROOT.TF1("func", "([0]/(1+ TMath::Exp(-[1]*(x-[2]))))", 40., 2000.) 
#func = ROOT.TF1('func', '0.5 * ([0]*TMath::Erf((x-[1])/[2]) + 1)', 25., 180.) # def pos erf
func.SetParameter(0,  0.68)
func.SetParameter(1,  0.1)
func.SetParameter(2, 160)

func.SetLineColor(ROOT.kRed)
func.SetParName(0, 'plateau')
func.SetParName(1, 'width')
func.SetParName(2, 'threshold')

h_ratio = h_data_num.Clone('h_ratio')
h_ratio.Sumw2()
h_ratio.SetStats(0)
h_ratio.Divide(h_data_den)
h_ratio.SetMaximum(1.2)
#h_ratio.SetMinimum(0.0001)
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
platho = round(fitResult.GetParameter(0),2)
print(platho)
plato_X = 0
for i in range(500):
	print(round(fitResult(threshold+i*1),2))
	if round(fitResult(threshold+i*1),2) == platho :
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
tex.DrawLatex(0.2,0.9,"SingleMuon Run 2017 BCDEF ")
tex.DrawLatex(0.2,0.85,"Ref. Trig.: HLT_IsoMu27 ")
tex.DrawLatex(0.2,0.8,"Prob. Trig.: "+prob_trigger)
tex.DrawLatex(0.2,0.75,"Plateau: "+str(round(platho,2))+", Reached at "+str(round(plato_X,2))+" GeV")
cb.cd()
cb.Draw()
cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+prob_trigger+'Eff_v4.png')
cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+prob_trigger+'Eff_v4.pdf')
cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+prob_trigger+'Eff_v4.root')
cb.Clear()
