import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist
import ROOT
import os

import configure
from configure import *


from optparse import OptionParser
parser = OptionParser()
parser.add_option("--ref_trig", dest="ref_trig", default="HLT_Photon165_R9Id90_HE10_IsoM", action="store", help="can be HLT_Photon165_R9Id90_HE10_IsoM")
parser.add_option("--prob_trig", dest="prob_trig", default="HLT_Photon175", action="store", help="HLT_Photon175")
parser.add_option("--plot", dest="plot", default="Photon_pt", action="store", help="photon_pt")
(options, args) = parser.parse_args()

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl"
import pickle
sample_dic = pickle.load(open(pfile,'rb'))
chain = getChain(stype="signal",sname="G1Jet_Pt",pfile=pfile,test=False)
c = chain[0]

plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Efficiency_Plots/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)

plot = plotlist[options.plot]
if not plot["bin_set"][0]: plot["bin"] = plot["binning"]

cut = "ngoodPhoton==1"
ref_trig = options.ref_trig 
prop_trig = options.prob_trig

#h_den     = ROOT.TH1F('h_den'    , 'h_den'    , len(gPtBins)-1, gPtBins)
#h_num     = ROOT.TH1F('h_num'    , 'h_num'    , len(gPtBins)-1, gPtBins)
#c.Draw("Photon_pt[0]>>h_den",jet_cut+"*(weight)","goff")
#c = getChain(stype="bkg",sname="QCD",pfile=pfile,test=True)
#c.Draw("Photon_pt[0]>>h_num",jet_cut_trig+"*(weight)","goff")
h_den = getPlotFromChain(c, plot["var"], plot['bin'], cutString = "&&".join([cut,ref_trig]), weight = "(weight*puweight)" ,addOverFlowBin='both',variableBinning=plot["bin_set"])
h_num = getPlotFromChain(c, plot["var"], plot['bin'], cutString = "&&".join([cut,ref_trig,prop_trig]), weight = "(weight*puweight)" ,addOverFlowBin='both',variableBinning=plot["bin_set"])
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
cb.SetBottomMargin(0.08)
cb.SetFrameFillStyle(0)
cb.SetFrameBorderMode(0)
cb.SetFrameFillStyle(0)
cb.cd()
h_ratio = h_num.Clone('h_ratio')
h_ratio.Sumw2()
h_ratio.SetStats(0)
h_ratio.Divide(h_den)
#h_ratio.SetMaximum(2)
h_ratio.SetMaximum(1.2)
h_ratio.SetMinimum(0.01)
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerSize(1.1)
h_ratio.SetMarkerColor(ROOT.kBlack)
h_ratio.SetTitle("")
#h_ratio.GetXaxis().SetTitle('p_{T}(#gamma)[GeV]')
h_ratio.GetXaxis().SetTitle(plot["x_axis"])
h_ratio.GetYaxis().SetTitle("Trigger Efficiency")
ROOT.gStyle.SetOptStat(0)
Draw_CMS_header(lumi_label=target_lumi)
h_ratio.Draw("E1")
cb.Draw()
cb.SaveAs(plots_path+'_GJEtsTrigEff_'+plot["var"]+prop_trig+ref_trig+'_zoomed.png')
cb.SaveAs(plots_path+'_GJEtsTrigEff_'+plot["var"]+prop_trig+ref_trig+'_zoomed.pdf')
cb.SaveAs(plots_path+'_GJEtsTrigEff_'+plot["var"]+prop_trig+ref_trig+'_zoomed.root')
cb.Clear()





