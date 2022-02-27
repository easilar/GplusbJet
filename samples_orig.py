# Sample dictionary for a GammaplusbJets Run II Analysis

import pickle


path_MC_UL = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/UL_MC/"
path_data_UL = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/data/SinglePhoton/UL/"

G1Jet_LHEGPt_150To250_2016 = path_MC_UL+"G1Jet/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/"
G1Jet_LHEGPt_250To400_2016 = path_MC_UL+"G1Jet/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/"
G1Jet_LHEGPt_400To675_2016 = path_MC_UL+"G1Jet/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/"
G1Jet_LHEGPt_675ToInf_2016 = path_MC_UL+"G1Jet/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/"
G1Jet_LHEGPt_150To250_2016_PreVFP = path_MC_UL+"G1Jet_PreVFP/G1Jet_LHEGpT-150To250_TuneCP5_13TeV-amcatnlo-pythia8/"
G1Jet_LHEGPt_250To400_2016_PreVFP = path_MC_UL+"G1Jet_PreVFP/G1Jet_LHEGpT-250To400_TuneCP5_13TeV-amcatnlo-pythia8/"
G1Jet_LHEGPt_400To675_2016_PreVFP = path_MC_UL+"G1Jet_PreVFP/G1Jet_LHEGpT-400To675_TuneCP5_13TeV-amcatnlo-pythia8/"
G1Jet_LHEGPt_675ToInf_2016_PreVFP = path_MC_UL+"G1Jet_PreVFP/G1Jet_LHEGpT-675ToInf_TuneCP5_13TeV-amcatnlo-pythia8/"

QCD_HT_50to100_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_100to200_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_200to300_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_300to500_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_500to700_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_700to1000_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_1000to1500_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_1500to2000_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_2000toInf_UL_2016 = path_MC_UL+"QCD_HT/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"

QCD_HT_50to100_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_100to200_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_200to300_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_300to500_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_500to700_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_700to1000_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_1000to1500_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_1500to2000_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"
QCD_HT_2000toInf_UL_2016_PreVFP = path_MC_UL+"QCD_HT_PreVFP/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/"

###xsect dictionary: valuses are taken from https://cms-gen-dev.cern.ch/xsdb/ Metin!!!!###
###Das paths are Added####
Samples = {2016: \
	{"signal":\
		{\
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
    },\
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
  },\
  # closes bkg
  "data":{\
    "SinglePhoton_UL":{\
      "B_ver1":{"dir":path_data_UL+"B_ver1/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "B_ver2":{"dir":path_data_UL+"B_ver2/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "C":{"dir":path_data_UL+"Run2016C/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "D":{"dir":path_data_UL+"Run2016D/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "E":{"dir":path_data_UL+"Run2016E/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "F":{"dir":path_data_UL+"Run2016F/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "F_noHIPM":{"dir":path_data_UL+"run2016F_noHIPM/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"},\
      "G":{"dir":path_data_UL+"Run2016G/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016G-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"},\
      "H":{"dir":path_data_UL+"Run2016H/", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016H-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"},\
      }, #single photon UL2016
  } # closes data
  }, # closes the 2016
  2017: \
  {
	"signal":{
	},\
	#closes signal
	"bkg":{
	},\
	#closes bkg
  	"data":{\
    	} #closes data
  }, # closes 2017
  2018: \
  {
	"signal":{
	},\
	#closes signal
	"bkg":{
	},\
	#closes bkg
  	"data":{\
    	}# closes data
  } #closes 2018
  } # closes the sample dic

pickle.dump(Samples, open("samples_orig.pkl", "wb"))
