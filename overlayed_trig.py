import ROOT
import pickle

from helper import *
from configure import *

pfile = "samples_ana.pkl"
year = 2016
sample_dic = pickle.load(open(pfile,'rb'))

if year == 2016:
	sname = "SinglePhoton_prescaled_NoPtCut_merged"
	ref_trigger = "(HLT_IsoMu24)"
	trigger_list = [
	{"trigger":"HLT_Photon36_R9Id90_HE10_IsoM","tex":"HLT_Photon36_R9Id90_HE10_IsoM", "color":ROOT.kBlue },
	{"trigger":"HLT_Photon50_R9Id90_HE10_IsoM","tex":"HLT_Photon50_R9Id90_HE10_IsoM", "color":ROOT.kMagenta},
	{"trigger":"HLT_Photon75_R9Id90_HE10_IsoM","tex":"HLT_Photon75_R9Id90_HE10_IsoM", "color":ROOT.kRed},
	{"trigger":"HLT_Photon90_R9Id90_HE10_IsoM","tex":"HLT_Photon90_R9Id90_HE10_IsoM", "color":ROOT.kOrange},
	{"trigger":"HLT_Photon120_R9Id90_HE10_IsoM","tex":"HLT_Photon120_R9Id90_HE10_IsoM", "color":ROOT.kGreen},
	{"trigger":"HLT_Photon165_R9Id90_HE10_IsoM","tex":"HLT_Photon165_R9Id90_HE10_IsoM", "color":ROOT.kCyan }, 
	{"trigger":"HLT_Photon175","tex":"HLT_Photon175_R9Id90_HE10_IsoM", "color":ROOT.kPink+10}
	]

elif year == 2017:
	sname = "SingleMuon_UL_prescaled_NoPtCut_merged"
	ref_trigger = "(HLT_IsoMu27)"
	trigger_list = [
	{"trigger":"HLT_Photon50_R9Id90_HE10_IsoM","tex":"HLT_Photon50_R9Id90_HE10_IsoM", "color":ROOT.kMagenta},
	{"trigger":"HLT_Photon75_R9Id90_HE10_IsoM","tex":"HLT_Photon75_R9Id90_HE10_IsoM", "color":ROOT.kRed},
	{"trigger":"HLT_Photon90_R9Id90_HE10_IsoM","tex":"HLT_Photon90_R9Id90_HE10_IsoM", "color":ROOT.kOrange},
	{"trigger":"HLT_Photon120_R9Id90_HE10_IsoM","tex":"HLT_Photon120_R9Id90_HE10_IsoM", "color":ROOT.kGreen},
	{"trigger":"HLT_Photon165_R9Id90_HE10_IsoM","tex":"HLT_Photon165_R9Id90_HE10_IsoM", "color":ROOT.kCyan }, 
	{"trigger":"HLT_Photon175","tex":"HLT_Photon175_R9Id90_HE10_IsoM", "color":ROOT.kPink+10}
	]
	
elif year == 2018:
	sname = "SingleMuon_UL_prescaled_NoPtCut_merged"
	ref_trigger = "(HLT_IsoMu24)"
	trigger_list = [
	{"trigger":"HLT_Photon50_R9Id90_HE10_IsoM","tex":"HLT_Photon50_R9Id90_HE10_IsoM", "color":ROOT.kMagenta},
	{"trigger":"HLT_Photon75_R9Id90_HE10_IsoM","tex":"HLT_Photon75_R9Id90_HE10_IsoM", "color":ROOT.kRed},
	{"trigger":"HLT_Photon90_R9Id90_HE10_IsoM","tex":"HLT_Photon90_R9Id90_HE10_IsoM", "color":ROOT.kOrange},
	{"trigger":"HLT_Photon120_R9Id90_HE10_IsoM","tex":"HLT_Photon120_R9Id90_HE10_IsoM", "color":ROOT.kGreen},
	{"trigger":"HLT_Photon165_R9Id90_HE10_IsoM","tex":"HLT_Photon165_R9Id90_HE10_IsoM", "color":ROOT.kCyan }, 
	{"trigger":"HLT_Photon175","tex":"HLT_Photon175_R9Id90_HE10_IsoM", "color":ROOT.kPink+10}
	]
	

c = getChain(year=year, stype='data', sname=sname, pfile=pfile, datatype='all', test=False)
print(sname)

plot_int = 0
for trg in trigger_list:
	plot = getPlotFromChain(c[0],'goodPhoton_pt', (25,0,1000), cutString=trg["trigger"]+"&&"+ref_trigger+"&&"+"weight_trig>0", weight='weight_trig',binningIsExplicit=False, addOverFlowBin='both', variableBinning=(False,1))		
#	plot = getPlotFromChain(c[0],'goodPhoton_pt', (25,0,1000), cutString=trg["trigger"]+"&&"+ref_trigger,binningIsExplicit=False, addOverFlowBin='both', variableBinning=(False,1))		
	trg["histo"] = plot
	plot_int+=trg["histo"].Integral()
	del plot


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

Pad1 = ROOT.TPad("Pad1", "Pad1", 0,0.31,1,1)
Pad1.Draw()
Pad1.cd()
#Pad1.Range(-0.7248462,-1.30103,3.302077,3.159352)
Pad1.SetFillColor(0)
Pad1.SetBorderMode(0)
Pad1.SetBorderSize(2)
Pad1.SetTickx(1)
Pad1.SetTicky(1)
Pad1.SetLeftMargin(0.18)
Pad1.SetRightMargin(0.04)
Pad1.SetTopMargin(0.055)
Pad1.SetBottomMargin(0.3)
Pad1.SetFrameFillStyle(0)
Pad1.SetFrameBorderMode(0)
Pad1.SetFrameFillStyle(0)
Pad1.SetFrameBorderMode(0)
Pad1.SetLogy()
#plot1 = ROOT.TH1('plot1','plot1')

print("LOOP is coming:")
for trg in trigger_list:
	print(trg["trigger"])
	color = trg["color"]
	plot = trg["histo"]
	plot.SetLineColor(color)
	plot.SetLineWidth(1)
	plot.SetStats(0)
	if year == 2016: plot.SetTitle("SingleMuon Run 2016 BCDEFGH")
	if year == 2017: plot.SetTitle("SingleMuon_UL Run 2017 BCDEF")
	if year == 2018: plot.SetTitle("SingleMuon_UL Run 2018 ABCD")
	plot.GetXaxis().SetTitle('goodPhoton_pt')
	Set_axis_pad1(plot)
	leg.AddEntry(plot,trg["tex"]+" "+str(round(plot.Integral())) ,"f")
	max_bin = plot.GetMaximum()*10000
	plot.SetMaximum(max_bin)
	plot.SetMinimum(0.11)
	plot.Draw("Histo Same")
	del plot
#tex = ROOT.TLatex()
#tex.DrawLatex(1.,1000000.,"SingleMuon Run 2016 BCDEFGH")
leg.Draw()
Pad1.RedrawAxis()
cb.cd()
cb.Draw()
cb.SaveAs(str(year)+"_weightedSP.png")
cb.SaveAs(str(year)+"_weightedSP.pdf")
cb.SaveAs(str(year)+"_weightedSP.root")
cb.Clear()
