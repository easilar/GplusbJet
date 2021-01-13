import helper
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist
import ROOT
import os

import configure
from configure import *

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_orig.pkl"
import pickle
sample_dic = pickle.load(open(pfile,'rb'))
c = getChain(stype="bkg",sname="QCD",pfile=pfile,test=True)
#c = getChain(stype="signal",sname="GJets",pfile=pfile,test=True)
c = c[0]

plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Efficiency_Plots/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)

h_den     = ROOT.TH1F('h_den'    , 'h_den'    , len(gPtBins)-1, gPtBins)
h_num     = ROOT.TH1F('h_num'    , 'h_num'    , len(gPtBins)-1, gPtBins)
c.Draw("Photon_pt>>h_den","(1)","goff")
c.Draw("Photon_pt>>h_num","(1)*"+single_photon_tight_cut,"goff")
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
h_ratio.SetMaximum(0.1)
h_ratio.SetMinimum(0.01)
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerSize(1.1)
h_ratio.SetMarkerColor(ROOT.kBlack)
h_ratio.SetTitle("")
h_ratio.GetXaxis().SetTitle('p_{T}(#gamma)[GeV]')
h_ratio.GetYaxis().SetTitle("Photon Selection Efficiency")
ROOT.gStyle.SetOptStat(0)
Draw_CMS_header(lumi_label=target_lumi)
h_ratio.Draw("E1")
cb.Draw()
cb.SaveAs(plots_path+'_QCD_PhotonSelectionEff.png')
cb.SaveAs(plots_path+'_QCD_PhotonSelectionEff.pdf')
cb.SaveAs(plots_path+'_QCD_PhotonSelectionEff.root')
cb.Clear()





