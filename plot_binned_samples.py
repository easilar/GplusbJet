import ROOT
import pickle

from helper import *
from configure import *

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_orig.pkl"

sample_dic = pickle.load(open(pfile,'rb'))
#sname = "GJets_Pt"
#sname = "G1Jet_Pt"
sname = "QCD_HT"
stype = "bkg"
#stype = "signal"
sdict = sample_dic[2016][stype][sname]
gjets = sample_dic[2016]["signal"]["G1Jet_Pt"]
#cut = "(Photon_cutBased>=3&&Photon_pt>200&&abs(Photon_eta)<1.4)"
cut = "Photon_cutBased>=3&&Photon_pt>200&&abs(Photon_eta)<1.4&&Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=1&&Jet_pt[0]>100"
#cut = "(1)"
cb = ROOT.TCanvas("cb","cb",564,232,600,600)
cb.cd()
h_Stack = ROOT.THStack('h_Stack','h_Stack')
#color = [ROOT.kBlue , ROOT.kBlue-7 , ROOT.kBlue+7 , ROOT.kBlue+3, ROOT.kBlue-3,ROOT.kPink-9,ROOT.kPink+10,ROOT.kAzure,ROOT.kAzure-4,ROOT.kAzure+6]
color_qcd = ROOT.kAzure+6
color_gjets = ROOT.kBlue-3
ROOT.gPad.SetLogy()
leg = ROOT.TLegend(0.65,0.5,0.93,0.925)
leg.SetBorderSize(1)
for ci,bin_name in enumerate(sdict.keys()):
	if bin_name == "QCD_HT_200To300" : continue
	if bin_name == "QCD_HT_100To200" : continue
	if bin_name == "QCD_HT_50To100" : continue
	c = ROOT.TChain("Events")
	c.Add(sdict[bin_name]["dir"]+"/*.root")
	weight = sdict[bin_name]["xsec"]*1000*target_lumi*(1/float(sdict[bin_name]["nevents"]))
	plot = getPlotFromChain(c,"Photon_pt[0]",(100,0,2000),cutString = cut ,weight=str(weight))
	#plot = getPlotFromChain(c,"Sum$(Jet_pt)",(200,0,5000),cutString = cut ,weight=str(weight))
	#plot.GetXaxis().SetTitle('H_{T}')
	#plot.SetFillColor(color[ci])	
	plot.SetFillColor(color_qcd)	
	plot.SetLineColor(ROOT.kBlack)
	h_Stack.Add(plot)
leg.AddEntry(plot,"QCD_HT" ,"f")
for ci,bin_name in enumerate(gjets.keys()):
        c = ROOT.TChain("Events")
        c.Add(gjets[bin_name]["dir"]+"/*.root")
        weight = gjets[bin_name]["xsec"]*1000*target_lumi*(1/float(gjets[bin_name]["nevents"]))
        plot = getPlotFromChain(c,"Photon_pt[0]",(100,0,2000),cutString = cut ,weight=str(weight))
        #plot = getPlotFromChain(c,"Sum$(Jet_pt)",(200,0,5000),cutString = cut ,weight=str(weight))
        #plot.GetXaxis().SetTitle('H_{T}')
        #plot.SetFillColor(color[ci])   
        plot.SetFillColor(color_gjets)
        plot.SetLineColor(ROOT.kBlack)
        h_Stack.Add(plot)
leg.AddEntry(plot,"G1Jet" ,"f")
ch_data = getChain(stype="data",sname="SinglePhoton",pfile=pfile)
ch = ch_data[0]
plot = getPlotFromChain(ch,"Photon_pt[0]",(100,0,2000),cutString = cut ,weight="(1)")
plot.Draw("E1")
h_Stack.Draw("HistoSame")
h_data.Draw("E1 Same")
leg.AddEntry(h_data, "Data","PL")
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.Draw()
cb.Draw()
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/Photon_pt.png")
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/Photon_pt.pdf")
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Test_Plots/Photon_pt.root")
