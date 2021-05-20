from array import array
from math import *
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist
import ROOT
import os
import operator
from configure import *
ROOT.gStyle.SetOptStat(0)

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl"

plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/SRCR_Ratio/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)


plot = {"var":"ngoodbJet","binning":(3,0,3),"x_axis":"b Jet Multiplicity","y_axis":"Events","bin":(),"histoname":"b Jet Multiplicity","title":"nbJet","bin_set":(False , 1)}
if not plot["bin_set"][0]: plot["bin"] = plot["binning"]

bkg = {"sample":"QCD_HT", "weight":"(1)",  "tex":"QCD", "color":ROOT.kBlue-3}
bkg["chain_all"] = getChain(stype="bkg",sname=bkg["sample"],pfile=pfile)
print(bkg["sample"],bkg["chain_all"][1],bkg["chain_all"][2])
bkg["chain"] = bkg["chain_all"][0]
bkg["weight"] = "(weight*puweight*PhotonSF)"

plot_cut = "ngoodPhoton==1&&(goodPhoton_pt>=225)&&ngoodGenPhoton==0"
CR = "goodPhoton_hoe>0.03"
SR = "goodPhoton_hoe<=0.03"

print("Obtain Numerator")
rCSnum = getPlotFromChain(bkg['chain'], plot['var'], plot['bin'], cutString = "&&".join([plot_cut,SR]), weight = bkg["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
print("Obtain denominator")
rCSden = getPlotFromChain(bkg['chain'], plot['var'], plot['bin'], cutString = "&&".join([plot_cut,CR]), weight = bkg["weight"] ,addOverFlowBin='both',variableBinning=plot["bin_set"])
rCSplot = rCSnum.Clone()
rCSplot.Divide(rCSden)

c1 = ROOT.TCanvas()
ROOT.gStyle.SetOptStat(0)
#rCSplot.GetYaxis().SetRangeUser(0,0.1)
rCSplot.GetYaxis().SetTitle("R_{CS}")
rCSplot.GetXaxis().SetTitle("b-tag multiplicity")
rCSplot.SetMarkerStyle(0)
rCSplot.SetMarkerSize(0)
rCSplot.SetLineStyle(1)
rCSplot.SetLineWidth(2)
rCSplot.Draw("eh1")
c1.Print(plots_path+'/rCS_QCD.png')
c1.Print(plots_path+'/rCS_QCD.pdf')
c1.Print(plots_path+'/rCS_QCD.root')


