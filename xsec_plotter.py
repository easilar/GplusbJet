import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist, Draw_era_tag
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
(options, args) = parser.parse_args()
exec("ndiv="+options.ndiv)
exec("divIndex="+options.divIndex)
plot_index = options.plot

#ROOT.setTDRStyle()
ROOT.gStyle.SetOptStat(0)


plot = plotlist[plot_index]
if not plot["bin_set"][0]: plot["bin"] = plot["binning"]

region = options.region

signal_samp = options.s_samp

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets_UL/samples_ana.pkl"

year = 2017
era_tag = "UL 2017"
lumi_weight = float(41.48)/100 

test = options.test
plots_path = '/eos/user/e/ecasilar/www/SMPVJ_Gamma_BJETS/Plots/UL/'+str(year)+'/xsec_plots/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)
  os.system('cp /eos/user/e/ecasilar/www/index.php /eos/user/e/ecasilar/www/SMPVJ_Gamma_BJETS/')
  os.system('cp /eos/user/e/ecasilar/www/index.php /eos/user/e/ecasilar/www/SMPVJ_Gamma_BJETS/Plots/')
  os.system('cp /eos/user/e/ecasilar/www/index.php /eos/user/e/ecasilar/www/SMPVJ_Gamma_BJETS/Plots/UL/')
  os.system('cp /eos/user/e/ecasilar/www/index.php /eos/user/e/ecasilar/www/SMPVJ_Gamma_BJETS/Plots/UL/'+str(year)+'/')
  os.system('cp /eos/user/e/ecasilar/www/index.php /eos/user/e/ecasilar/www/SMPVJ_Gamma_BJETS/Plots/UL/'+str(year)+'/xsec_plots/')


#signal chain al

if signal_samp == "G1Jet_Pt":
	signal_dict = {"sample":"G1Jet_LHEGpt", "weight":"(1/(41.48*1000))", "chain_all":getChain(year=year,stype="signal",sname="G1Jet_LHEGpt",pfile=pfile,test=test), "tex":"MC: G+1Jet", "color":ROOT.kAzure+6}
	signal_dict["weight"] = str(lumi_weight)+"*(weight*puweight*PhotonSF/(41.48*1000))"


print(signal_dict["sample"],signal_dict["chain_all"][1],signal_dict["chain_all"][2])


#define photon cuts
selections={
"jetphoton": jet_photon_cut,\
"jet_cut":jet_cut,\
"no_cut":"(1)",\
"vtx_cut":ngood_vtx_cut,\
"met_filters": "&&".join([ngood_vtx_cut,met_filters]),\
"single_photon":"ngoodPhoton==1&&(goodPhoton_pt>=225)",\
"presel":"ngoodPhoton==1&&HLT_Photon200&&(goodPhoton_pt>=225)&&goodJet_pt[0]>100",\
"1b":"ngoodbJet==1&&ngoodPhoton==1&&(goodPhoton_pt>=225)",\
"2b":"ngoodbJet==2&&ngoodPhoton==1&&(goodPhoton_pt>=225)",\
"0b":"ngoodbJet==0&&ngoodPhoton==1&&(goodPhoton_pt>=225)",\
}

hightweightcut="!(event==50233261||event==171503688||event==331789209)"
plot_cut = selections[region]

signal_dict["chain"] = signal_dict["chain_all"][0]
print(signal_dict["chain"].GetEntries())
print('Ploting starts......')


signal_dict["histo"] = getPlotFromChain(signal_dict["chain"], plot['var'], plot['bin'], cutString = plot_cut, weight = signal_dict["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
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

leg_sig = ROOT.TLegend(0.7,0.8,0.9,0.925)
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
Pad1.SetTopMargin(0.06)
Pad1.SetBottomMargin(0.1)
Pad1.SetFrameFillStyle(0)
Pad1.SetFrameBorderMode(0)
Pad1.SetFrameFillStyle(0)
Pad1.SetFrameBorderMode(0)
Pad1.SetLogy()
ROOT.gStyle.SetErrorX(.5)
h_sig = getPlotFromChain(signal_dict["chain"], plot['var'], plot['bin'], cutString = plot_cut, weight = signal_dict["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
#h_sig.SetFillColor(signal_dict["color"])
h_sig.SetLineColor(signal_dict["color"])
h_sig.SetLineWidth(2)
h_sig.GetXaxis().SetNdivisions(505)
h_sig.GetYaxis().SetTitle('#frac{d #sigma}{d p_{T}}(pb)')
h_sig.SetTitle("")
h_sig.SetMarkerColor(signal_dict["color"])
h_sig.SetMarkerStyle(20)
h_sig.SetMarkerSize(1.1)
h_sig.GetXaxis().SetTitle(plot['x_axis'])
h_sig.Draw("E1")
leg_sig.AddEntry(h_sig, signal_dict['tex'],"l")
leg_sig.SetFillColor(0)
leg_sig.SetLineColor(0)
leg_sig.Draw()
print("Integral of Signal:" , h_sig.Integral()) 
Draw_CMS_header(lumi_label=target_lumi)
Draw_era_tag(era_tag=era_tag)
Pad1.RedrawAxis()
cb.cd()
'''
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
Func.Draw("same")
'''
cb.cd()
cb.Draw()
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+signal_samp+'_High_pt_test.png')
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+signal_samp+'_High_pt_test.pdf')
cb.SaveAs(plots_path+'_'+region+'_'+plot['title']+signal_samp+'_High_pt_test.root')
cb.Clear()
