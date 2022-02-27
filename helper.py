import ROOT
import os
import sys
import pickle
import json
from math import pi, sqrt, cos, sin, sinh, log



def getChain(year=2016,stype="signal",sname="GJets",pfile="/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_orig.pkl",datatype="all", test=False):
	sample_dic = pickle.load(open(pfile,'rb'))
	schain = ROOT.TChain("Events")
	if stype=="data":
		sxsec = "(1)" 
		if datatype=="all":
			sdict = sample_dic[year][stype][sname]
			for d in sdict.keys():
				slist = os.listdir(sdict[d]["dir"])
				if test: slist = slist[:1]
				for f in slist:
					schain.Add(sdict[d]["dir"]+"/"+f)
		else :
			sdict = sample_dic[year][stype][sname][datatype]
			slist = os.listdir(sdict["dir"])
			if test: slist = slist[:1]
			for f in slist:
				schain.Add(sdict["dir"]+"/"+f)
	else:
		if sample_dic[year][stype][sname].keys()[0].startswith(sname) or sname.startswith("CR"):
			for s_bin in sample_dic[year][stype][sname].keys():
				sdict = sample_dic[year][stype][sname][s_bin]
				slist = os.listdir(sdict["dir"])
				sxsec = sdict['xsec']
				if test: slist = slist[:1]
				for f in slist:
					schain.Add(sdict["dir"]+"/"+f)
		else:
			sdict = sample_dic[year][stype][sname]
			sdir = sdict['dir']
			sxsec = sdict['xsec']
			slist = os.listdir(sdir)
			if test : slist = slist[:1]
			for f in slist:
				schain.Add(sdir+"/"+f)
	nevents = schain.GetEntries() 
	return (schain, nevents, sxsec, sdict)

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
   if lumi_label=="" : tex.DrawLatex(0.96,0.96,str(lumi_label)+"    (13 TeV)")
   else : tex.DrawLatex(0.96,0.96,str(lumi_label)+" fb^{-1} (13 TeV)")
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
   tex.DrawLatex(0.29,0.96,CMS_Tag)
   return

def Draw_era_tag(era_tag):
   tex = ROOT.TLatex()
   tex.SetNDC()
   tex.SetTextFont(61)
   tex.SetTextSize(0.05)
   tex.SetLineWidth(2)
   tex.DrawLatex(0.25,0.8, era_tag)	
   return

def applyLumi(origFilePath,newfilePath,cert_json_path):
	data = json.load(open(cert_json_path))
	curfile = origFilePath
	newfilename = newfilePath
	ch = ROOT.TChain("Events")
	ch.Add(curfile)
	nentries = ch.GetEntries()
	print(" Creating new root-file ...")
	newFile = ROOT.TFile(newfilename,"recreate")
	print(" Creating new tree ...")
	newchain = ch.CloneTree(0)
	tree = newchain.GetTree()
	print(nentries)
	for jentry in range(nentries):
		ch.GetEntry(jentry)
		run = ch.GetLeaf('run').GetValue()
		lumi = ch.GetLeaf('luminosityBlock').GetValue()
		nPhoton = ch.GetLeaf('nPhoton').GetValue()
		nJet = ch.GetLeaf('nJet').GetValue()
		PV_npvsGood = ch.GetLeaf('PV_npvsGood').GetValue()
		Flag_goodVertices = ch.GetLeaf('Flag_goodVertices').GetValue()
		Flag_1 = ch.GetLeaf('Flag_globalSuperTightHalo2016Filter').GetValue()
		Flag_2 = ch.GetLeaf('Flag_HBHENoiseFilter').GetValue()
		Flag_3 = ch.GetLeaf('Flag_HBHENoiseIsoFilter').GetValue()
		Flag_4 = ch.GetLeaf('Flag_EcalDeadCellTriggerPrimitiveFilter').GetValue()
		Flag_5 = ch.GetLeaf('Flag_BadPFMuonFilter').GetValue()
		Flag_6 = ch.GetLeaf('Flag_eeBadScFilter').GetValue()
		if (jentry%50000 == 0) : print(jentry,run,lumi)
		if not str(int(run)) in data.keys(): continue
		if not (PV_npvsGood>=1 and nPhoton>=1 and nJet>=1): continue
		if not (Flag_goodVertices and Flag_1 and Flag_2 and Flag_3 and Flag_4 and Flag_5 and Flag_6): continue
		if str(int(run)) in data.keys():
		     for lumiBlock in data[str(int(run))]:
		             if (lumi >= lumiBlock[0] and lumi <= lumiBlock[1] ) : tree.Fill()
	newFile.cd()
	tree.Write()
	return

def applyminCut(origChain,newfilePath):
	newfilename = newfilePath
	ch = origChain
	nentries = ch.GetEntries()
	ch.Draw(">>eList", "PV_npvsGood>=1&&nPhoton>=1&&nJet>=1")
	elist = ROOT.gDirectory.Get("eList")
	number_events = elist.GetN()
	print(" Creating new root-file ...")
	newFile = ROOT.TFile(newfilename,"recreate")
	print(" Creating new tree ...")
	newchain = ch.CloneTree(0)
	tree = newchain.GetTree()
	print(number_events)
	for jentry in range(number_events):
		ch.GetEntry(elist.GetEntry(jentry))
		if (jentry%50000 == 0) : print(jentry)
		tree.Fill()
	newFile.cd()
	tree.Write()
	newFile.Write()
	newFile.Map()
	newFile.Close()
	return

def setElist(c,cut):
	c.Draw(">>eList", cut)
	elist = ROOT.gDirectory.Get("eList")
	c.SetEventList(elist)	
	return c

def deltaPhi(phi1, phi2):
  dphi = phi2-phi1
  if  dphi > pi: dphi -= 2.0*pi
  if dphi <= -pi: dphi += 2.0*pi
  return abs(dphi)

def deltaR(phi1,phi2,eta1,eta2):
  return sqrt(deltaPhi(phi1, phi2)**2 + (eta1 - eta2)**2)


def matching_particles(RecoPhotons=None, GenPhotons=None, pt_ratio=0.0, dr_cone=0.0):
	"""

	:param RecoPhotons: List
	:param GenPhotons: List
	:param pt_ratio: float
	:param dr_cone: float
	:return: tuple of two dictionaries

	selected => {1: {1st recoPhotn}, 2: { 2nd recoPhot}} selected[1]
	matched => {1: {match 1st recoPhot}, 2: {match 2nd reco} }
	selected , matched = matching_particles()

	"""
	
	if not RecoPhotons or not GenPhotons:
		return []

	selected_list = {}
	matched_list = {}

	for i, photon in enumerate(RecoPhotons):  # Matching GenPhoton-RecoPhoton in cone dR
		dR = []
		dRm = []
		for j, GenPhoton in enumerate(GenPhotons):
			dR_Pho_Match = deltaR(photon["phi"], GenPhoton["phi"], photon["eta"], GenPhoton["eta"])
			PtRatio = (GenPhoton["pt"]-photon["pt"]) / (GenPhoton["pt"])
			dR.append({'index': j, 'dR': dR_Pho_Match, 'PtRatio': PtRatio})

		dRm = sorted(dR, key=lambda x: x['dR'])

		matched_photons = None
		for k in dRm:
			# print abs((i['PtRatio']))
			if abs(k['PtRatio']) < pt_ratio:
				matched_photons = GenPhotons[dRm[0]['index']]
				break
			else:
				continue

		if dRm[0]['dR'] <= dr_cone:
			selected_list[i] = photon
			matched_list[i] = matched_photons
	    # sel = {1: photon, 2: photon} mat = {1: [], 2: []}

    # select the biggest pt from the photons
    	#photon_biggest_pt = max([(key, val['pt']) for key, val in selected_list.items()], key=lambda x: x[1])
    	#selected_list = list(selected_list[photon_biggest_pt[0]])
    	#matched_list = list(matched_list[photon_biggest_pt[0]])

	return selected_list, matched_list,dRm[0]['dR']





def matching(RecoPhoton=None, GenPhoton=None, pt_ratio=0.0, dr_cone=0.0):
	"""

	:param RecoPhoton: dict
	:param GenPhoton: dict
	:param pt_ratio: float
	:param dr_cone: float
	:return: bool and 1 dict if True

	selected => {1: {1st recoPhotn}, 2: { 2nd recoPhot}} selected[1]
	matched => {1: {match 1st recoPhot}, 2: {match 2nd reco} }
	selected , matched = matching_particles()

	"""


	Match = False
	matched = {}
		

	dR_Pho_Match = deltaR(RecoPhoton["phi"], GenPhoton["phi"], RecoPhoton["eta"], GenPhoton["eta"])
	PtRatio = abs(GenPhoton["pt"]-RecoPhoton["pt"]) / (GenPhoton["pt"])
	#dRm.append({'index': j, 'dR': dR_Pho_Match, 'PtRatio': PtRatio})
	GenPhoton['dR'] = dR_Pho_Match
	GenPhoton['PtRatio']=  PtRatio


	matched_photon = None
	if abs(GenPhoton['PtRatio']) < pt_ratio and GenPhoton['dR'] <= dr_cone:
				matched_photon = GenPhoton
				Match = True

	if Match == True:
			matched = matched_photon

	return (matched , Match) 

def getbTagSF(bdict,flavor,pt,eta,disc):
	btagging_dict = bdict
	f = flavor
	pt = pt
	eta = abs(eta)
	disc = disc
	pt_lis_LB = btagging_dict[f]["pt_lis_LB"]
	pt_lis_UB = btagging_dict[f]["pt_lis_UB"]
	pt_UB = pt_lis_UB[pt_lis_UB>=pt][0]
	pt_LB = pt_lis_LB[pt_lis_LB<pt][-1]
	#print("pt bins :",btagging_dict[f].keys())
	#print("pt:",pt,pt_LB,pt_UB)
	eta_lis_LB = btagging_dict[f][(pt_LB,pt_UB)]["eta_lis_LB"]
	eta_lis_UB = btagging_dict[f][(pt_LB,pt_UB)]["eta_lis_UB"]
	if len(eta_lis_LB)==1:
		eta_UB = eta_lis_UB[0]
		eta_LB = eta_lis_LB[0]
	else:
		eta_UB = eta_lis_UB[eta_lis_UB>=eta][0]
		eta_LB = eta_lis_LB[eta_lis_LB<eta][-1]
	#print("eta:",eta,eta_LB,eta_UB)
	disc_lis_LB = btagging_dict[f][(pt_LB,pt_UB)][(eta_LB,eta_UB)]["disc_lis_LB"]
	disc_lis_UB = btagging_dict[f][(pt_LB,pt_UB)][(eta_LB,eta_UB)]["disc_lis_UB"]
	disc_UB = disc_lis_UB[disc_lis_UB>=disc][0]
	disc_LB = disc_lis_LB[disc_lis_LB<disc][-1]
	#print("disc",disc,disc_LB,disc_UB)
	exec("temp_btagSF="+btagging_dict[f][(pt_LB,pt_UB)][(eta_LB,eta_UB)][(disc_LB,disc_UB)]['formula'].replace("x",str(disc)))
	#print("SF",temp_btagSF)
	return temp_btagSF
