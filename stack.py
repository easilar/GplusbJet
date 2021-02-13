import ROOT
import helper
from helper import *
target_lumi = 35.9
sample_dic = pickle.load(open("samples_orig.pkl",'rb'))
sdict = sample_dic[2016]['bkg']['QCD_HT']
cut = "(Photon_cutBased>=3&&Photon_pt>200&&abs(Photon_eta)<1.4)"
cb = ROOT.TCanvas("cb", "cb", 564,232,600,600)
cb.cd()
h_Stack = ROOT.THStack('h_Stack','h_Stack')
color = [ROOT.kBlue,ROOT.kRed,ROOT.kGreen,ROOT.kOrange,ROOT.kYellow,ROOT.kCyan,ROOT.kYellow+4,ROOT.kSpring+10,ROOT.kGray,ROOT.kMagenta]
ROOT.gPad.SetLogy()
for ci,bin_name in enumerate(sdict.keys()):
	c = ROOT.TChain("Events")
	c.Add(sdict[bin_name]['dir']+"/*.root")
	weight = sdict[bin_name]["xsec"]*1000*target_lumi*(1/float(sdict[bin_name]["nevents"]))
	plot = getPlotFromChain(c,"Photon_pt[0]", (100,0,2000), cutString = cut, weight = str(weight))
	plot.SetFillColor(color[ci])
	plot.SetLineColor(ROOT.kBlack)
	h_Stack.Add(plot)
h_Stack.Draw("Histo")
cb.Draw()
cb.SaveAs("QCD_HT.png")
cb.SaveAs("QCD_HT.pdf")
