import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist
import ROOT
import os
import operator

import configure
from configure import *


from optparse import OptionParser
parser = OptionParser()
parser.add_option("--trig", dest="trig", default=0, action="store", help="can be 0 , 1 ,2")
(options, args) = parser.parse_args()

exec("tmp_index="+options.trig)
print type(tmp_index)
index = tmp_index


ROOT.gStyle.SetOptStat(0)

plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Efficiency_Plots/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)

plotlist = [
{"var":"Photon_pt[0]","binning":(100,0,2000),"x_axis":"p_{T}(#gamma)[GeV]","y_axis":"Events","bin":(len(gPtBins)-1,gPtBins),"histoname":"Leading Photon Pt[GeV]","title":"LPhotonPt","bin_set":(True , 25)}
]

data_dict = {"sample":"SingleMuon", "weight":"(1)", "chain":getChain(stype="data",sname="SingleMuon")[0], "tex":"SingleMuon", "color":ROOT.kBlack}

prob_triggers = [prob_trigger_1 , prob_trigger_2 , prob_trigger_3]
prob_trigger = prob_triggers[index]

#define photon cuts
presel_event_cut = presel
num_cut = "&&".join([presel_event_cut,ref_trigger,prob_trigger])
den_cut = "&&".join([presel_event_cut,ref_trigger])
print(num_cut)
print(den_cut)
c = data_dict["chain"]
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
	Pad1 = ROOT.TPad("Pad1", "Pad1", 0,0.41,1,1)
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
	#start data
        h_data_den = getPlotFromChain(c, plot['var'], plot['bin'], cutString =den_cut , weight = "(1)" ,addOverFlowBin='both',variableBinning=plot["bin_set"]) 
        #h_data_den.SetMarkerStyle(20)
        #h_data_den.SetMarkerSize(1.1)
        h_data_den.SetLineColor(ROOT.kAzure+1)
        h_data_den.SetFillColor(ROOT.kAzure-9)
        h_data_den.GetXaxis().SetTitle(plot['x_axis'])
	h_data_den.GetYaxis().SetTitle(plot['y_axis'])
        h_data_den.SetTitle("")
        Set_axis_pad1(h_data_den)
        h_data_den.Draw("Histo")
        h_data_den.SetMaximum(h_data_den.Integral()*5)
        color = ROOT.kRed
        h_data_num = getPlotFromChain(c, plot['var'], plot['bin'], cutString =num_cut , weight = "(1)" ,addOverFlowBin='both',variableBinning=plot["bin_set"]) 
        #h_data_num.SetMarkerStyle(20)
        #h_data_num.SetMarkerSize(1.1)
        h_data_num.SetLineColor(color)
        h_data_num.GetXaxis().SetTitle(plot['x_axis'])
	h_data_num.GetYaxis().SetTitle(plot['y_axis'])
        h_data_num.SetTitle("")
        Set_axis_pad1(h_data_num)
        h_data_num.Draw("E1 Same")
        h_data_num.SetMaximum(h_data_den.Integral()*5)
        h_data_num.SetMinimum(0.11)
	leg.AddEntry(h_data_num, "Data Num","PL")
	leg.AddEntry(h_data_den, "Data Den","f")
	leg.SetFillColor(0)
	leg.SetLineColor(0)
	leg.Draw()
	Draw_CMS_header(lumi_label=target_lumi)
	#Pad1.RedrawAxis()
	cb.cd()
	Pad2 = ROOT.TPad("Pad2", "Pad2",  0, 0, 1, 0.41)
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
	h_ratio = h_data_num.Clone('h_ratio')
	h_ratio.Sumw2()
	h_ratio.SetStats(0)
	h_ratio.Divide(h_data_den)
	h_ratio.SetMaximum(1.2)
	h_ratio.SetMinimum(0.001)
	h_ratio.SetMarkerStyle(20)
	h_ratio.SetMarkerSize(1.1)
	h_ratio.SetMarkerColor(ROOT.kBlack)
	h_ratio.SetTitle("")
	Set_axis_pad2(h_ratio)
	h_ratio.GetYaxis().SetTitle("Efficiency")
	h_ratio.GetXaxis().SetTitle(plot['x_axis'])
	h_ratio.GetYaxis().SetNdivisions(505)
	h_ratio.Draw("E1")
	Func.Draw("same")
	h_ratio.Draw("E1 Same")
	cb.cd()
	cb.Draw()
	cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+str(index)+'vetolep.png')
	cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+str(index)+'vetolep.pdf')
	cb.SaveAs(plots_path+plot['title']+data_dict["tex"]+'_trig_'+str(index)+'vetolep.root')
	cb.Clear()
