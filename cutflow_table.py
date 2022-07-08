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
samples_2016PreVFP = [
{"sample_name":"G1Jet\_2016\_preVFP","sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_150To250","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_150To250_2016"]},
{"sample_name":"G1Jet\_2016\_preVFP","sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_250To400","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_250To400_2016"]},
{"sample_name":"G1Jet\_2016\_preVFP","sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_400To675","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_400To675_2016"]},
{"sample_name":"G1Jet\_2016\_preVFP","sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_675ToInf","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_675ToInf_2016"]},
]
samples_2016PostVFP = [
{"sample_name":"G1Jet\_2016\_postVFP","sample":"G1Jet\_LHEGpt\_150To250\_2016","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 16.81, "btagWP":0.6502,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_150To250_2016"]},\
{"sample_name":"G1Jet\_2016\_postVFP","sample":"G1Jet\_LHEGpt\_250To400\_2016","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 16.81, "btagWP":0.6502,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2016"]},\
{"sample_name":"G1Jet\_2016\_postVFP","sample":"G1Jet\_LHEGpt\_400To675\_2016","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 16.81, "btagWP":0.6502,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2016"]},\
{"sample_name":"G1Jet\_2016\_postVFP","sample":"G1Jet\_LHEGpt\_675ToInf\_2016","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 16.81, "btagWP":0.6502,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_675ToInf_2016"]},\
]

samples_2017 = [
{"sample_name":"G1Jet\_2017","sample":"G1Jet\_LHEGpt\_150To250\_2017","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_150To250_2017"]},\
{"sample_name":"G1Jet\_2017","sample":"G1Jet\_LHEGpt\_250To400\_2017","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"G1Jet\_2017","sample":"G1Jet\_LHEGpt\_400To675\_2017","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"G1Jet\_2017","sample":"G1Jet\_LHEGpt\_675ToInf\_2017","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_675ToInf_2017"]},\
]

QCD_HT_2017 = [
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_50To100","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_50To100"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_100To200"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_200To300","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_200To300"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_300To500","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_300To500"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_500To700","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_500To700"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_700To1000","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_700To1000"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_1000To1500","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_1000To1500"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_1500To2000","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_1500To2000"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_2000ToInf","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_2000ToInf"]},\
]

QCD_bEnriched_HT_2017 = [
{"sample_name":"QCD\_bEnriched\_HT","sample":"QCD\_bEnriched\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_bEnriched_HT_UL2017"]["QCD_bEnriched_HT_UL2017_100To200"]},\
{"sample_name":"QCD\_bEnriched\_HT","sample":"QCD\_bEnriched\_HT\_UL2017\_200To300","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_bEnriched_HT_UL2017"]["QCD_bEnriched_HT_UL2017_200To300"]},\
{"sample_name":"QCD\_bEnriched\_HT","sample":"QCD\_bEnriched\_HT\_UL2017\_300To500","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_bEnriched_HT_UL2017"]["QCD_bEnriched_HT_UL2017_300To500"]},\
{"sample_name":"QCD\_bEnriched\_HT","sample":"QCD\_bEnriched\_HT\_UL2017\_500To700","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_bEnriched_HT_UL2017"]["QCD_bEnriched_HT_UL2017_500To700"]},\
{"sample_name":"QCD\_bEnriched\_HT","sample":"QCD\_bEnriched\_HT\_UL2017\_700To1000","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_bEnriched_HT_UL2017"]["QCD_bEnriched_HT_UL2017_700To1000"]},\
{"sample_name":"QCD\_bEnriched\_HT","sample":"QCD\_bEnriched\_HT\_UL2017\_1000To1500","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_bEnriched_HT_UL2017"]["QCD_bEnriched_HT_UL2017_1000To1500"]},\
{"sample_name":"QCD\_bEnriched\_HT","sample":"QCD\_bEnriched\_HT\_UL2017\_1500To2000","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_bEnriched_HT_UL2017"]["QCD_bEnriched_HT_UL2017_1500To2000"]},\
{"sample_name":"QCD\_bEnriched\_HT","sample":"QCD\_bEnriched\_HT\_UL2017\_2000ToInf","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_bEnriched_HT_UL2017"]["QCD_bEnriched_HT_UL2017_2000ToInf"]},\
]
TGJets_17 = [
{"sample_name":"TGJets\_UL\_2017","sample":"TGJets\_UL\_2017","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["TGJets_UL_2017"]}
]
TTGJets_17 = [
{"sample_name":"TTGJets\_UL\_2017","sample":"TTGJets\_UL\_2017","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["TTGJets_UL_2017"]}
]
WZG_17 = [
{"sample_name":"TGJets\_UL\_2017","sample":"TGJets\_UL\_2017","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["WZG_UL_2017"]}
]
ZGToLLG_17 = [
{"sample_name":"TGJets\_UL\_2017","sample":"TGJets\_UL\_2017","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["ZGToLLG_UL_2017"]}
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_100To200"]},\
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_100To200"]},\
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_100To200"]},\
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_100To200"]},\
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_100To200"]},\
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_100To200"]},\
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"QCD\_HT","sample":"QCD\_HT\_UL2017\_100To200","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["bkg"]["QCD_HT_UL2017"]["QCD_HT_UL2017_100To200"]},\
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"TTGJets","sample":"TTGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_675ToInf_2017"]},\
{"sample_name":"WZG","sample":"WZG","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
]
samples_2018 = [
{"sample_name":"QCD\_bEnriched","sample":"QCD_bEnriched","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2017"]},\
{"sample_name":"TGJets","sample":"TGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"TTGJets","sample":"TTGJets","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_675ToInf_2017"]},\
{"sample_name":"WZG","sample":"WZG","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2017"]},\
{"sample_name":"ZGToLLG","sample":"ZZGToLLG","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 41.48, "btagWP":0.7476,"chain":sample_dic[2017]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_675ToInf_2017"]},\
]
samples_2018 = [
{"sample_name":"G1Jet\_2018","sample":"G1Jet\_LHEGpt\_150To250\_2018","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 59.83, "btagWP":0.7100,"chain":sample_dic[2018]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_150To250_2018"]},\
{"sample_name":"G1Jet\_2018","sample":"G1Jet\_LHEGpt\_250To400\_2018","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 59.83, "btagWP":0.7100,"chain":sample_dic[2018]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_250To400_2018"]},\
{"sample_name":"G1Jet\_2018","sample":"G1Jet\_LHEGpt\_400To675\_2018","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 59.83, "btagWP":0.7100,"chain":sample_dic[2018]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_400To675_2018"]},\
{"sample_name":"G1Jet\_2018","sample":"G1Jet\_LHEGpt\_675ToInf\_2018","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter)","lumi_weight": 59.83, "btagWP":0.7100,"chain":sample_dic[2018]["signal"]["G1Jet_LHEGpt"]["G1Jet_LHEGpt_675ToInf_2018"]},\
]



Signal_samples = [samples_2016PreVFP,samples_2016PostVFP,samples_2017,samples_2018]
#Signal_samples = [samples_2016PreVFP,samples_2016PostVFP]
#bkg_samples = [QCD_HT_2017, QCD_bEnriched_HT_2017]
bkg_samples = [TGJets_17,TTGJets_17,WZG_17,ZGToLLG_17]
#signal_samples = [ 
#{"sample_name":"G1Jet_2016_preVFP","sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_150To250","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter&&HLT_Photon175)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_150To250_2016"]},
#{"sample_name":"G1Jet_2016_preVFP","sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_250To400","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter&&HLT_Photon175)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_250To400_2016"]},
#{"sample_name":"G1Jet_2016_preVFP","sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_400To675","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter&&HLT_Photon175)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_400To675_2016"]},
#{"sample_name":"G1Jet_2016_preVFP","sample":"G1Jet\_LHEGPt\_2016\_PreVFP\_675ToInf","met_filters": "((Flag_goodVertices)&&(Flag_globalSuperTightHalo2016Filter)&&(Flag_HBHENoiseFilter)&&(Flag_HBHENoiseIsoFilter)&&(Flag_EcalDeadCellTriggerPrimitiveFilter)&&(Flag_BadPFMuonFilter)&&Flag_eeBadScFilter&&HLT_Photon175)","lumi_weight": 19.52, "btagWP":0.6377,"chain":sample_dic[2016]["signal"]["G1Jet_LHEGPt_PreVFP"]["G1Jet_LHEGPt_PreVFP_675ToInf_2016"]},
#]

pt_binning = [[225,300],[300,350],[350,400],[400,500],[500,700],[700,1000],[1000,2000]]
#ofile = file(path+'cut_flow_table_'+signal_samples[0]['sample_name'],'w')
ofile = file(path+'cut_flow_table_bkg','w')
doc_header = '\\documentclass{article}\\usepackage[english]{babel}\\usepackage{graphicx}\\usepackage[margin=0.5in]{geometry}\\begin{document}'
ofile.write(doc_header)
ofile.write("\n")
table_header = '\\begin{table}[ht]\\begin{center}\\resizebox{\\textwidth}{!}{\\begin{tabular}{c | c | c | c | c | c | c | c | c | c}'
ofile.write(table_header)
ofile.write("\n")
binning = 'binning'+ '&'+ 'cuts'
ofile.write(binning)
for lis in bkg_samples:
#for lis in Signal_samples:
    for dic in lis:
	line = '&'+dic['sample_name']
    ofile.write(line)
    ofile.write("\n")
line_end = '\\\ \\hline'
ofile.write(line_end)
ofile.write("\n")
for bin1 in pt_binning:
  ptcut = "Photon_pt>="+str(bin1[0])+"&&"+"Photon_pt<"+str(bin1[1])
  ofile.write(str(bin1))
  ngood_vtx_cut = "(PV_npvsGood>=1)"
  met_filters = dic["met_filters"]
  single_photon_cut = "Sum$(Photon_cutBased>=3&&Photon_pt>=40&&abs(Photon_eta)<1.4)>=1"
  njet_tight = "Sum$(Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=6&&Jet_puId>=7)>=1"
  ntightDeepBJets = "Sum$(Jet_pt>40&&abs(Jet_eta)<2.4&&Jet_jetId>=6&&Jet_puId>=7 && Jet_btagDeepFlavB>="+str(dic['btagWP'])+")"
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
    print("#1",currentCUT)
    cut_line = '&'+cut['label']
    ofile.write(cut_line)
    ofile.write("\n")
    gtot_yields = 0
    gtot_err = 0
#    for sample in signal_samples:
    for lis in bkg_samples:
      for dic in lis:
        ch = ROOT.TChain("Events")
        ch.Add(dic['chain']['dir']+'/*.root')
        tot_yields = 0
        dic["weight"] = dic["chain"]['xsec']*1000*dic["lumi_weight"]*(1/float(dic["chain"]["nevents"]))
        nEntry = ch.GetEntries()
        y_remain = getYieldFromChain(ch,cutString = currentCUT,weight = str(dic["weight"]), returnError = True)
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
table_end = '\end{tabular}}\end{center}\caption{CutFlow}\label{tab:CutFlow}\end{table}'
ofile.write(table_end)
ofile.write("\n")
doc_end = '\\end{document}'
ofile.write(doc_end)
ofile.close()
print("Written", ofile.name)
