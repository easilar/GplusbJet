import helper
from helper import *
cb = ROOT.TCanvas("cb","cb",564,232,600,600)
cb.SetHighLightColor(2)
cb.Range(0,0,1,1)
cb.SetFillColor(0)
cb.SetBorderMode(0)
cb.SetBorderSize(2)
cb.SetTickx(1)
cb.SetTicky(1)
cb.SetLeftMargin(0.15)
cb.SetRightMargin(0.15)
cb.SetTopMargin(0.06)
cb.SetBottomMargin(0.10)
cb.SetFrameFillStyle(0)
cb.SetFrameBorderMode(0)
cb.SetFrameFillStyle(0)
lumi_weight17 = float(41.8/100)
#Define plots
#plotPhovsDR = ROOT.TH2D("photonvsDR","goodPhoton_pt vs minDR plot", 100,0,6,100,0,1500)
plotJetvsDR = ROOT.TH2D("jetvsDR"," Leading Jet_pt vs minDR plot", 100,0,6,100,0,1500)
#plotPhovsDR.SetXTitle("DeltaR")
#plotPhovsDR.SetYTitle("goodPhoton_pt")
plotJetvsDR.SetXTitle("DeltaR")
plotJetvsDR.SetYTitle("Leading Jet_pt")
#get Chain
signal_dict17 = {"sample":"G1Jet_LHEGpt", "weight":"(1)","chain_all":getChain(year=2017,stype="signal",sname="G1Jet_LHEGpt",pfile="samples_ana.pkl",test=True)[0]}
ch = signal_dict17["chain_all"]
#EventLOOP
#for jentry in range(0, ch.GetEntries()):
for jentry in range(0, ch.GetEntries()):
    ch.GetEntry(jentry)
    ngoodPhoton =ch.GetLeaf("ngoodPhoton").GetValue()
    ngoodJet =ch.GetLeaf("ngoodJet").GetValue()
    goodPhoton_pt = ch.GetLeaf("goodPhoton_pt").GetValue()
    goodJet_pt = ch.GetLeaf("goodJet_pt").GetValue(0)
    goodPhoton_minDR = ch.GetLeaf("goodPhoton_minDR").GetValue()
    weight = ch.GetLeaf("weight").GetValue()
    puweight = ch.GetLeaf("puweight").GetValue()
    PhotonSF = ch.GetLeaf("PhotonSF").GetValue()
    #Calculate weight
    applied_weight = lumi_weight17*weight*puweight*PhotonSF
    #print(applied_weight)
    #print(goodJet_pt,goodJet_pt,goodPhoton_minDR)
    #apply presel cuts
    if not (ngoodPhoton==1 and goodPhoton_pt>225 and goodJet_pt>100): continue

    #print(ngoodPhoton,goodPhoton_pt,goodJet_pt,goodPhoton_minDR)
    #print(goodPhoton_minDR)
    #fill histograms with weights
    #plotPhovsDR.Fill(goodPhoton_minDR,goodPhoton_pt,applied_weight)
    plotJetvsDR.Fill(goodPhoton_minDR,goodJet_pt,applied_weight)
#cb.cd()
#ROOT.gPad.SetLogz()
#plotPhovsDR.Draw('colz')
#cb.SaveAs('/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/UL/2017/Control_Plots/G1Jet/phovsDR.pdf')
#cb.Clear()
cb.cd()
ROOT.gPad.SetLogz()
plotJetvsDR.Draw('colz')
cb.SaveAs('/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/Plots/UL/2017/Control_Plots/G1Jet/jetvsDR.pdf')
