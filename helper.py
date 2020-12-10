import ROOT
import os
import sys
import pickle
from math import pi, sqrt, cos, sin, sinh, log

def getChain(year=2016,stype="signal",sname="GJets",pfile="samples.pkl"):
	sample_dic = pickle.load(open(pfile,'rb'))
	schain = ROOT.TChain("Events")
	#slist = sample_dic[year][stype][sname]['files_list']
 	if stype=="data": 
		print("data ")
		sxsec = "(1)" 
		for d in sample_dic[year][stype][sname].keys():
			print(d)
			for f in os.listdir(sample_dic[year][stype][sname][d]["dir"]):
				print(f)
				schain.Add(sample_dic[year][stype][sname][d]["dir"]+"/"+f)
	else:	
		sdir = sample_dic[year][stype][sname]['dir']
		sxsec = sample_dic[year][stype][sname]['xsec']
		slist = os.listdir(sdir)
		for f in slist:
			schain.Add(sdir+"/"+f)
	nevents = schain.GetEntries() 
	return (schain, nevents, sxsec)

def getYieldFromChain(c, cutString = "(1)", weight = "1", returnError=False, returnVar=False):
  h = ROOT.TH1D('h_tmp', 'h_tmp', 1,0,2)
  h.Sumw2()
  c.Draw("1>>h_tmp", "("+weight+")*("+cutString+")", 'goff')
  res = h.GetBinContent(1)
  resErr = h.GetBinError(1)
#  print "1>>h_tmp", weight+"*("+cutString+")",res,resErr
  del h
  if returnError:
    return res, resErr
  elif returnVar:
    return res, resErr**2
  return res 

def getPlotFromChain(c, var, binning, cutString = "(1)", weight = "weight", binningIsExplicit=False ,addOverFlowBin='',variableBinning=(False, 1)):
  htmp = "h_tmp"
  if binningIsExplicit:
    h = ROOT.TH1D(htmp, htmp, len(binning)-1, array('d', binning))
  else:
    if len(binning)==6:
      h = ROOT.TH2D(htmp, htmp, *binning)
    else:
      h = ROOT.TH1D(htmp, htmp, *binning)
  c.Draw(var+">>%s"%htmp, weight+"*("+cutString+")", 'goff')
  res = h.Clone()
  if variableBinning[0]:
    c.Draw(var+">>h_tmp", weight+"*("+cutString+")", 'goff')
    h.Scale(variableBinning[1],"width")
    res = h.Clone()
  h.Delete()
  del h
  if addOverFlowBin.lower() == "upper" or addOverFlowBin.lower() == "both":
    nbins = res.GetNbinsX()
    res.SetBinContent(nbins , res.GetBinContent(nbins) + res.GetBinContent(nbins + 1))
    res.SetBinError(nbins , sqrt(res.GetBinError(nbins)**2 + res.GetBinError(nbins + 1)**2))
  if addOverFlowBin.lower() == "lower" or addOverFlowBin.lower() == "both":
    res.SetBinContent(1 , res.GetBinContent(0) + res.GetBinContent(1))
    res.SetBinError(1 , sqrt(res.GetBinError(0)**2 + res.GetBinError(1)**2))
  return res

def Set_axis_pad2(histo):
   histo.GetXaxis().SetLabelFont(42)
   histo.GetXaxis().SetLabelOffset(0.007)
   histo.GetXaxis().SetLabelSize(0.11)
   histo.GetXaxis().SetTitleSize(0.14)
   histo.GetXaxis().SetTitleOffset(0.9)
   histo.GetXaxis().SetTitleFont(42)
   histo.GetYaxis().SetTitle("Data/Pred.")
   histo.GetYaxis().SetDecimals()
   histo.GetYaxis().SetNdivisions(505)
   histo.GetYaxis().SetLabelFont(42)
   histo.GetYaxis().SetLabelOffset(0.007)
   histo.GetYaxis().SetLabelSize(0.11)
   histo.GetYaxis().SetTitleSize(0.14)
   histo.GetYaxis().SetTitleOffset(0.52)
   histo.GetYaxis().SetTitleFont(42)
   histo.GetZaxis().SetLabelFont(42)
   histo.GetZaxis().SetLabelOffset(0.007)
   histo.GetZaxis().SetLabelSize(0.05)
   histo.GetZaxis().SetTitleSize(0.06)
   histo.GetZaxis().SetTitleFont(42)
   return

def Set_axis_pad1(histo):
   histo.GetXaxis().SetLabelFont(42)
   histo.GetXaxis().SetLabelOffset(0.007)
   histo.GetXaxis().SetLabelSize(0.05)
   histo.GetXaxis().SetTitleSize(0.06)
   histo.GetXaxis().SetTitleOffset(0.9)
   histo.GetXaxis().SetTitleFont(42)
   histo.GetYaxis().SetLabelFont(42)
   histo.GetYaxis().SetLabelOffset(0.007)
   histo.GetYaxis().SetLabelSize(0.05)
   histo.GetYaxis().SetTitleSize(0.06)
   histo.GetYaxis().SetTitleOffset(1.35)
   histo.GetYaxis().SetTitleFont(42)
   histo.GetZaxis().SetLabelFont(42)
   histo.GetZaxis().SetLabelOffset(0.007)
   histo.GetZaxis().SetLabelSize(0.05)
   histo.GetZaxis().SetTitleSize(0.06)
   histo.GetZaxis().SetTitleFont(42)
   return

def Draw_CMS_header(lumi_label=12.88,CMS_Tag="Preliminary"):
   tex = ROOT.TLatex()
   tex.SetNDC()
   tex.SetTextAlign(31)
   tex.SetTextFont(42)
   tex.SetTextSize(0.05)
   tex.SetLineWidth(2)
   tex.DrawLatex(0.96,0.96,str(lumi_label)+" fb^{-1} (13 TeV)")
   tex = ROOT.TLatex()
   tex.SetNDC()
   tex.SetTextFont(61)
   tex.SetTextSize(0.05)
   tex.SetLineWidth(2)
   tex.DrawLatex(0.18,0.96,"CMS")
   tex = ROOT.TLatex()
   tex.SetNDC()
   tex.SetTextFont(52)
   tex.SetTextSize(0.05)
   tex.SetLineWidth(2)
   tex.DrawLatex(0.26,0.96,CMS_Tag)
   return

