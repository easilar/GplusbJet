# Sample dictionary for a GammaplusbJets Run II Analysis

import pickle

path_MC_UL = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/MC/"
path_MC_UL_MTN = "/eos/user/m/myalvac/GPlusBJets/MC/"
path_data_UL_17 = "/eos/user/m/myalvac/GPlusBJets/data/2017/SinglePhoton_UL/"
path_data_UL_18 = "/eos/user/m/myalvac/GPlusBJets/data/2018/EGamma_UL/"
path_data_UL = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton_UL/"
path_data_UL_PreVFP = "/eos/user/m/myalvac/GPlusBJets/data/2016/SinglePhoton_UL/"
#path_MC = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/MC/"
tag = "High_PT_Tight/"
subdir = "hadd/"
subdir_UNC = "hadd_UNC/"

G1Jet_LHEGPt_150To250_2017 = path_MC_UL+"/2017/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_250To400_2017 = path_MC_UL+"/2017/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_400To675_2017 = path_MC_UL+"/2017/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_675ToInf_2017 = path_MC_UL+"/2017/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir

GJets_DR_0p4_HT_100To200_2017 = path_MC_UL_MTN+"/2017/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_200To400_2017 = path_MC_UL_MTN+"/2017/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_400To600_2017 = path_MC_UL_MTN+"/2017/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_600ToInf_2017 = path_MC_UL_MTN+"/2017/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir

G1Jet_LHEGPt_150To250_2018 = path_MC_UL+"/2018/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_250To400_2018 = path_MC_UL+"/2018/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_400To675_2018 = path_MC_UL+"/2018/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_675ToInf_2018 = path_MC_UL+"/2018/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir

GJets_DR_0p4_HT_100To200_2018 = path_MC_UL_MTN+"/2018/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
GJets_DR_0p4_HT_200To400_2018 = path_MC_UL_MTN+"/2018/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
GJets_DR_0p4_HT_400To600_2018 = path_MC_UL_MTN+"/2018/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
GJets_DR_0p4_HT_600ToInf_2018 = path_MC_UL_MTN+"/2018/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC

QCD_HT_50to100_UL_2017    = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_100to200_UL_2017   = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_200to300_UL_2017   = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_300to500_UL_2017   = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_500to700_UL_2017   = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_700to1000_UL_2017  = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_1000to1500_UL_2017 = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_1500to2000_UL_2017 = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_2000toInf_UL_2017  = path_MC_UL+"/2017/"+"QCD_HT_UL2017/"+tag+"/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir

QCD_bEnriched_HT_100to200_UL_2017   = path_MC_UL_MTN+"/2017/"+"QCD_bEnriched_HT_UL2017/"+tag+"QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_200to300_UL_2017   = path_MC_UL_MTN+"/2017/"+"QCD_bEnriched_HT_UL2017/"+tag+"QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_300to500_UL_2017   = path_MC_UL_MTN+"/2017/"+"QCD_bEnriched_HT_UL2017/"+tag+"QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_500to700_UL_2017   = path_MC_UL_MTN+"/2017/"+"QCD_bEnriched_HT_UL2017/"+tag+"QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_700to1000_UL_2017  = path_MC_UL_MTN+"/2017/"+"QCD_bEnriched_HT_UL2017/"+tag+"QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_1000to1500_UL_2017 = path_MC_UL_MTN+"/2017/"+"QCD_bEnriched_HT_UL2017/"+tag+"QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_1500to2000_UL_2017 = path_MC_UL_MTN+"/2017/"+"QCD_bEnriched_HT_UL2017/"+tag+"QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_2000toInf_UL_2017  = path_MC_UL_MTN+"/2017/"+"QCD_bEnriched_HT_UL2017/"+tag+"QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/"+subdir

TGJets_UL_2017  = path_MC_UL_MTN+"/2017/"+"TGJets_UL_2017/"+tag+"TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/"+subdir
TTGJets_UL_2017 = path_MC_UL_MTN+"/2017/"+"TTGJets_UL_2017/"+tag+"TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+subdir
WZG_UL_2017     = path_MC_UL_MTN+"/2017/"+"WZG_UL_2017/"+tag+"WZG_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
ZGToLLG_UL_2017 = path_MC_UL_MTN+"/2017/"+"ZGToLLG_UL_2017/"+tag+"ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/"+subdir


QCD_HT_50to100_UL_2018    = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_HT_100to200_UL_2018   = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_HT_200to300_UL_2018   = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_HT_300to500_UL_2018   = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_HT_500to700_UL_2018   = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_HT_700to1000_UL_2018  = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_HT_1000to1500_UL_2018 = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_HT_1500to2000_UL_2018 = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_HT_2000toInf_UL_2018  = path_MC_UL_MTN+"/2018/"+"QCD_HT_UL2018/"+tag+"/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir_UNC

QCD_bEnriched_HT_100to200_UL_2018   = path_MC_UL_MTN+"/2018/"+"QCD_bEnriched_HT_UL2018/"+tag+"QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_bEnriched_HT_200to300_UL_2018   = path_MC_UL_MTN+"/2018/"+"QCD_bEnriched_HT_UL2018/"+tag+"QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_bEnriched_HT_300to500_UL_2018   = path_MC_UL_MTN+"/2018/"+"QCD_bEnriched_HT_UL2018/"+tag+"QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_bEnriched_HT_500to700_UL_2018   = path_MC_UL_MTN+"/2018/"+"QCD_bEnriched_HT_UL2018/"+tag+"QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_bEnriched_HT_700to1000_UL_2018  = path_MC_UL_MTN+"/2018/"+"QCD_bEnriched_HT_UL2018/"+tag+"QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_bEnriched_HT_1000to1500_UL_2018 = path_MC_UL_MTN+"/2018/"+"QCD_bEnriched_HT_UL2018/"+tag+"QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_bEnriched_HT_1500to2000_UL_2018 = path_MC_UL_MTN+"/2018/"+"QCD_bEnriched_HT_UL2018/"+tag+"QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/"+subdir_UNC
QCD_bEnriched_HT_2000toInf_UL_2018  = path_MC_UL_MTN+"/2018/"+"QCD_bEnriched_HT_UL2018/"+tag+"QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/"+subdir_UNC

TGJets_UL_2018  = path_MC_UL_MTN+"/2018/"+"TGJets_UL_2018/"+tag+"TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/"+subdir_UNC
TTGJets_UL_2018 = path_MC_UL_MTN+"/2018/"+"TTGJets_UL_2018/"+tag+"TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+subdir_UNC
WZG_UL_2018     = path_MC_UL_MTN+"/2018/"+"WZG_UL_2018/"+tag+"WZG_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir_UNC
ZGToLLG_UL_2018 = path_MC_UL_MTN+"/2018/"+"ZGToLLG_UL_2018/"+tag+"ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/"+subdir_UNC

WJetsToLNu_HT_100to200_UL_2018   = path_MC_UL_MTN+"/2018/"+"WJetsToLNu_HT/"+tag+"WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
WJetsToLNu_HT_200to400_UL_2018   = path_MC_UL_MTN+"/2018/"+"WJetsToLNu_HT/"+tag+"WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
WJetsToLNu_HT_400to600_UL_2018   = path_MC_UL_MTN+"/2018/"+"WJetsToLNu_HT/"+tag+"WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
WJetsToLNu_HT_600to800_UL_2018   = path_MC_UL_MTN+"/2018/"+"WJetsToLNu_HT/"+tag+"WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
WJetsToLNu_HT_800to1200_UL_2018  = path_MC_UL_MTN+"/2018/"+"WJetsToLNu_HT/"+tag+"WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
WJetsToLNu_HT_1200to2500_UL_2018 = path_MC_UL_MTN+"/2018/"+"WJetsToLNu_HT/"+tag+"WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC
WJetsToLNu_HT_2500toInf_UL_2018  = path_MC_UL_MTN+"/2018/"+"WJetsToLNu_HT/"+tag+"WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir_UNC

DYJetsToLL_M_50_HT_100to200_UL_2018   = path_MC_UL_MTN+"/2018/"+"DYJetsToLL_M_50_HT/"+tag+"DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/"+subdir_UNC
DYJetsToLL_M_50_HT_200to400_UL_2018   = path_MC_UL_MTN+"/2018/"+"DYJetsToLL_M_50_HT/"+tag+"DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/"+subdir_UNC
DYJetsToLL_M_50_HT_400to600_UL_2018   = path_MC_UL_MTN+"/2018/"+"DYJetsToLL_M_50_HT/"+tag+"DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/"+subdir_UNC
DYJetsToLL_M_50_HT_600to800_UL_2018   = path_MC_UL_MTN+"/2018/"+"DYJetsToLL_M_50_HT/"+tag+"DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/"+subdir_UNC
DYJetsToLL_M_50_HT_800to1200_UL_2018  = path_MC_UL_MTN+"/2018/"+"DYJetsToLL_M_50_HT/"+tag+"DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/"+subdir_UNC
DYJetsToLL_M_50_HT_1200to2500_UL_2018 = path_MC_UL_MTN+"/2018/"+"DYJetsToLL_M_50_HT/"+tag+"DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/"+subdir_UNC
DYJetsToLL_M_50_HT_2500toInf_UL_2018  = path_MC_UL_MTN+"/2018/"+"DYJetsToLL_M_50_HT/"+tag+"DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/"+subdir_UNC

G1Jet_LHEGPt_150To250_2016 = path_MC_UL+"/2016/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_250To400_2016 = path_MC_UL+"/2016/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_400To675_2016 = path_MC_UL+"/2016/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_675ToInf_2016 = path_MC_UL+"/2016/"+"G1Jet_LHEGpt/"+tag+"/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir

GJets_DR_0p4_HT_100To200_2016 = path_MC_UL_MTN+"/2016/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_200To400_2016 = path_MC_UL_MTN+"/2016/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_400To600_2016 = path_MC_UL_MTN+"/2016/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_600ToInf_2016 = path_MC_UL_MTN+"/2016/"+"GJets_DR_0p4_HT/"+tag+"GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir

G1Jet_LHEGPt_150To250_2016_PreVFP = path_MC_UL_MTN+"/2016/"+"G1Jet_LHEGPt_PreVFP/"+tag+"/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_250To400_2016_PreVFP = path_MC_UL_MTN+"/2016/"+"G1Jet_LHEGPt_PreVFP/"+tag+"/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_400To675_2016_PreVFP = path_MC_UL_MTN+"/2016/"+"G1Jet_LHEGPt_PreVFP/"+tag+"/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
G1Jet_LHEGPt_675ToInf_2016_PreVFP = path_MC_UL_MTN+"/2016/"+"G1Jet_LHEGPt_PreVFP/"+tag+"/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir

GJets_DR_0p4_HT_PreVFP_100To200_2016 = path_MC_UL_MTN+"/2016/"+"GJets_DR_0p4_HT_PreVFP/"+tag+"GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_PreVFP_200To400_2016 = path_MC_UL_MTN+"/2016/"+"GJets_DR_0p4_HT_PreVFP/"+tag+"GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_PreVFP_400To600_2016 = path_MC_UL_MTN+"/2016/"+"GJets_DR_0p4_HT_PreVFP/"+tag+"GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir
GJets_DR_0p4_HT_PreVFP_600ToInf_2016 = path_MC_UL_MTN+"/2016/"+"GJets_DR_0p4_HT_PreVFP/"+tag+"GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+subdir

QCD_HT_50to100_UL_2016    = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_100to200_UL_2016   = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_200to300_UL_2016   = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_300to500_UL_2016   = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_500to700_UL_2016   = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_700to1000_UL_2016  = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_1000to1500_UL_2016 = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_1500to2000_UL_2016 = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_2000toInf_UL_2016  = path_MC_UL+"QCD_HT_UL2016/"+tag+"/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir

QCD_HT_50to100_UL_2016_PreVFP    = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_100to200_UL_2016_PreVFP   = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_200to300_UL_2016_PreVFP   = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_300to500_UL_2016_PreVFP   = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_500to700_UL_2016_PreVFP   = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_700to1000_UL_2016_PreVFP  = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_1000to1500_UL_2016_PreVFP = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_1500to2000_UL_2016_PreVFP = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir
QCD_HT_2000toInf_UL_2016_PreVFP  = path_MC_UL_MTN+"/2016/"+"QCD_HT_UL2016_PreVFP/"+tag+"/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"+subdir

QCD_bEnriched_HT_100to200_UL_2016   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_200to300_UL_2016   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_300to500_UL_2016   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_500to700_UL_2016   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_700to1000_UL_2016  = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_1000to1500_UL_2016 = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_1500to2000_UL_2016 = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_2000toInf_UL_2016  = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_100to200_UL_2016   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016/"+tag+"/QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/"+subdir

QCD_bEnriched_HT_100to200_UL_2016_PreVFP   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016_PreVFP/"+tag+"/QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_200to300_UL_2016_PreVFP   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016_PreVFP/"+tag+"/QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_300to500_UL_2016_PreVFP   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016_PreVFP/"+tag+"/QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_500to700_UL_2016_PreVFP   = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016_PreVFP/"+tag+"/QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_700to1000_UL_2016_PreVFP  = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016_PreVFP/"+tag+"/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_1000to1500_UL_2016_PreVFP = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016_PreVFP/"+tag+"/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_1500to2000_UL_2016_PreVFP = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016_PreVFP/"+tag+"/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/"+subdir
QCD_bEnriched_HT_2000toInf_UL_2016_PreVFP  = path_MC_UL_MTN+"/2016/"+"QCD_bEnriched_HT_UL2016_PreVFP/"+tag+"/QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/"+subdir

TGJets_UL_2016  = path_MC_UL_MTN+"/2017/"+"TGJets_UL_2017/"+tag+"TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/"+subdir
TTGJets_UL_2016 = path_MC_UL_MTN+"/2017/"+"TTGJets_UL_2017/"+tag+"TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+subdir
WZG_UL_2016     = path_MC_UL_MTN+"/2017/"+"WZG_UL_2017/"+tag+"WZG_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
ZGToLLG_UL_2016 = path_MC_UL_MTN+"/2017/"+"ZGToLLG_UL_2017/"+tag+"ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/"+subdir

TGJets_UL_2016_PreVFP  = path_MC_UL_MTN+"/2017/"+"TGJets_UL_2017/"+tag+"TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/"+subdir
TTGJets_UL_2016_PreVFP = path_MC_UL_MTN+"/2017/"+"TTGJets_UL_2017/"+tag+"TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+subdir
WZG_UL_2016_PreVFP     = path_MC_UL_MTN+"/2017/"+"WZG_UL_2017/"+tag+"WZG_TuneCP5_13TeV-amcatnlo-pythia8/"+subdir
ZGToLLG_UL_2016_PreVFP = path_MC_UL_MTN+"/2017/"+"ZGToLLG_UL_2017/"+tag+"ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/"+subdir

###xsect dictionary: valuses are taken from https://cms-gen-dev.cern.ch/xsdb/ Metin!!!!###
###Das paths are Added####
Samples = {2016: \
	{"signal":\
			{
			"G1Jet_LHEGpt":\
					{
					"G1Jet_LHEGpt_150To250_2016":{"dir":G1Jet_LHEGPt_150To250_2016,"nevents":5862211,"xsec":2.262e+2,"xsec_unc":6.433e-1,"equivalent_lumi":1.882,"fraction_negative_weight":0.1738, "das_path":"/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
					"G1Jet_LHEGpt_250To400_2016":{"dir":G1Jet_LHEGPt_250To400_2016,"nevents":3004010,"xsec":2.699e+1,"xsec_unc":0.08345,"equivalent_lumi":17.17,"fraction_negative_weight":0.1697, "das_path":"/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
					"G1Jet_LHEGpt_400To675_2016":{"dir":G1Jet_LHEGPt_400To675_2016,"nevents":1000053,"xsec":3.395,"xsec_unc":0.007753,"equivalent_lumi":133.2,"fraction_negative_weight":0.1638, "das_path":"/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
					"G1Jet_LHEGpt_675ToInf_2016":{"dir":G1Jet_LHEGPt_675ToInf_2016,"nevents":249174,"xsec":2.478e-1,"xsec_unc":0.0005027,"equivalent_lumi":1883.0,"fraction_negative_weight":0.1584, "das_path":"/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
					},\
			"G1Jet_LHEGPt_PreVFP":\
					{
					"G1Jet_LHEGPt_PreVFP_150To250_2016":{"dir":G1Jet_LHEGPt_150To250_2016_PreVFP,"nevents":5861243,"xsec":2.262e+2,"xsec_unc":6.433e-1,"equivalent_lumi":1.882,"fraction_negative_weight":0.1738, "das_path":"/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
					"G1Jet_LHEGPt_PreVFP_250To400_2016":{"dir":G1Jet_LHEGPt_250To400_2016_PreVFP,"nevents":2918574,"xsec":2.699e+1,"xsec_unc":0.08345,"equivalent_lumi":17.17,"fraction_negative_weight":0.1697, "das_path":"/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
					"G1Jet_LHEGPt_PreVFP_400To675_2016":{"dir":G1Jet_LHEGPt_400To675_2016_PreVFP,"nevents":999246,"xsec":3.395,"xsec_unc":0.007753,"equivalent_lumi":133.2,"fraction_negative_weight":0.1638, "das_path":"/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
					"G1Jet_LHEGPt_PreVFP_675ToInf_2016":{"dir":G1Jet_LHEGPt_675ToInf_2016_PreVFP,"nevents":249100,"xsec":2.478e-1,"xsec_unc":0.0005027,"equivalent_lumi":1883.0,"fraction_negative_weight":0.1584, "das_path":"/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
					},\
  			   "GJets_DR_0p4_HT":\
                                        {
                                        "GJets_DR_0p4_HT_100To200_2016":{"dir":GJets_DR_0p4_HT_100To200_2016,"nevents":4421327,"xsec":5034.0,"xsec_unc":14.69,"equivalent_lumi":0.1986,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"},\
                                        "GJets_DR_0p4_HT_200To400_2016":{"dir":GJets_DR_0p4_HT_200To400_2016,"nevents":13744262,"xsec":1129.0,"xsec_unc":3.338,"equivalent_lumi":0.8859,"fraction_negative_weight":0.0,"das_path":"/GJets_DR_0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"},\
                                        "GJets_DR_0p4_HT_400To600_2016":{"dir":GJets_DR_0p4_HT_400To600_2016,"nevents":4124520,"xsec":126.2,"xsec_unc":0.03779,"equivalent_lumi":7.921,"fraction_negative_weight":0.0,"das_path":"/GJets_DR_0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"},\
                                        "GJets_DR_0p4_HT_600ToInf_2016":{"dir":GJets_DR_0p4_HT_600ToInf_2016,"nevents":3427780,"xsec":41.31,"xsec_unc":0.1242,"equivalent_lumi":24.21,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"},\
                                        },\
                            "GJets_DR_0p4_HT_PreVFP":\
                                        {
                                        "GJets_DR_0p4_HT_PreVFP_100To200_2016":{"dir":GJets_DR_0p4_HT_PreVFP_100To200_2016,"nevents":5069975,"xsec":5034.0,"xsec_unc":14.69,"equivalent_lumi":0.1986,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"},\
                                        "GJets_DR_0p4_HT_PreVFP_200To400_2016":{"dir":GJets_DR_0p4_HT_PreVFP_200To400_2016,"nevents":14620395,"xsec":1129.0,"xsec_unc":3.338,"equivalent_lumi":0.8859,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"},\
                                        "GJets_DR_0p4_HT_PreVFP_400To600_2016":{"dir":GJets_DR_0p4_HT_PreVFP_400To600_2016,"nevents":4116285,"xsec":126.2,"xsec_unc":0.03779,"equivalent_lumi":7.921,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"},\
                                        "GJets_DR_0p4_HT_PreVFP_600ToInf_2016":{"dir":GJets_DR_0p4_HT_PreVFP_600ToInf_2016,"nevents":3936783,"xsec":41.31,"xsec_unc":0.1242,"equivalent_lumi":24.21,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"},\
                                        },\
    },\
	#Closes Signal
  "bkg":{\
     "QCD_HT_UL2016":{ \
      "QCD_HT_UL2016_50To100":{"dir":QCD_HT_50to100_UL_2016,"nevents":11197186,"xsec":1.860e+8,"xsec_unc":4.897e+4,"equivalent_lumi":5.377e-06,"fraction_negative_weight":0.0, "das_path":"/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_100To200":{"dir":QCD_HT_100to200_UL_2016,"nevents":23717410,"xsec":2.365e+7,"xsec_unc":4.467e+3,"equivalent_lumi":4.229e-05,"fraction_negative_weight":0.0, "das_path":"/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_200To300":{"dir":QCD_HT_200to300_UL_2016,"nevents":17569141,"xsec":1.553e+6,"xsec_unc":3.499e+2,"equivalent_lumi":6.440e-04  ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_300To500":{"dir":QCD_HT_300to500_UL_2016,"nevents":16747056,"xsec":3.245e+5,"xsec_unc":75.53,"equivalent_lumi":3.082e-3,"fraction_negative_weight":0.0, "das_path":"/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_500To700":{"dir":QCD_HT_500to700_UL_2016,"nevents":14212819,"xsec":3.028e+4,"xsec_unc":7.439,"equivalent_lumi":0.03303 ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_700To1000":{"dir":QCD_HT_700to1000_UL_2016,"nevents":13750537,"xsec":6.437e+3,"xsec_unc":1.658,"equivalent_lumi":0.1554,"fraction_negative_weight":0.0, "das_path":"/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_1000To1500":{"dir":QCD_HT_1000to1500_UL_2016,"nevents":4365993,"xsec":1.122e+3,"xsec_unc":0.5173,"equivalent_lumi":0.8911  ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_1500To2000":{"dir":QCD_HT_1500to2000_UL_2016,"nevents":3003707,"xsec":1.083e+2,"xsec_unc":0.05823,"equivalent_lumi":9.230,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_2000ToInf":{"dir":QCD_HT_2000toInf_UL_2016,"nevents":1847781,"xsec":2.204e+1,"xsec_unc":0.01560,"equivalent_lumi":45.38,"fraction_negative_weight":0.0, "das_path":"/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      },
      "QCD_bEnriched_HT_UL2016":\
      { 
      "QCD_bEnriched_HT_UL2016_100To200":{"dir":QCD_bEnriched_HT_100to200_UL_2016,"nevents":19202473,"xsec":1127000.0,"xsec_unc":3241.0,"equivalent_lumi":0.0008871,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_200To300":{"dir":QCD_bEnriched_HT_200to300_UL_2016,"nevents":9196799,"xsec":80220.0,"xsec_unc":235.7,"equivalent_lumi":0.01247  ,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_300To500":{"dir":QCD_bEnriched_HT_300to500_UL_2016,"nevents":5612374,"xsec":16700.0,"xsec_unc":49.74,"equivalent_lumi":0.05988,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_500To700":{"dir":QCD_bEnriched_HT_500to700_UL_2016,"nevents":4616176,"xsec":1487.0,"xsec_unc":4.442,"equivalent_lumi":0.6699 ,"fraction_negative_weight":0.001047, "das_path":"/QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_700To1000":{"dir":QCD_bEnriched_HT_700to1000_UL_2016,"nevents":903293,"xsec":298.8,"xsec_unc":0.8983,"equivalent_lumi":3.347,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_1000To1500":{"dir":QCD_bEnriched_HT_1000to1500_UL_2016,"nevents":663922,"xsec":46.61,"xsec_unc":0.2002,"equivalent_lumi":21.2,"fraction_negative_weight":0.002946, "das_path":"/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_1500To2000":{"dir":QCD_bEnriched_HT_1500to2000_UL_2016,"nevents":698469,"xsec":4.017,"xsec_unc":0.01213,"equivalent_lumi":248.9,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_2000ToInf":{"dir":QCD_bEnriched_HT_2000toInf_UL_2016,"nevents":684942,"xsec":0.6967,"xsec_unc":0.002099,"equivalent_lumi":1435.0,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      },
     "QCD_HT_UL2016_PreVFP":\
      {
      "QCD_HT_UL2016_PreVFP_50To100":{"dir":QCD_HT_50to100_UL_2016_PreVFP,"nevents":12233035,"xsec":1.860e+8,"xsec_unc":4.897e+4,"equivalent_lumi":5.377e-06,"fraction_negative_weight":0.0, "das_path":"/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_PreVFP_100To200":{"dir":QCD_HT_100to200_UL_2016_PreVFP,"nevents":26312661,"xsec":2.365e+7,"xsec_unc":4.467e+3,"equivalent_lumi":4.229e-05,"fraction_negative_weight":0.0, "das_path":"/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_PreVFP_200To300":{"dir":QCD_HT_200to300_UL_2016_PreVFP,"nevents":16524587,"xsec":1.553e+6,"xsec_unc":3.499e+2,"equivalent_lumi":6.440e-04  ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_PreVFP_300To500":{"dir":QCD_HT_300to500_UL_2016_PreVFP,"nevents":15183920,"xsec":3.245e+5,"xsec_unc":75.53,"equivalent_lumi":3.082e-3,"fraction_negative_weight":0.0, "das_path":"/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_PreVFP_500To700":{"dir":QCD_HT_500to700_UL_2016_PreVFP,"nevents":15775001,"xsec":3.028e+4,"xsec_unc":7.439,"equivalent_lumi":0.03303 ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_PreVFP_700To1000":{"dir":QCD_HT_700to1000_UL_2016_PreVFP,"nevents":15808790,"xsec":6.437e+3,"xsec_unc":1.658,"equivalent_lumi":0.1554,"fraction_negative_weight":0.0, "das_path":"/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_PreVFP_1000To1500":{"dir":QCD_HT_1000to1500_UL_2016_PreVFP,"nevents":4773503,"xsec":1.122e+3,"xsec_unc":0.5173,"equivalent_lumi":0.8911  ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_PreVFP_1500To2000":{"dir":QCD_HT_1500to2000_UL_2016_PreVFP,"nevents":3503675,"xsec":1.083e+2,"xsec_unc":0.05823,"equivalent_lumi":9.230,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      "QCD_HT_UL2016_PreVFP_2000ToInf":{"dir":QCD_HT_2000toInf_UL_2016_PreVFP,"nevents":1629000,"xsec":2.204e+1,"xsec_unc":0.01560,"equivalent_lumi":45.38,"fraction_negative_weight":0.0, "das_path":"/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
      }, 
      "QCD_bEnriched_HT_UL2016_PreVFP":\
      {
      "QCD_bEnriched_HT_UL2016_PreVFP_100To200":{"dir":QCD_bEnriched_HT_100to200_UL_2016_PreVFP,"nevents":17657456,"xsec":1127000.0,"xsec_unc":3241.0,"equivalent_lumi":0.0008871,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_PreVFP_200To300":{"dir":QCD_bEnriched_HT_200to300_UL_2016_PreVFP,"nevents":8886507,"xsec":80220.0,"xsec_unc":235.7,"equivalent_lumi":0.01247  ,"fraction_negative_weight":0.0, "das_path":"//QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_PreVFP_300To500":{"dir":QCD_bEnriched_HT_300to500_UL_2016_PreVFP,"nevents":4978755,"xsec":16700.0,"xsec_unc":49.74,"equivalent_lumi":0.05988,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_PreVFP_500To700":{"dir":QCD_bEnriched_HT_500to700_UL_2016_PreVFP,"nevents":4433560,"xsec":1487.0,"xsec_unc":4.442,"equivalent_lumi":0.6699 ,"fraction_negative_weight":0.001047, "das_path":"/QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_PreVFP_700To1000":{"dir":QCD_bEnriched_HT_700to1000_UL_2016_PreVFP,"nevents":979344,"xsec":298.8,"xsec_unc":0.8983,"equivalent_lumi":3.347,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_PreVFP_1000To1500":{"dir":QCD_bEnriched_HT_1000to1500_UL_2016_PreVFP,"nevents":591966,"xsec":46.61,"xsec_unc":0.2002,"equivalent_lumi":21.2,"fraction_negative_weight":0.002946, "das_path":"/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_PreVFP_1500To2000":{"dir":QCD_bEnriched_HT_1500to2000_UL_2016_PreVFP,"nevents":675657,"xsec":4.017,"xsec_unc":0.01213,"equivalent_lumi":248.9,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"},\
      "QCD_bEnriched_HT_UL2016_PreVFP_2000ToInf":{"dir":QCD_bEnriched_HT_2000toInf_UL_2016_PreVFP,"nevents":668223,"xsec":0.6967,"xsec_unc":0.002099,"equivalent_lumi":1435.0,"fraction_negative_weight":0.0, "das_path":"/QCD_bEnriched_HT200toInf_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"},\
      },

	"TGJets_UL_2016":{"dir":TGJets_UL_2017,"nevents":1965000,"xsec":2.997,"xsec_unc":0.01239,"equivalent_lumi":14.46,"fraction_negative_weight":0.3959,"das_path":"/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"},
        "TTGJets_UL_2016":{"dir":TTGJets_UL_2017,"nevents":3534208,"xsec":3.757,"xsec_unc":0.02243,"equivalent_lumi":33.81,"fraction_negative_weight":0.3218,"das_path":"/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        "WZG_UL_2016":{"dir":WZG_UL_2017,"nevents":1400000,"xsec":3.75,"xsec_unc":4.524e-05,"equivalent_lumi":16260.0,"fraction_negative_weight":0.07975,"das_path":"/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        "ZGToLLG_UL_2016":{"dir":ZGToLLG_UL_2017,"nevents":29890946,"xsec":51.1,"xsec_unc":0.8077,"equivalent_lumi":7.41,"fraction_negative_weight":0.1923,"das_path":"/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},

	"TGJets_UL_2016_PreVFP":{"dir":TGJets_UL_2017,"nevents":1965000,"xsec":2.997,"xsec_unc":0.01239,"equivalent_lumi":14.46,"fraction_negative_weight":0.3959,"das_path":"/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"},
        "TTGJets_UL_2016_PreVFP":{"dir":TTGJets_UL_2017,"nevents":3534208,"xsec":3.757,"xsec_unc":0.02243,"equivalent_lumi":33.81,"fraction_negative_weight":0.3218,"das_path":"/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        "WZG_UL_2016_PreVFP":{"dir":WZG_UL_2017,"nevents":1400000,"xsec":3.75,"xsec_unc":4.524e-05,"equivalent_lumi":16260.0,"fraction_negative_weight":0.07975,"das_path":"/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        "ZGToLLG_UL_2016_PreVFP":{"dir":ZGToLLG_UL_2017,"nevents":29890946,"xsec":51.1,"xsec_unc":0.8077,"equivalent_lumi":7.41,"fraction_negative_weight":0.1923,"das_path":"/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},

  },\
  # closes bkg
  "data":{\
    "SinglePhoton_UL_PreVFP":{\
      "B_ver1":{"dir":path_data_UL_PreVFP+tag+"B_ver1/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "B_ver2":{"dir":path_data_UL_PreVFP+tag+"B_ver2/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "C":{"dir":path_data_UL_PreVFP+tag+"Run2016C/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "D":{"dir":path_data_UL_PreVFP+tag+"Run2016D/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "E":{"dir":path_data_UL_PreVFP+tag+"Run2016E/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "F":{"dir":path_data_UL_PreVFP+tag+"Run2016F/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      }, #single photon UL2016 APV
 "SinglePhoton_UL_PostVFP":{\
      "F_noHIPM":{"dir":path_data_UL+tag+"run2016F_noHIPM/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "G":{"dir":path_data_UL+tag+"Run2016G/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016G-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"},\
      "H":{"dir":path_data_UL+tag+"Run2016H/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016H-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"},\
      }, #single photon UL2016 POST APV


  } # closes data
  }, # closes the 2016
  2017: \
  {
        "signal":{
                "G1Jet_LHEGpt":\
                                {
                        "G1Jet_LHEGpt_150To250_2017":{"dir":G1Jet_LHEGPt_150To250_2017,"nevents":11616288,"xsec":2.262e+2,"xsec_unc":6.433e-1,"equivalent_lumi":1.882,"fraction_negative_weight":0.1738, "das_path":"/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "G1Jet_LHEGpt_250To400_2017":{"dir":G1Jet_LHEGPt_250To400_2017,"nevents":5994569,"xsec":2.699e+1,"xsec_unc":0.08345,"equivalent_lumi":17.17,"fraction_negative_weight":0.1697, "das_path":"/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "G1Jet_LHEGpt_400To675_2017":{"dir":G1Jet_LHEGPt_400To675_2017,"nevents":1999564,"xsec":3.395,"xsec_unc":0.007753,"equivalent_lumi":133.2,"fraction_negative_weight":0.1638, "das_path":"/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "G1Jet_LHEGpt_675ToInf_2017":{"dir":G1Jet_LHEGPt_675ToInf_2017,"nevents":498411,"xsec":2.478e-1,"xsec_unc":0.0005027,"equivalent_lumi":1883.0,"fraction_negative_weight":0.1584, "das_path":"/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                                },\
                  "GJets_DR_0p4_HT":\
                                {
                         "GJets_DR_0p4_HT_100To200_2017":{"dir":GJets_DR_0p4_HT_100To200_2017,"nevents":10034997,"xsec":5034.0,"xsec_unc":14.69,"equivalent_lumi":0.1986,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
                         "GJets_DR_0p4_HT_200To400_2017":{"dir":GJets_DR_0p4_HT_200To400_2017,"nevents":33884844,"xsec":1129.0,"xsec_unc":3.338,"equivalent_lumi":0.8859,"fraction_negative_weight":0.0,"das_path":"/GJets_DR_0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
                         "GJets_DR_0p4_HT_400To600_2017":{"dir":GJets_DR_0p4_HT_400To600_2017,"nevents":9022800,"xsec":126.2,"xsec_unc":0.03779,"equivalent_lumi":7.921,"fraction_negative_weight":0.0,"das_path":"/GJets_DR_0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
                         "GJets_DR_0p4_HT_600ToInf_2017":{"dir":GJets_DR_0p4_HT_600ToInf_2017,"nevents":8330226,"xsec":41.31,"xsec_unc":0.1242,"equivalent_lumi":24.21,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
                                },\
        },\
        #closes signal
	"bkg":{\
                "QCD_HT_UL2017":{ \
                        "QCD_HT_UL2017_50To100":{"dir":QCD_HT_50to100_UL_2017,"nevents":26243010,"xsec":1.860e+8,"xsec_unc":4.897e+4,"equivalent_lumi":5.377e-06,"fraction_negative_weight":0.0, "das_path":"/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "QCD_HT_UL2017_100To200":{"dir":QCD_HT_100to200_UL_2017,"nevents":54381393,"xsec":2.365e+7,"xsec_unc":4.467e+3,"equivalent_lumi":4.229e-05,"fraction_negative_weight":0.0, "das_path":"/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "QCD_HT_UL2017_200To300":{"dir":QCD_HT_200to300_UL_2017,"nevents":42714435,"xsec":1.553e+6,"xsec_unc":3.499e+2,"equivalent_lumi":6.440e-04  ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "QCD_HT_UL2017_300To500":{"dir":QCD_HT_300to500_UL_2017,"nevents":43429979,"xsec":3.245e+5,"xsec_unc":75.53,"equivalent_lumi":3.082e-3,"fraction_negative_weight":0.0, "das_path":"/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "QCD_HT_UL2017_500To700":{"dir":QCD_HT_500to700_UL_2017,"nevents":36194860,"xsec":3.028e+4,"xsec_unc":7.439,"equivalent_lumi":0.03303 ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "QCD_HT_UL2017_700To1000":{"dir":QCD_HT_700to1000_UL_2017,"nevents":32934816,"xsec":6.437e+3,"xsec_unc":1.658,"equivalent_lumi":0.1554,"fraction_negative_weight":0.0, "das_path":"/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "QCD_HT_UL2017_1000To1500":{"dir":QCD_HT_1000to1500_UL_2017,"nevents":10186734,"xsec":1.122e+3,"xsec_unc":0.5173,"equivalent_lumi":0.8911  ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "QCD_HT_UL2017_1500To2000":{"dir":QCD_HT_1500to2000_UL_2017,"nevents":7701876,"xsec":1.083e+2,"xsec_unc":0.05823,"equivalent_lumi":9.230,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        "QCD_HT_UL2017_2000ToInf":{"dir":QCD_HT_2000toInf_UL_2017,"nevents":4112573,"xsec":2.204e+1,"xsec_unc":0.01560,"equivalent_lumi":45.38,"fraction_negative_weight":0.0, "das_path":"/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                        },
		"QCD_bEnriched_HT_UL2017":{ \
      			"QCD_bEnriched_HT_UL2017_100To200":{"dir":QCD_bEnriched_HT_100to200_UL_2017,"nevents":37074807,"xsec":1127000.0,"xsec_unc":3241.0,"equivalent_lumi":0.0008871,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
      			"QCD_bEnriched_HT_UL2017_200To300":{"dir":QCD_bEnriched_HT_200to300_UL_2017,"nevents":19844424,"xsec":80220.0,"xsec_unc":235.7,"equivalent_lumi":0.01247  ,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
      			"QCD_bEnriched_HT_UL2017_300To500":{"dir":QCD_bEnriched_HT_300to500_UL_2017,"nevents":11312350,"xsec":16700.0,"xsec_unc":49.74,"equivalent_lumi":0.05988,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
      			"QCD_bEnriched_HT_UL2017_500To700":{"dir":QCD_bEnriched_HT_500to700_UL_2017,"nevents":10203561,"xsec":1487.0,"xsec_unc":4.442,"equivalent_lumi":0.6699 ,"fraction_negative_weight":0.001047,"das_path":"/QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
      			"QCD_bEnriched_HT_UL2017_700To1000":{"dir":QCD_bEnriched_HT_700to1000_UL_2017,"nevents":1881618,"xsec":298.8,"xsec_unc":0.8983,"equivalent_lumi":3.347,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
      			"QCD_bEnriched_HT_UL2017_1000To1500":{"dir":QCD_bEnriched_HT_1000to1500_UL_2017,"nevents":1385631,"xsec":46.61,"xsec_unc":0.2002,"equivalent_lumi":21.2,"fraction_negative_weight":0.002946,"das_path":"/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
     				"QCD_bEnriched_HT_UL2017_1500To2000":{"dir":QCD_bEnriched_HT_1500to2000_UL_2017,"nevents":1458069,"xsec":4.017,"xsec_unc":0.01213,"equivalent_lumi":248.9,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
      			"QCD_bEnriched_HT_UL2017_2000ToInf":{"dir":QCD_bEnriched_HT_2000toInf_UL_2017,"nevents":1408971,"xsec":0.6967,"xsec_unc":0.002099,"equivalent_lumi":1435.0,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},\
      			},
	"TGJets_UL_2017":{"dir":TGJets_UL_2017,"nevents":1965000,"xsec":2.997,"xsec_unc":0.01239,"equivalent_lumi":14.46,"fraction_negative_weight":0.3959,"das_path":"/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"},
        "TTGJets_UL_2017":{"dir":TTGJets_UL_2017,"nevents":3534208,"xsec":3.757,"xsec_unc":0.02243,"equivalent_lumi":33.81,"fraction_negative_weight":0.3218,"das_path":"/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        "WZG_UL_2017":{"dir":WZG_UL_2017,"nevents":1400000,"xsec":3.75,"xsec_unc":4.524e-05,"equivalent_lumi":16260.0,"fraction_negative_weight":0.07975,"das_path":"/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        "ZGToLLG_UL_2017":{"dir":ZGToLLG_UL_2017,"nevents":29890946,"xsec":51.1,"xsec_unc":0.8077,"equivalent_lumi":7.41,"fraction_negative_weight":0.1923,"das_path":"/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        },\
        #closes bkg
  "data":{\
                "SinglePhoton_UL":{\
                        "B":{"dir":path_data_UL_17+tag+"Run2017B/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
                        "C":{"dir":path_data_UL_17+tag+"Run2017C/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
                        "D":{"dir":path_data_UL_17+tag+"Run2017D/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
                        "E":{"dir":path_data_UL_17+tag+"Run2017E/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
                        "F":{"dir":path_data_UL_17+tag+"Run2017F/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
                                }, #single photon UL2017
        }
	},#Closes 2017 
  2018: \
  {
        "signal":{
                "G1Jet_LHEGpt":\
                                {
                        "G1Jet_LHEGpt_150To250_2018":{"dir":G1Jet_LHEGPt_150To250_2018,"nevents":11192434,"xsec":2.262e+2,"xsec_unc":6.433e-1,"equivalent_lumi":1.882,"fraction_negative_weight":0.1738, "das_path":"/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "G1Jet_LHEGpt_250To400_2018":{"dir":G1Jet_LHEGPt_250To400_2018,"nevents":6004413,"xsec":2.699e+1,"xsec_unc":0.08345,"equivalent_lumi":17.17,"fraction_negative_weight":0.1697, "das_path":"/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "G1Jet_LHEGpt_400To675_2018":{"dir":G1Jet_LHEGPt_400To675_2018,"nevents":1999690,"xsec":3.395,"xsec_unc":0.007753,"equivalent_lumi":133.2,"fraction_negative_weight":0.1638, "das_path":"/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "G1Jet_LHEGpt_675ToInf_2018":{"dir":G1Jet_LHEGPt_675ToInf_2018,"nevents":498616,"xsec":2.478e-1,"xsec_unc":0.0005027,"equivalent_lumi":1883.0,"fraction_negative_weight":0.1584, "das_path":"/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"},\
                                },\
                 "GJets_DR_0p4_HT":\
                                {
                         "GJets_DR_0p4_HT_100To200_2018":{"dir":GJets_DR_0p4_HT_100To200_2018,"nevents":14278296,"xsec":5034.0,"xsec_unc":14.69,"equivalent_lumi":0.1986,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                         "GJets_DR_0p4_HT_200To400_2018":{"dir":GJets_DR_0p4_HT_200To400_2018,"nevents":44247215,"xsec":1129.0,"xsec_unc":3.338,"equivalent_lumi":0.8859,"fraction_negative_weight":0.0,"das_path":"/GJets_DR_0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                         "GJets_DR_0p4_HT_400To600_2018":{"dir":GJets_DR_0p4_HT_400To600_2018,"nevents":13373955,"xsec":126.2,"xsec_unc":0.03779,"equivalent_lumi":7.921,"fraction_negative_weight":0.0,"das_path":"/GJets_DR_0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                         "GJets_DR_0p4_HT_600ToInf_2018":{"dir":GJets_DR_0p4_HT_600ToInf_2018,"nevents":11584420,"xsec":41.31,"xsec_unc":0.1242,"equivalent_lumi":24.21,"fraction_negative_weight":0.0, "das_path":"/GJets_DR_0p4_HT-400ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                                        },\
        },\
        #closes signal
        "bkg":{
		"QCD_HT_UL2018":{ \
                        "QCD_HT_UL2018_50To100":{"dir":QCD_HT_50to100_UL_2018,"nevents":38599389,"xsec":1.860e+8,"xsec_unc":4.897e+4,"equivalent_lumi":5.377e-06,"fraction_negative_weight":0.0, "das_path":"/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_HT_UL2018_100To200":{"dir":QCD_HT_100to200_UL_2018,"nevents":84434559,"xsec":2.365e+7,"xsec_unc":4.467e+3,"equivalent_lumi":4.229e-05,"fraction_negative_weight":0.0, "das_path":"/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_HT_UL2018_200To300":{"dir":QCD_HT_200to300_UL_2018,"nevents":57336623,"xsec":1.553e+6,"xsec_unc":3.499e+2,"equivalent_lumi":6.440e-04  ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_HT_UL2018_300To500":{"dir":QCD_HT_300to500_UL_2018,"nevents":61609663,"xsec":3.245e+5,"xsec_unc":75.53,"equivalent_lumi":3.082e-3,"fraction_negative_weight":0.0, "das_path":"/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_HT_UL2018_500To700":{"dir":QCD_HT_500to700_UL_2018,"nevents":49184771,"xsec":3.028e+4,"xsec_unc":7.439,"equivalent_lumi":0.03303 ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_HT_UL2018_700To1000":{"dir":QCD_HT_700to1000_UL_2018,"nevents":48506751,"xsec":6.437e+3,"xsec_unc":1.658,"equivalent_lumi":0.1554,"fraction_negative_weight":0.0, "das_path":"/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_HT_UL2018_1000To1500":{"dir":QCD_HT_1000to1500_UL_2018,"nevents":14394786,"xsec":1.122e+3,"xsec_unc":0.5173,"equivalent_lumi":0.8911  ,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_HT_UL2018_1500To2000":{"dir":QCD_HT_1500to2000_UL_2018,"nevents":10411831,"xsec":1.083e+2,"xsec_unc":0.05823,"equivalent_lumi":9.230,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_HT_UL2018_2000ToInf":{"dir":QCD_HT_2000toInf_UL_2018,"nevents":5374711,"xsec":2.204e+1,"xsec_unc":0.01560,"equivalent_lumi":45.38,"fraction_negative_weight":0.0, "das_path":"/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        },
		"QCD_bEnriched_HT_UL2018":{ \
                        "QCD_bEnriched_HT_UL2018_100To200":{"dir":QCD_bEnriched_HT_100to200_UL_2018,"nevents":36118282,"xsec":1127000.0,"xsec_unc":3241.0,"equivalent_lumi":0.0008871,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_bEnriched_HT_UL2018_200To300":{"dir":QCD_bEnriched_HT_200to300_UL_2018,"nevents":18462183,"xsec":80220.0,"xsec_unc":235.7,"equivalent_lumi":0.01247  ,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_bEnriched_HT_UL2018_300To500":{"dir":QCD_bEnriched_HT_300to500_UL_2018,"nevents":11197722,"xsec":16700.0,"xsec_unc":49.74,"equivalent_lumi":0.05988,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_bEnriched_HT_UL2018_500To700":{"dir":QCD_bEnriched_HT_500to700_UL_2018,"nevents":9246898,"xsec":1487.0,"xsec_unc":4.442,"equivalent_lumi":0.6699 ,"fraction_negative_weight":0.001047,"das_path":"/QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1NANOAODSIM"},\
                        "QCD_bEnriched_HT_UL2018_700To1000":{"dir":QCD_bEnriched_HT_700to1000_UL_2018,"nevents":1844165,"xsec":298.8,"xsec_unc":0.8983,"equivalent_lumi":3.347,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "QCD_bEnriched_HT_UL2018_1000To1500":{"dir":QCD_bEnriched_HT_1000to1500_UL_2018,"nevents":1330829,"xsec":46.61,"xsec_unc":0.2002,"equivalent_lumi":21.2,"fraction_negative_weight":0.002946,"das_path":"/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                                "QCD_bEnriched_HT_UL2018_1500To2000":{"dir":QCD_bEnriched_HT_1500to2000_UL_2018,"nevents":1431254,"xsec":4.017,"xsec_unc":0.01213,"equivalent_lumi":248.9,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1NANOAODSIM"},\
                        "QCD_bEnriched_HT_UL2018_2000ToInf":{"dir":QCD_bEnriched_HT_2000toInf_UL_2018,"nevents":1357334,"xsec":0.6967,"xsec_unc":0.002099,"equivalent_lumi":1435.0,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        },
"TGJets_UL_2018":{"dir":TGJets_UL_2018,"nevents":1965000,"xsec":2.997,"xsec_unc":0.01239,"equivalent_lumi":14.46,"fraction_negative_weight":0.3959,"das_path":"/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"},
        "TTGJets_UL_2018":{"dir":TTGJets_UL_2018,"nevents":3534208,"xsec":3.757,"xsec_unc":0.02243,"equivalent_lumi":33.81,"fraction_negative_weight":0.3218,"das_path":"/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        "WZG_UL_2018":{"dir":WZG_UL_2018,"nevents":1400000,"xsec":3.75,"xsec_unc":4.524e-05,"equivalent_lumi":16260.0,"fraction_negative_weight":0.07975,"das_path":"/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},
        "ZGToLLG_UL_2018":{"dir":ZGToLLG_UL_2018,"nevents":29890946,"xsec":51.1,"xsec_unc":0.8077,"equivalent_lumi":7.41,"fraction_negative_weight":0.1923,"das_path":"/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"},

		"WJetsToLNu_HT":{ \
                        "WJetsToLNu_HT_UL2018_100To200":{"dir":  WJetsToLNu_HT_100to200_UL_2018,"nevents":51408967,"xsec":1395.0,"xsec_unc":235.7,"equivalent_lumi":0.01247  ,"fraction_negative_weight":0.0,"das_path":"/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "WJetsToLNu_HT_UL2018_200To400":{"dir":  WJetsToLNu_HT_200to400_UL_2018,"nevents":58225632,"xsec":407.9,"xsec_unc":49.74,"equivalent_lumi":0.05988,"fraction_negative_weight":0.0,"das_path":"/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "WJetsToLNu_HT_UL2018_400To600":{"dir":  WJetsToLNu_HT_400to600_UL_2018,"nevents":9246898,"xsec":57.48,"xsec_unc":4.442,"equivalent_lumi":0.6699 ,"fraction_negative_weight":0.001047,"das_path":"/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "WJetsToLNu_HT_UL2018_600To800":{"dir":  WJetsToLNu_HT_600to800_UL_2018,"nevents":7718765,"xsec":12.87,"xsec_unc":0.8983,"equivalent_lumi":3.347,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "WJetsToLNu_HT_UL2018_800To1200":{"dir": WJetsToLNu_HT_800to1200_UL_2018,"nevents":7306187,"xsec":5.366,"xsec_unc":0.2002,"equivalent_lumi":21.2,"fraction_negative_weight":0.002946,"das_path":"/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "WJetsToLNu_HT_UL2018_1200To2500":{"dir":WJetsToLNu_HT_1200to2500_UL_2018,"nevents":6481518,"xsec":1.074,"xsec_unc":0.01213,"equivalent_lumi":248.9,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1NANOAODSIM"},\
                        "WJetsToLNu_HT_UL2018_2500ToInf":{"dir": WJetsToLNu_HT_2500toInf_UL_2018,"nevents":2097648,"xsec":0.008001,"xsec_unc":0.002099,"equivalent_lumi":1435.0,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        },

		"DYJetsToLL_M_50_HT":{ \
                        "DYJetsToLL_M_50_HT_UL2018_100To200":{"dir":  DYJetsToLL_M_50_HT_100to200_UL_2018,"nevents":26202328,"xsec":161.1,"xsec_unc":235.7,"equivalent_lumi":0.01247  ,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "DYJetsToLL_M_50_HT_UL2018_200To400":{"dir":  DYJetsToLL_M_50_HT_200to400_UL_2018,"nevents":18455718,"xsec":48.6,"xsec_unc":49.74,"equivalent_lumi":0.05988,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "DYJetsToLL_M_50_HT_UL2018_400To600":{"dir":  DYJetsToLL_M_50_HT_400to600_UL_2018,"nevents":8682257,"xsec":6.96,"xsec_unc":4.442,"equivalent_lumi":0.6699 ,"fraction_negative_weight":0.001047,"das_path":"/QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1NANOAODSIM"},\
                        "DYJetsToLL_M_50_HT_UL2018_600To800":{"dir":  DYJetsToLL_M_50_HT_600to800_UL_2018,"nevents":7035971,"xsec":1.74,"xsec_unc":0.8983,"equivalent_lumi":3.347,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "DYJetsToLL_M_50_HT_UL2018_800To1200":{"dir": DYJetsToLL_M_50_HT_800to1200_UL_2018,"nevents":6554679,"xsec":0.8052,"xsec_unc":0.2002,"equivalent_lumi":21.2,"fraction_negative_weight":0.002946,"das_path":"/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        "DYJetsToLL_M_50_HT_UL2018_1200To2500":{"dir":DYJetsToLL_M_50_HT_1200to2500_UL_2018,"nevents":5966661,"xsec":0.1933,"xsec_unc":0.01213,"equivalent_lumi":248.9,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1NANOAODSIM"},\
                        "DYJetsToLL_M_50_HT_UL2018_2500ToInf":{"dir": DYJetsToLL_M_50_HT_2500toInf_UL_2018,"nevents":1978203,"xsec":0.003468,"xsec_unc":0.002099,"equivalent_lumi":1435.0,"fraction_negative_weight":0.0,"das_path":"/QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106Xupgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"},\
                        },

        },\
        #closes bkg
        "data":{\
                "EGamma_UL":{\
                        "A":{"dir":path_data_UL_18+tag+"Run2018A/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
                        "B":{"dir":path_data_UL_18+tag+"Run2018B/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
                        "C":{"dir":path_data_UL_18+tag+"Run2018C/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
                        "D":{"dir":path_data_UL_18+tag+"Run2018D/"+subdir, "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
			}
        }# closes data
  } #closes 2018
  } # closes the sample dic


pickle.dump(Samples, open("samples_ana.pkl", "wb"))
