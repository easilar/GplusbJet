import ROOT
import pickle

from helper import *
from configure import *

pfile = "samples_ana.pkl"
year = 2016
sample_dic = pickle.load(open(pfile,'rb'))
plots_path = '/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/Trigger/'
if not os.path.exists(plots_path):
  os.makedirs(plots_path)
if year == 2016:
	sname = "SingleMuon_prescaled_NoPtCut_merged"
	trigger_list = ["HLT_Photon36_R9Id90_HE10_IsoM","HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon175"]
	color = [ROOT.kBlue ,ROOT.kMagenta,ROOT.kRed,ROOT.kOrange,ROOT.kGreen,ROOT.kCyan,ROOT.kPink+10]
elif year == 2017:
	sname = "SingleMuon_UL_prescaled_NoPtCut_merged"
	trigger_list = ["HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon200"]
	color = [ROOT.kMagenta,ROOT.kRed,ROOT.kOrange,ROOT.kGreen,ROOT.kCyan,ROOT.kPink+10]
elif year == 2018:
	sname = "SingleMuon_UL_prescaled_NoPtCut_merged"
	trigger_list = ["HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon200"]
	color = [ROOT.kMagenta+3,ROOT.kRed+2,ROOT.kOrange+7,ROOT.kGreen+2,ROOT.kCyan,ROOT.kBlue]
lenght = len(trigger_list)

c = getChain(year=year, stype='data', sname=sname, pfile=pfile, datatype='all', test=False)
print(sname)
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

leg = ROOT.TLegend(0.65,0.5,0.93,0.925)
leg.SetBorderSize(1)
plot = getPlotFromChain(c[0],'goodPhoton_pt', (100,0,1000), weight="(weight_trig)",cutString=trigger_list[0]+"&&(weight_trig>=0)", binningIsExplicit=False, addOverFlowBin='', variableBinning=(False,1))
plot.SetLineColor(ROOT.kBlack)
leg.AddEntry(plot,trigger_list[0] ,"f")
plot.Draw("E1")	
print("Empty plot is created")
del plot	
print("LOOP is coming:")
for i in range(1,lenght):
	print(i)
	plot = getPlotFromChain(c[0],'goodPhoton_pt', (100,0,1000), weight="(weight_trig)",cutString=trigger_list[i]+"&&(weight_trig>=0)", binningIsExplicit=False, addOverFlowBin='', variableBinning=(False,1))		
	plot.SetLineColor(color[i])
	print(color[i])
#	leg.AddEntry(plot,trigger_list[i] ,"f")
	plot.Draw("E1 Same")
	del plot 
#leg.Draw()
cb.cd()
cb.Draw()
cb.SaveAs(plots_path+str(year)+".png")
cb.SaveAs(plots_path+str(year)+".pdf")
cb.SaveAs(plots_path+str(year)+".root")
cb.Clear()
