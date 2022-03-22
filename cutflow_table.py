import helper
from helper import *
import ROOT
import os
import operator

import configure
from configure import *


path = "/eos/user/m/myalvac/tables/"
if not os.path.exists(path):
  os.makedirs(path)

afs_dir = "/afs/cern.ch/user/m/myalvac/GPlusbJets_UL"
pfile = afs_dir+"/samples_orig.pkl"
sample_dic = pickle.load(open(pfile,'rb'))

signal_samples = [ 
{"sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_150To250","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter&&HLT_Photon175)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_150To250_2016"]},
{"sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_250To400","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter&&HLT_Photon175)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_250To400_2016"]},
{"sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_400To675","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter&&HLT_Photon175)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_400To675_2016"]},
{"sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_675ToInf","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter&&HLT_Photon175)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_675ToInf_2016"]},
]

pt_binning = [[225,300],[300,350],[350,400],[400,500],[500,700],[700,1000],[1000,2000]]
#pt_binning = [[225,300],[300,350]]

ofile = file(path+'cut_flow_table','w')
doc_header = '\\documentclass{article}\\usepackage[english]{babel}\\usepackage{graphicx}\\usepackage[margin=0.5in]{geometry}\\begin{document}'
ofile.write(doc_header)
ofile.write("\n")
table_header = '\\begin{table}[ht]\\begin{center}\\resizebox{\\textwidth}{!}{\\begin{tabular}{c | c | c | c | c | c | c | c | c | c}'
ofile.write(table_header)
ofile.write("\n")
binning = 'binning'+ '&'+ 'cuts'
ofile.write(binning)
for sample in signal_samples:
    line = '&'+sample['sample'] 
    ofile.write(line)
    ofile.write("\n")
line_end = '\\\ \\hline'
ofile.write(line_end)
ofile.write("\n")
for bin1 in pt_binning:
  ptcut = "Photon_pt>="+str(bin1[0])+"&&"+"Photon_pt<"+str(bin1[1])
  ofile.write(str(bin1))
  ngood_vtx_cut = "(PV_npvsGood>=1)"
  met_filters = sample["met_filters"]
  single_photon_cut = "Sum$(Photon_cutBased>=3&&Photon_pt>=40&&abs(Photon_eta)<1.4)>=1"
  njet_tight = "Sum$(Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=6&&Jet_puId>=7)>=1"
  ntightDeepBJets = "Sum$(Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=6&&Jet_puId>=7 && Jet_btagDeepFlavB>="+str(sample['btagWP'])+")"
  cut_0b = ntightDeepBJets+"==0"
  cut_1b = ntightDeepBJets+"==1"
  cut_2b = ntightDeepBJets+"==2"
  cuts = [
  {'cut':"&&".join(['(1)']), 'label':'no cut'},\
  {'cut':"&&".join([ngood_vtx_cut]), 'label': 'PV\_npvsGood'},\
  {'cut':"&&".join([ngood_vtx_cut,met_filters]), 'label': 'MET FILTERS'},\
  {'cut':"&&".join([ngood_vtx_cut,met_filters,single_photon_cut]), 'label':'Single Photon'},\
  {'cut':"&&".join([ngood_vtx_cut,met_filters,single_photon_cut,njet_tight]), 'label': 'Presel' },\
  {'cut':"&&".join([ngood_vtx_cut,met_filters,single_photon_cut,cut_0b]), 'label': 'gamma+0bjets' },\
  {'cut':"&&".join([ngood_vtx_cut,met_filters,single_photon_cut,cut_1b]), 'label': 'gamma+1bjets' },\
  {'cut':"&&".join([ngood_vtx_cut,met_filters,single_photon_cut,cut_2b]), 'label': 'gamma+2bjets'},\
  ]
  for cut in cuts:
    #print cut['label']
    #print cut['cut']
    currentCUT = "&&".join([cut['cut'],ptcut])
    print(currentCUT)
    cut_line = '&'+cut['label']
    ofile.write(cut_line)
    for sample in signal_samples:
      ch = ROOT.TChain("Events")
      ch.Add(sample['chain']['dir']+'/*.root')
      tot_yields = 0
      #sample["weight"] = sample["lumi_weight"]+"*(weight*puweight*PhotonSF)"
      sample["weight"] = sample["chain"]['xsec']*1000*sample["lumi_weight"]*(1/float(sample["chain"]["nevents"]))
      nEntry = ch.GetEntries()
      y_remain = getYieldFromChain(ch,cutString = currentCUT,weight = str(sample["weight"]), returnError = True)
      print(tot_yields , y_remain)
      print(y_remain[0])
      tot_yields = y_remain
      print(tot_yields)
      line_yield = '&' + str(format((tot_yields[0]),'.1f'))+'\pm'+str(format((tot_yields[1]),'.1f'))
      #line_err = '&' + str(format((tot_yields[1]["err"]),'.1f'))
      ofile.write(line_yield)
      #ofile.write(line_err)
    ofile.write('\\\\')
    ofile.write('\n')
  ofile.write('\hline')
  ofile.write('\n')
table_end = '\end{tabular}}\end{center}\caption{CutFlow}\label{tab:CutFlow}\end{table}'
ofile.write(table_end)
ofile.write("\n")
doc_end = '\\end{document}'
ofile.write(doc_end)
ofile.close()
print("Written", ofile.name)
