import helper
from helper import *
import ROOT
import os
import operator

import configure
from configure import *


path = '/eos/user/m/myalvac/www/MC_GEN_study/'
if not os.path.exists(path):
  os.makedirs(path)

afs_dir = "/afs/cern.ch/user/m/myalvac/GPlusbJets_UL"
pfile = afs_dir+"/samples_ana.pkl"

sample_dic = pickle.load(open(pfile,'rb'))

EGamma_UL_2018 = [
{"sample_name":"EGamma\_UL\_2018","sample":"EGamma\_UL\_2018","lumi_weight":59.83,"chain":sample_dic[2018]["data"]["EGamma_UL"]["A"]},
{"sample_name":"EGamma\_UL\_2018","sample":"EGamma\_UL\_2018","lumi_weight":59.83,"chain":sample_dic[2018]["data"]["EGamma_UL"]["B"]},
{"sample_name":"EGamma\_UL\_2018","sample":"EGamma\_UL\_2018","lumi_weight":59.83,"chain":sample_dic[2018]["data"]["EGamma_UL"]["C"]},
{"sample_name":"EGamma\_UL\_2018","sample":"EGamma\_UL\_2018","lumi_weight":59.83,"chain":sample_dic[2018]["data"]["EGamma_UL"]["D"]}

]

GJets_DR_0p4_HT_2018 = [
{"sample_name":"GJets\_DR\_0p4\_HT\_2018","sample":"GJets\_DR\_0p4\_HT_2018","lumi_weight":59.83,"chain":sample_dic[2018]["signal"]["GJets_DR_0p4_HT"]["GJets_DR_0p4_HT_100To200_2018"]},
{"sample_name":"GJets\_DR\_0p4\_HT\_2018","sample":"GJets\_DR\_0p4\_HT_2018","lumi_weight":59.83,"chain":sample_dic[2018]["signal"]["GJets_DR_0p4_HT"]["GJets_DR_0p4_HT_200To400_2018"]},
{"sample_name":"GJets\_DR\_0p4\_HT\_2018","sample":"GJets\_DR\_0p4\_HT_2018","lumi_weight":59.83,"chain":sample_dic[2018]["signal"]["GJets_DR_0p4_HT"]["GJets_DR_0p4_HT_400To600_2018"]},
{"sample_name":"GJets\_DR\_0p4\_HT\_2018","sample":"GJets\_DR\_0p4\_HT_2018","lumi_weight":59.83,"chain":sample_dic[2018]["signal"]["GJets_DR_0p4_HT"]["GJets_DR_0p4_HT_600ToInf_2018"]}
]

TGJets_2018 = [
{"sample_name":"TGJets\_2018","sample":"TGJets\_2018","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["TGJets_UL_2018"]}
]
TTGJets_2018 = [
{"sample_name":"TTGJets\_2018","sample":"TTGJets\_2018","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["TTGJets_UL_2018"]}
]

WZG_2018 = [
{"sample_name":"WZG\_2018","sample":"WZG\_2018","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["WZG_UL_2018"]}
]
ZGToLLG_2018 = [
{"sample_name":"ZGToLLG\_2018","sample":"ZGToLLG\_2018","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["ZGToLLG_UL_2018"]}
]
WJetsToLNu_HT = [
{"sample_name":"WJetsToLNu\_HT\_2018","sample":"WJetsToLNu\_2018\_100To200","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["WJetsToLNu_HT"]["WJetsToLNu_HT_UL2018_100To200"]},
{"sample_name":"WJetsToLNu\_HT\_2018","sample":"WJetsToLNu\_2018\_200To400","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["WJetsToLNu_HT"]["WJetsToLNu_HT_UL2018_200To400"]},
{"sample_name":"WJetsToLNu\_HT\_2018","sample":"WJetsToLNu\_2018\_400To600","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["WJetsToLNu_HT"]["WJetsToLNu_HT_UL2018_400To600"]},
{"sample_name":"WJetsToLNu\_HT\_2018","sample":"WJetsToLNu\_2018\_600To800","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["WJetsToLNu_HT"]["WJetsToLNu_HT_UL2018_600To800"]},
{"sample_name":"WJetsToLNu\_HT\_2018","sample":"WJetsToLNu\_2018\_800To1200","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["WJetsToLNu_HT"]["WJetsToLNu_HT_UL2018_800To1200"]},
{"sample_name":"WJetsToLNu\_HT\_2018","sample":"WJetsToLNu\_2018\_1200To2500","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["WJetsToLNu_HT"]["WJetsToLNu_HT_UL2018_1200To2500"]},
{"sample_name":"WJetsToLNu\_HT\_2018","sample":"WJetsToLNu\_2018\_2500ToInf","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["WJetsToLNu_HT"]["WJetsToLNu_HT_UL2018_2500ToInf"]}
]

DYJetsToLL_M_50_HT = [
{"sample_name":"DYJetsToLL\_M\_50\_HT\_2018","sample":"DYJetsToLL_M_50_HT\_2018\_100To200","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["DYJetsToLL_M_50_HT"]["DYJetsToLL_M_50_HT_UL2018_100To200"]},
{"sample_name":"DYJetsToLL\_M\_50\_HT\_2018","sample":"DYJetsToLL_M_50_HT\_2018\_200To400","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["DYJetsToLL_M_50_HT"]["DYJetsToLL_M_50_HT_UL2018_200To400"]},
{"sample_name":"DYJetsToLL\_M\_50\_HT\_2018","sample":"DYJetsToLL_M_50_HT\_2018\_400To600","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["DYJetsToLL_M_50_HT"]["DYJetsToLL_M_50_HT_UL2018_400To600"]},
{"sample_name":"DYJetsToLL\_M\_50\_HT\_2018","sample":"DYJetsToLL_M_50_HT\_2018\_600To800","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["DYJetsToLL_M_50_HT"]["DYJetsToLL_M_50_HT_UL2018_600To800"]},
{"sample_name":"DYJetsToLL\_M\_50\_HT\_2018","sample":"DYJetsToLL_M_50_HT\_2018\_800To1200","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["DYJetsToLL_M_50_HT"]["DYJetsToLL_M_50_HT_UL2018_800To1200"]},
{"sample_name":"DYJetsToLL\_M\_50\_HT\_2018","sample":"DYJetsToLL_M_50_HT\_2018\_1200To2500","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["DYJetsToLL_M_50_HT"]["DYJetsToLL_M_50_HT_UL2018_1200To2500"]},
{"sample_name":"DYJetsToLL\_M\_50\_HT\_2018","sample":"DYJetsToLL_M_50_HT\_2018\_2500ToInf","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["DYJetsToLL_M_50_HT"]["DYJetsToLL_M_50_HT_UL2018_2500ToInf"]}
]

QCD_HT_2018 = [
#{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_50To100","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_50To100"]},
#{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_100To200","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_100To200"]},
#{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_200To300","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_200To300"]},
#{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_300To500","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_300To500"]},
#{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_500To700","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_500To700"]},
{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_700To1000","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_700To1000"]}
#{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_1000To1500","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_1000To1500"]},
#{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_1500To2000","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_1500To2000"]},
#{"sample_name":"QCD\_HT\_2018","sample":"QCD\_HT\_2018\_2000ToInf","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_HT_UL2018"]["QCD_HT_UL2018_2000ToInf"]}
]

QCD_bEnriched_HT_2018 = [
{"sample_name":"QCD\_bEnriched\_HT\_2018","sample":"QCD\_bEnriched\_HT\_2018\_100To200","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_bEnriched_HT_UL2018"]["QCD_bEnriched_HT_UL2018_100To200"]},
{"sample_name":"QCD\_bEnriched\_HT\_2018","sample":"QCD\_bEnriched\_HT\_2018\_200To300","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_bEnriched_HT_UL2018"]["QCD_bEnriched_HT_UL2018_200To300"]},
{"sample_name":"QCD\_bEnriched\_HT\_2018","sample":"QCD\_bEnriched\_HT\_2018\_300To500","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_bEnriched_HT_UL2018"]["QCD_bEnriched_HT_UL2018_300To500"]},
{"sample_name":"QCD\_bEnriched\_HT\_2018","sample":"QCD\_bEnriched\_HT\_2018\_500To700","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_bEnriched_HT_UL2018"]["QCD_bEnriched_HT_UL2018_500To700"]},
{"sample_name":"QCD\_bEnriched\_HT\_2018","sample":"QCD\_bEnriched\_HT\_2018\_700To1000","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_bEnriched_HT_UL2018"]["QCD_bEnriched_HT_UL2018_700To1000"]},
{"sample_name":"QCD\_bEnriched\_HT\_2018","sample":"QCD\_bEnriched\_HT\_2018\_1000To1500","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_bEnriched_HT_UL2018"]["QCD_bEnriched_HT_UL2018_1000To1500"]},
{"sample_name":"QCD\_bEnriched\_HT\_2018","sample":"QCD\_bEnriched\_HT\_2018\_1500To2000","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_bEnriched_HT_UL2018"]["QCD_bEnriched_HT_UL2018_1500To2000"]},
{"sample_name":"QCD\_bEnriched\_HT\_2018","sample":"QCD\_bEnriched\_HT\_2018\_2000ToInf","lumi_weight":59.83,"chain":sample_dic[2018]["bkg"]["QCD_bEnriched_HT_UL2018"]["QCD_bEnriched_HT_UL2018_2000ToInf"]}
]
bkg_samples = [QCD_HT_2018]
#bkg_samples = [EGamma_UL_2018,GJets_DR_0p4_HT_2018,TGJets_2018,TTGJets_2018,WZG_2018,ZGToLLG_2018,WJetsToLNu_HT,DYJetsToLL_M_50_HT,QCD_HT_2018,QCD_bEnriched_HT_2018]

#pt_binning = [[225,300],[300,350],[350,400],[400,500],[500,700],[700,1000],[1000,2000]]
#ofile = file(path+'cut_flow_table_'+signal_samples[0]['sample_name'],'w')
ofile = file(path+'cut_flow_table_QCD_HT_2018_2','w')
doc_header = '\\documentclass{article}\\usepackage[english]{babel}\\usepackage{graphicx}\\usepackage[margin=0.5in]{geometry}\\begin{document}'
ofile.write(doc_header)
ofile.write("\n")
table_header = '\\begin{table}[ht]\\begin{center}\\resizebox{\\textwidth}{!}{\\begin{tabular}{c | c | c | c | c | c | c | c | c | c}'
ofile.write(table_header)
ofile.write("\n")
#binning = 'binning'+ '&'+ 'cuts'
#ofile.write(binning)
for lis in bkg_samples:
#for lis in Signal_samples:
    for dic in lis:
	line = '&'+dic['sample_name']
    ofile.write(line)
    ofile.write("\n")
line_end = '\\\ \\hline'
ofile.write(line_end)
ofile.write("\n")

cutstring_list = [
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200","label":"presel"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodGenPhoton==0","label":"presel+ngoodGenPhoton=0"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodGenPhoton==1","label":"presel+ngoodGenPhoton=1"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet>0","label":"goodbJet$>$0"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet>0&&ngoodGenPhoton==0","label":"goodbJet$>$0+ngoodGenPhoton=0"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet>0&&ngoodGenPhoton==1","label":"goodbJet$>$0+ngoodGenPhoton=1"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==0","label":"0b"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==0&&ngoodGenPhoton==0","label":"0b+ngoodGenPhoton=0"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==0&&ngoodGenPhoton==1","label":"0b+ngoodGenPhoton=1"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==1","label":"1b"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==1&&ngoodGenPhoton==0","label":"1b+ngoodGenPhoton=0"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==1&&ngoodGenPhoton==1","label":"1b+ngoodGenPhoton=1"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==2","label":"2b"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==2&&ngoodGenPhoton==0","label":"2b+ngoodGenPhoton=0"},
{"cutstring":"ngoodPhoton==1&&(goodPhoton_pt>=225)&&goodJet_pt[0]>=225&&HLT_Photon200&&ngoodbJet==2&&ngoodGenPhoton==1","label":"2b+ngoodGenPhoton=1"}
]

for cuts in cutstring_list:
  #print cut['label']
  #print cut['cut']
  currentCUT = cuts['cutstring']
  print("#1",currentCUT)
  cut_line = '&'+cuts['label']
  ofile.write(cut_line)
  ofile.write("\n")
  gtot_yields = 0
  gtot_err = 0
#    for sample in signal_samples:
  for lis in bkg_samples:
    #print lis
    for dic in lis:
      ch = ROOT.TChain("Events")
      ch.Add(dic['chain']['dir']+'/*.root')
      tot_yields = 0
      
      #dic["weight"] = "(1)"
      lumi_weight = dic["chain"]['xsec']*1000*dic["lumi_weight"]*(1/float(dic["chain"]["nevents"]))
      #lumi_weight = float(59.83/100)
      dic["weight"] = str(lumi_weight)+"*(weight*puweight*PhotonSF)"
      #dic["weight"] = dic["chain"]['xsec']*1000*dic["lumi_weight"]*(1/float(dic["chain"]["nevents"]))
      #dic["weight"] = dic["chain"]['xsec']
      nEntry = ch.GetEntries()
      print("#2",nEntry)
      y_remain = getYieldFromChain(ch,cutString = currentCUT,weight = str(dic["weight"]), returnError = True)
      print("#3", y_remain[0])
      gtot_yields += y_remain[0]
      gtot_err += y_remain[1]*y_remain[1]
      tot_yields = y_remain
      line_yield = '&' + str(format((tot_yields[0]),'.1f'))+'$\pm$'+str(format((tot_yields[1]),'.1f'))
      #line_err = '&' + str(format((tot_yields[1]["err"]),'.1f'))
    #ofile.write(line_yield)
    #ofile.write(line_err)
    errors = sqrt(gtot_err)
    #print("#8",errors)
    #print("#6","TOTAL:", gtot_yields)
    line_tot_yield = '&'+str(format((gtot_yields),'.1f'))+'$\pm$'+str(format((errors),'.1f'))
    ofile.write(line_tot_yield)
    #ofile.write('\\\\')
  #ofile.write('\n')
  ofile.write('\\\\')
ofile.write('\\hline')
ofile.write('\n')
table_end = '\end{tabular}}\end{center}\caption{CutFlow with weight}\label{tab:CutFlow}\end{table}'
ofile.write(table_end)
ofile.write("\n")
doc_end = '\\end{document}'
ofile.write(doc_end)
ofile.close()
print("Written", ofile.name)
