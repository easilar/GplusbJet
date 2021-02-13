import ROOT
import helper
from helper import *
target_lumi = 35.9
sample_dic = pickle.load(open("samples_orig.pkl",'rb'))
sdic = sample_dic[2016]['bkg']['QCD_HT']
c = ROOT.TChain("Events")
c.Add(sdic['QCD_HT_50To100']['dir']+"/*.root")
cut = "(HLT_Photon175 && (Photon_pt>200) && (abs(Photon_eta)<1.4442) && Sum$(Jet_pt>40 && abs(Jet_eta)<2.4 && Jet_jetId>=7 && Jet_puId>=7)>=1 && (Jet_pt[0]>100) && (Jet_pt>40))"
weight = sdic['QCD_HT_50To100']["xsec"]*1000*target_lumi*(1/float(sdic['QCD_HT_50To100']["nevents"]))
cb = ROOT.TCanvas("cb", "cb", 564,232,600,600)
cb.cd()
ROOT.gPad.SetLogy()
plot = getPlotFromChain(c,"Photon_pt[0]", (100,0,2000), cutString = cut, weight = str(weight))
plot.Draw("Histo")
cb.Draw()
cb.SaveAs("MTN.png")

