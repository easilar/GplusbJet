from array import array
from math import *
from helper import getChain, Set_axis_pad2, Set_axis_pad1, Draw_CMS_header, getPlotFromChain , setElist
import ROOT
import os
import operator
from configure import *
ROOT.gStyle.SetOptStat(0)

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl"

plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Correlation/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)


plot = {"var":"ngoodbJet","binning":(3,0,3),"x_axis":"b Jet Multiplicity","y_axis":"Events","bin":(),"histoname":"b Jet Multiplicity","title":"nbJet","bin_set":(False , 1)}
if not plot["bin_set"][0]: plot["bin"] = plot["binning"]

bkg = {"sample":"QCD_HT", "weight":"(1)",  "tex":"QCD", "color":ROOT.kBlue-3}
bkg["chain_all"] = getChain(stype="bkg",sname=bkg["sample"],pfile=pfile)
print(bkg["sample"],bkg["chain_all"][1],bkg["chain_all"][2])
bkg["chain"] = bkg["chain_all"][0]
bkg["weight"] = "(weight*puweight*PhotonSF)"

signal_dict = {"sample":"G1Jet_Pt", "weight":"(1)", "chain_all":getChain(stype="signal",sname="G1Jet_Pt",pfile=pfile), "tex":"GJets", "color":ROOT.kAzure+6}
signal_dict["weight"] = "(weight*puweight*PhotonSF)"
signal_dict["chain"] = signal_dict["chain_all"][0]
print(signal_dict["chain"].GetEntries())
c = signal_dict
c = bkg
plot_cut = "ngoodPhoton==1&&(goodPhoton_pt>=225)&&ngoodGenPhoton==0"
#plot_cut = "ngoodPhoton==1&&(goodPhoton_pt>=225)&&(abs(goodGenPhoton_pt-goodPhoton_pt)/goodPhoton_pt<0.1)"

print("Obtain 2D histo")
plot_Corr = getPlotFromChain(c['chain'], "ngoodbJet:goodPhoton_hoe", (20,0,0.35,3,0,3), cutString = "&&".join([plot_cut,"(1)"]), weight = c["weight"])

c1 = ROOT.TCanvas()
ROOT.gStyle.SetOptStat(0)
#rCSplot.GetYaxis().SetRangeUser(0,0.1)
plot_Corr.GetXaxis().SetTitle("Photon H over E")
plot_Corr.GetYaxis().SetTitle("b-tag multiplicity")
plot_Corr.SetMarkerStyle(0)
plot_Corr.SetMarkerSize(0)
plot_Corr.SetLineStyle(1)
plot_Corr.SetLineWidth(2)
plot_Corr.Draw("COLZ")
c1.Print(plots_path+'/Correlation_'+c["tex"]+'.png')
c1.Print(plots_path+'/Correlation_'+c["tex"]+'.pdf')
c1.Print(plots_path+'/Correlation_'+c["tex"]+'.root')


