import ROOT
import pickle

from helper import *
from configure import *

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_orig.pkl"

cplot = plotlist["PV_npvsGood"]

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
cb.cd()
h_Stack = ROOT.THStack('h_Stack','h_Stack')
color = [ROOT.kBlue , ROOT.kBlue-7 , ROOT.kBlue+7 , ROOT.kBlue+3, ROOT.kBlue-3,ROOT.kPink-9,ROOT.kPink+10,ROOT.kAzure,ROOT.kAzure-4,ROOT.kAzure+6,ROOT.kRed,ROOT.kGreen]
color_qcd = ROOT.kAzure+6
color_gjets = ROOT.kBlue-3
ROOT.gPad.SetLogy()
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
		#plot.GetXaxis().SetTitle('H_{T}')
		#plot.SetFillColor(color[ci])	
	leg.AddEntry(plot,"QCD_HT" ,"f")
#chain_dict = getChain(stype="bkg",sname="QCD_HT",pfile="/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl")
#cQCD = chain_dict[0]
#plot = getPlotFromChain(cQCD,"Photon_pt[0]",(40,0,2000),cutString = cut ,weight="weight")
#plot = getPlotFromChain(cQCD,"Sum$(Jet_pt)",(200,0,5000),cutString = cut ,weight="weight")
#plot.SetFillColor(color_qcd)	
#plot.SetLineColor(ROOT.kBlack)
#h_Stack.Add(plot)
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
	#plot.SetFillColor(color_gjets)
	plot.SetFillColor(color[ci])
	plot.SetLineColor(ROOT.kBlack)
	leg.AddEntry(plot,bin_name ,"f")
	h_Stack.Add(plot)

#plot.SetFillColor(color_gjets)
#plot.SetLineColor(ROOT.kBlack)
#h_Stack.Add(plot)
#ch_data = getChain(stype="data",sname="SinglePhoton",pfile=pfile)
ch_data = getChain(stype="data",sname="SinglePhoton",pfile="/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl")
ch = ch_data[0]
print("obtained data chain")
plot = getPlotFromChain(ch,cplot["var"],cplot["binning"],cutString = cut ,weight="(1)")
#plot = getPlotFromChain(ch,"Sum$(Jet_pt)",(200,0,5000),cutString = cut ,weight="(1)")
plot.Draw("E1")
h_Stack.Draw("HistoSame")
h_Stack.Draw("Histo")
plot.Draw("E1 Same")
leg.AddEntry(plot, "Data","PL")
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.Draw()
cb.Draw()
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/"+cplot["title"]+"G1Jet.png")
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/"+cplot["title"]+"G1Jet.pdf")
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/"+cplot["title"]+"G1Jet.root")
