import ROOT
import pickle

from helper import *
from configure import *

ROOT.gStyle.SetOptStat(0)

pfile = "/afs/cern.ch/work/e/ecasilar/GplusbJets_UL/samples_orig.pkl"

#https://hypernews.cern.ch/HyperNews/CMS/get/luminosity/1041.html

data_pufile = ROOT.TFile("PUfiles/PileupHistogram-goldenJSON-13tev-2018-69200ub-99bins.root")
h_data = data_pufile.Get("pileup")
h_data.SetLineColor(ROOT.kBlack)
h_data.Scale(1/h_data.Integral())
h_data.SetTitle("")
h_data.GetYaxis().SetTitle("a.u.")
print(h_data.GetNbinsX())

data_pufile_p5 = ROOT.TFile("PUfiles/PileupHistogram-goldenJSON-13tev-2018-72400ub-99bins.root")
h_data_p5 = data_pufile_p5.Get("pileup")
h_data_p5.SetLineColor(ROOT.kRed)
h_data_p5.Scale(1/h_data_p5.Integral())
h_data_p5.SetTitle("")
h_data_p5.GetYaxis().SetTitle("a.u.")

data_pufile_m5 = ROOT.TFile("PUfiles/PileupHistogram-goldenJSON-13tev-2018-66000ub-99bins.root")
h_data_m5 = data_pufile_m5.Get("pileup")
h_data_m5.SetLineColor(ROOT.kRed)
h_data_m5.Scale(1/h_data_m5.Integral())
h_data_m5.SetTitle("")
h_data_m5.GetYaxis().SetTitle("a.u.")

h_mc = ROOT.TH1F("h_mc","h_mc",99,0,99)
#mix_2016_25ns_Moriond17MC_PoissonOOTPU_cfi.py
#bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
#bin_contents = [1.78653e-05 ,2.56602e-05 ,5.27857e-05 ,8.88954e-05 ,0.000109362 ,0.000140973 ,0.000240998 ,0.00071209 ,0.00130121 ,0.00245255 ,0.00502589 ,0.00919534 ,0.0146697 ,0.0204126 ,0.0267586 ,0.0337697 ,0.0401478 ,0.0450159 ,0.0490577 ,0.0524855 ,0.0548159 ,0.0559937 ,0.0554468 ,0.0537687 ,0.0512055 ,0.0476713 ,0.0435312 ,0.0393107 ,0.0349812 ,0.0307413 ,0.0272425 ,0.0237115 ,0.0208329 ,0.0182459 ,0.0160712 ,0.0142498 ,0.012804 ,0.011571 ,0.010547 ,0.00959489 ,0.00891718 ,0.00829292 ,0.0076195 ,0.0069806 ,0.0062025 ,0.00546581 ,0.00484127 ,0.00407168 ,0.00337681 ,0.00269893 ,0.00212473 ,0.00160208 ,0.00117884 ,0.000859662 ,0.000569085 ,0.000365431 ,0.000243565 ,0.00015688 ,9.88128e-05 ,6.53783e-05 ,3.73924e-05 ,2.61382e-05 ,2.0307e-05 ,1.73032e-05 ,1.435e-05 ,1.36486e-05 ,1.35555e-05 ,1.37491e-05 ,1.34255e-05 ,1.33987e-05 ,1.34061e-05 ,1.34211e-05 ,1.34177e-05 ,1.32959e-05 ,1.33287e-05]

#https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2017_25ns_UltraLegacy_PoissonOOTPU_cfi.py
'''
bins = [    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
    30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
    50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    90, 91, 92, 93, 94, 95, 96, 97, 98]
bin_contents = [
    1.1840841518e-05, 3.46661037703e-05, 8.98772521472e-05, 7.47400487733e-05, 0.000123005176624,
    0.000156501700614, 0.000154660478659, 0.000177496185603, 0.000324149805611, 0.000737524009713,
    0.00140432980253, 0.00244424508696, 0.00380027898037, 0.00541093042612, 0.00768803501793,
    0.010828224552, 0.0146608623707, 0.01887739113, 0.0228418813823, 0.0264817796874,
    0.0294637401336, 0.0317960986171, 0.0336645950831, 0.0352638818387, 0.036869429333,
    0.0382797316998, 0.039386705577, 0.0398389681346, 0.039646211131, 0.0388392805703,
    0.0374195678161, 0.0355377892706, 0.0333383902828, 0.0308286549265, 0.0282914440969,
    0.0257860718304, 0.02341635055, 0.0213126338243, 0.0195035612803, 0.0181079838989,
    0.0171991315458, 0.0166377598339, 0.0166445341361, 0.0171943735369, 0.0181980997278,
    0.0191339792146, 0.0198518804356, 0.0199714909193, 0.0194616474094, 0.0178626975229,
    0.0153296785464, 0.0126789254325, 0.0100766041988, 0.00773867100481, 0.00592386091874,
    0.00434706240169, 0.00310217013427, 0.00213213401899, 0.0013996000761, 0.000879148859271,
    0.000540866009427, 0.000326115560156, 0.000193965828516, 0.000114607606623, 6.74262828734e-05,
    3.97805301078e-05, 2.19948704638e-05, 9.72007976207e-06, 4.26179259146e-06, 2.80015581327e-06,
    1.14675436465e-06, 2.52452411995e-07, 9.08394910044e-08, 1.14291987912e-08, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0
]
'''
#https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi.py

bins = [    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
    30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
    50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    90, 91, 92, 93, 94, 95, 96, 97, 98
]

bin_contents = [
    8.89374611122e-07, 1.1777062868e-05, 3.99725585118e-05, 0.000129888015252, 0.000265224848687,
    0.000313088635109, 0.000353781668514, 0.000508787237162, 0.000873670065767, 0.00147166880932,
    0.00228230649018, 0.00330375581273, 0.00466047608406, 0.00624959203029, 0.00810375867901,
    0.010306521821, 0.0129512453978, 0.0160303925502, 0.0192913204592, 0.0223108613632,
    0.0249798930986, 0.0273973789867, 0.0294402350483, 0.031029854302, 0.0324583524255,
    0.0338264469857, 0.0351267479019, 0.0360320204259, 0.0367489568401, 0.0374133183052,
    0.0380352633799, 0.0386200967002, 0.039124376968, 0.0394201612616, 0.0394673457109,
    0.0391705388069, 0.0384758587461, 0.0372984548399, 0.0356497876549, 0.0334655175178,
    0.030823567063, 0.0278340752408, 0.0246009685048, 0.0212676009273, 0.0180250593982,
    0.0149129830776, 0.0120582333486, 0.00953400069415, 0.00738546929512, 0.00563442079939,
    0.00422052915668, 0.00312446316347, 0.00228717533955, 0.00164064894334, 0.00118425084792,
    0.000847785826565, 0.000603466454784, 0.000419347268964, 0.000291768785963, 0.000199761337863,
    0.000136624574661, 9.46855200945e-05, 6.80243180179e-05, 4.94806013765e-05, 3.53122628249e-05,
    2.556765786e-05, 1.75845711623e-05, 1.23828210848e-05, 9.31669724108e-06, 6.0713272037e-06,
    3.95387384933e-06, 2.02760874107e-06, 1.22535149516e-06, 9.79612472109e-07, 7.61730246474e-07,
    4.2748847738e-07, 2.41170461205e-07, 1.38701083552e-07, 3.37678010922e-08, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0
]

for cbin in bins:
	h_mc.SetBinContent(cbin+1,bin_contents[cbin])

h_mc.SetLineColor(ROOT.kGreen)
#h_mc.SetMinimum(0)
h_mc.SetLineWidth(1)
h_mc.SetTitle("")
h_mc.GetYaxis().SetTitle("a.u.")
sample_dic = pickle.load(open(pfile,'rb'))
sname = "G1Jet_Pt"
stype = "signal"
gjets = sample_dic[2018]["signal"]["G1Jet_LHEGpt"]
cut = "(1)"
cb = ROOT.TCanvas("cb","cb",564,232,600,1000)
cb.cd()
leg = ROOT.TLegend(0.1,0.1,0.55,0.4)
leg.SetBorderSize(1)

h_Stack = ROOT.THStack('h_Stack','h_Stack')
color_gjets = ROOT.kBlue-3
#ROOT.gPad.SetLogy()
print("start gjets")
stack_hist=ROOT.TH1F("stack_hist","stack_hist",99,0,99)
for ci,bin_name in enumerate(gjets.keys()):
        print(gjets[bin_name])
        c = ROOT.TChain("Events")
        c.Add(gjets[bin_name]["dir"]+"/*.root")
        weight = gjets[bin_name]["xsec"]*1000*target_lumi*(1/float(gjets[bin_name]["nevents"]))
        plot = getPlotFromChain(c,"Pileup_nTrueInt",(99,0,99),cutString = cut ,weight=str(weight))
	print("INTEGRAL:" , plot.Integral())
        plot.SetFillColor(color_gjets)
        #plot.SetFillColor(color[ci])
        plot.SetLineColor(color_gjets)
        h_Stack.Add(plot)
stack_hist.Merge(h_Stack.GetHists())
stack_hist.Scale(1/stack_hist.Integral())
Pad1 = ROOT.TPad("Pad1", "Pad1", 0,0.55,1,1)
Pad1.Draw()
Pad1.cd()
Pad1.SetFillColor(0)
Pad1.SetBorderMode(0)
Pad1.SetBorderSize(2)
Pad1.SetLogy()
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
h_mc.Draw("L")
stack_hist.Draw("HistoSame")
h_data.Draw("L Same")
h_data_m5.Draw("L Same")
h_data_p5.Draw("L Same")
leg.AddEntry(h_data, "Data (Nominal)","PL")
#leg.AddEntry(h_data_m5, "Data Ref. Trigger","f")
leg.AddEntry(h_data_p5, "Data (XS #pm 5%)","l")
leg.AddEntry(h_mc, "MC 2018 25ns UL","l")
leg.AddEntry(stack_hist, "G + 1Jet: nTrueInt","f")
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.Draw()
cb.cd()
Pad2 = ROOT.TPad("Pad2", "Pad2",  0, 0.3, 1, 0.55)
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
Pad2.SetBottomMargin(0.0)
Pad2.SetFrameFillStyle(0)
Pad2.SetFrameBorderMode(0)
Pad2.SetFrameFillStyle(0)
Pad2.SetFrameBorderMode(0)
Func = ROOT.TF1('Func',"[0]",0,100)
Func.SetParameter(0,1)
Func.SetLineColor(58)
Func.SetLineWidth(2)
h_ratio = h_data.Clone('h_ratio')
h_ratio.Sumw2()
h_ratio.SetStats(0)
h_ratio.Divide(h_mc)
h_ratio.SetMaximum(2)
h_ratio.SetMinimum(0.000)
h_ratio.SetMarkerStyle(20)
h_ratio.SetMarkerSize(0.8)
h_ratio.SetMarkerColor(ROOT.kBlack)
h_ratio.SetTitle("")
#h_ratio.GetXaxis().SetNdivisions(505)
#Set_axis_pad2(h_ratio)
h_ratio.GetYaxis().SetTitle("Correction")
h_ratio.GetXaxis().SetTitle("n True Int")
#h_ratio.GetYaxis().SetNdivisions(505)
h_ratio.Draw("Histo")
Func.Draw("same")
h_ratio.Draw("HistoSame")
cb.cd()
Pad3 = ROOT.TPad("Pad3", "Pad3",  0, 0, 1, 0.3)
Pad3.Draw()
Pad3.cd()
Pad3.SetFillColor(0)
Pad3.SetFillStyle(4000)
Pad3.SetBorderMode(0)
Pad3.SetBorderSize(2)
Pad3.SetTickx(1)
Pad3.SetTicky(1)
Pad3.SetLeftMargin(0.18)
Pad3.SetRightMargin(0.04)
Pad3.SetTopMargin(0)
Pad3.SetBottomMargin(0.1)
Pad3.SetFrameFillStyle(0)
Pad3.SetFrameBorderMode(0)
Pad3.SetFrameFillStyle(0)
Pad3.SetFrameBorderMode(0)
Func1 = ROOT.TF1('Func1',"[0]",0,100)
Func1.SetParameter(0,1)
Func1.SetLineColor(58)
Func1.SetLineWidth(2)
h_unc1 = h_data_p5.Clone('h_unc1')
h_unc1.Sumw2()
h_unc1.SetStats(0)
h_unc1.Divide(h_mc)
h_unc1.SetMarkerStyle(20)
h_unc1.SetMarkerSize(0.8)
h_unc1.SetMarkerColor(ROOT.kBlack)
h_unc1.SetTitle("")
h_unc1.GetYaxis().SetTitle("Rel. Unc.")
h_unc1.GetXaxis().SetTitle("n True Int")
#h_unc1.Add(h_ratio,-1)
h_unc1.SetMaximum(4)
h_unc1.SetMinimum(0)
h_unc1.Divide(h_ratio)
h_unc2 = h_data_m5.Clone('h_unc2')
h_unc2.Sumw2()
h_unc2.SetStats(0)
#h_unc2.Divide(h_mc)
#h_unc2.SetMaximum(2)
#h_unc2.SetMinimum(-8)
h_unc2.SetMarkerStyle(20)
h_unc2.SetMarkerSize(0.8)
h_unc2.SetMarkerColor(ROOT.kBlack)
h_unc2.SetTitle("")
h_unc2.GetYaxis().SetTitle("Rel. Unc.")
h_unc2.GetXaxis().SetTitle("n True Int")
h_unc2.Divide(h_mc)
h_unc2.Divide(h_ratio)
h_unc2.SetMaximum(4)
h_unc2.SetMinimum(0)
h_unc1.Draw("Histo")
h_unc2.Draw("HistoiSame")
Func1.Draw("same")
h_unc1.Draw("HistoSame")
cb.cd()
cb.Draw()
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/UL/2018/PileUP/nTrueInt_G1Jet.png")
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/UL/2018/PileUP/nTrueInt_G1Jet.pdf")
cb.SaveAs("/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/UL/2018/PileUP/nTrueInt_G1Jet.root")
h_ratio.SaveAs("PUfiles/puCorrection_2018UL.root")
