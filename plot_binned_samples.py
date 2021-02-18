import ROOT
import pickle

from helper import *
from configure import *

pfile = "samples_orig.pkl"

cplot = plotlist["PV_npvsGood"]
if not cplot["bin_set"][0]: cplot["bin"] = cplot["binning"]

sample_dic = pickle.load(open(pfile,'rb'))
#sname = "GJets_Pt"
#sname = "G1Jet_Pt"
sname = "QCD_HT"
stype = "bkg"
plot_QCD=False
#stype = "signal"
sdict = sample_dic[2016][stype][sname]
gjets = sample_dic[2016]["signal"]["G1Jet_Pt"]
cut = "Photon_cutBased>=3&&Photon_pt>200&&abs(Photon_eta)<1.4"
#cut = "Photon_cutBased>=3&&Photon_pt>200&&abs(Photon_eta)<1.4&&Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=7&&Jet_puId>=7&&Jet_pt[0]>100"
#cut = "Photon_cutBased>=3&&Photon_pt>200&&abs(Photon_eta)<1.4&&Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=1&&Jet_pt[0]>100"
#cut = "(1)"
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
Pad1.SetBottomMargin(0)
Pad1.SetFrameFillStyle(0)
Pad1.SetFrameBorderMode(0)
Pad1.SetFrameFillStyle(0)
Pad1.SetFrameBorderMode(0)
Pad1.SetLogy()


h_Stack = ROOT.THStack('h_Stack','h_Stack')
color = [ROOT.kBlue , ROOT.kBlue-7 , ROOT.kBlue+7 , ROOT.kBlue+3, ROOT.kBlue-3,ROOT.kPink-9,ROOT.kPink+10,ROOT.kAzure,ROOT.kAzure-4,ROOT.kAzure+6,ROOT.kRed,ROOT.kGreen]
color_gjets = ROOT.kAzure+6
color_qcd = ROOT.kBlue-3
#ROOT.gPad.SetLogy()
leg = ROOT.TLegend(0.65,0.5,0.93,0.925)
leg.SetBorderSize(1)
if plot_QCD:
	for ci,bin_name in enumerate(sdict.keys()):
		if bin_name == "QCD_HT_200To300" : continue
		if bin_name == "QCD_HT_100To200" : continue
		if bin_name == "QCD_HT_50To100" : continue
		c = ROOT.TChain("Events")
		c.Add(sdict[bin_name]["dir"]+"/*.root")
		weight = sdict[bin_name]["xsec"]*1000*target_lumi*(1/float(sdict[bin_name]["nevents"]))
		plot = getPlotFromChain(c,cplot["var"],cplot["binning"],cutString = cut ,weight=str(weight))
		plot.SetFillColor(color_qcd)	
		h_Stack.Add(plot)
		plot.SetLineColor(ROOT.kBlack)
		#plot = getPlotFromChain(c,"Sum$(Jet_pt)",(200,0,5000),cutString = cut ,weight=str(weight))
		plot.GetYaxis().SetTitle(cplot['y_axis'])
		#plot.SetFillColor(color[ci])	
	leg.AddEntry(plot,"QCD_HT" ,"f")
chain_dict = getChain(stype="bkg",sname="QCD_HT",pfile="samples_ana.pkl")
cQCD = chain_dict[0]
plot = getPlotFromChain(cQCD,cplot["var"],cplot["binning"],cutString = cut ,weight="weight")
leg.AddEntry(plot,"QCD_HT" ,"f")

#chain_dict = getChain(stype="bkg",sname="QCD_HT",pfile="/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl")
#cQCD = chain_dict[0]
#plot = getPlotFromChain(cQCD,"Photon_pt[0]",(40,0,2000),cutString = cut ,weight="weight")
#plot = getPlotFromChain(cQCD,"Sum$(Jet_pt)",(200,0,5000),cutString = cut ,weight="weight")
plot.SetFillColor(color_qcd)	
plot.SetLineColor(ROOT.kBlack)
plot.GetYaxis().SetTitle(cplot['y_axis'])
h_Stack.Add(plot)
#cGJEtss = getChain(sname="G1Jet_Pt",pfile="/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl")
#cGJEts = cGJEtss[0]
#plot = getPlotFromChain(cGJEts,"Photon_pt[0]",(40,0,2000),cutString = cut ,weight="weight")
#plot = getPlotFromChain(cGJEts,"Sum$(Jet_pt)",(200,0,5000),cutString = cut ,weight="weight")
#plot.GetXaxis().SetTitle('H_{T}')
#plot.SetFillColor(color[ci])   
print("start gjets")
for ci,bin_name in enumerate(gjets.keys()):
	print(gjets[bin_name])
	if "50To100" in bin_name: continue
	if not "_NOExt" in bin_name: continue
	c = ROOT.TChain("Events")
	c.Add(gjets[bin_name]["dir"]+"/*.root")
	weight = gjets[bin_name]["xsec"]*1000*target_lumi*(1/float(gjets[bin_name]["nevents"]))
	plot = getPlotFromChain(c,cplot["var"],cplot["binning"],cutString = cut ,weight=str(weight))
	plot.SetFillColor(color_gjets)
	#plot.SetFillColor(color[ci])
	plot.SetLineColor(color_gjets)
	plot.GetYaxis().SetTitle(cplot['y_axis'])
	#leg.AddEntry(plot,bin_name ,"f")
	h_Stack.Add(plot)
leg.AddEntry(plot,"G1Jet_Pt","f")
#stack_hist=ROOT.TH1F("stack_hist","stack_hist",cplot["binning"])
if cplot["bin_set"][0]: stack_hist=ROOT.TH1F("stack_hist","stack_hist", cplot['bin'][0],cplot['bin'][1])
else: stack_hist=ROOT.TH1F("stack_hist","stack_hist",cplot['bin'][0],cplot['bin'][1],cplot['bin'][2])
stack_hist.Merge(h_Stack.GetHists())
max_bin = stack_hist.GetMaximum()*10000
h_Stack.SetMaximum(max_bin)
h_Stack.SetMinimum(0.00001)
h_Stack.SetTitle("")
#plot.SetFillColor(color_gjets)
#plot.SetLineColor(ROOT.kBlack)
#h_Stack.Add(plot)
#ch_data = getChain(stype="data",sname="SinglePhoton",pfile=pfile)
ch_data = getChain(stype="data",sname="SinglePhoton",pfile="samples_ana.pkl")
ch = ch_data[0]
print("obtained data chain")
plot = getPlotFromChain(ch,cplot["var"],cplot["binning"],cutString = cut ,weight="(1)")
#plot = getPlotFromChain(ch,"Sum$(Jet_pt)",(200,0,5000),cutString = cut ,weight="(1)")
h_data = plot
h_data.SetLineColor(ROOT.kBlack)
h_data.GetYaxis().SetTitle(cplot['y_axis'])
h_data.SetTitle("")
Set_axis_pad1(h_data)
plot.Draw("E1")
h_Stack.Draw("HistoSame")
h_Stack.Draw("Histo")
plot.Draw("E1 Same")
leg.AddEntry(plot, "Data","PL")
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.Draw()
Draw_CMS_header(lumi_label=target_lumi)


cb.cd()
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
Func = ROOT.TF1('Func',"[0]",cplot['binning'][1],cplot['binning'][2])
Func.SetParameter(0,1)
Func.SetLineColor(58)
Func.SetLineWidth(2)
h_ratio = h_data.Clone('h_ratio')
h_ratio.Sumw2()
h_ratio.SetStats(0)
h_ratio.Divide(stack_hist)
h_ratio.SetMaximum(2)
h_ratio.SetMinimum(0.01)
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerSize(1.1)
h_ratio.SetMarkerColor(ROOT.kBlack)
h_ratio.SetTitle("")
Set_axis_pad2(h_ratio)
h_ratio.GetYaxis().SetTitle("Data/MC")
h_ratio.GetXaxis().SetTitle(cplot['x_axis'])
h_ratio.GetYaxis().SetNdivisions(505)
h_ratio.Draw("E1")
Func.Draw("same")
h_ratio.Draw("E1 Same")



cb.Draw()
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/"+cplot["title"]+"G1Jet.png")
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/"+cplot["title"]+"G1Jet.pdf")
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/"+cplot["title"]+"G1Jet.root")
