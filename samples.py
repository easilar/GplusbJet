# Sample dictionary for a GammaplusbJets Run II Analysis

import pickle

save_orig = True

path_MC = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/MC_filtered/"
path_data = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied_loose/SinglePhoton/"
path_data_SM = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied/SingleMuon/"
if save_orig:
	path_MC = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/MC/"
	#path_data = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied_HLT_Photon175_MetFilters/SinglePhoton/"
	path_data = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied_HLT_Photon175_MetFilters_Photon_Jet/SinglePhoton/"
	#path_data = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied_loose/SinglePhoton/"
	#path_data = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/data/SinglePhoton/data/"
	path_data_SM = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/data/SingleMuon/"
GJets_2016 = path_MC+"GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8_20M/"
GJets_Pt_100To200_2016 = path_MC+"GJets_Pt-100To200_13TeV-sherpa/"
GJets_Pt_200To500_2016 = path_MC+"GJets_Pt-200To500_13TeV-sherpa/"
GJets_Pt_500To1000_2016 = path_MC+"GJets_Pt-500To1000_13TeV-sherpa/"
GJets_Pt_1000To2000_2016 = path_MC+"GJets_Pt-1000To2000_13TeV-sherpa/"
GJets_Pt_2000To5000_2016 = path_MC+"GJets_Pt-2000To5000_13TeV-sherpa/"
G1Jet_Pt_50To100_2016 = path_MC+"G1Jet_Pt-50To100_TuneCUETP8M1_13TeV-amcatnlo-pythia8/"
G1Jet_Pt_100To250_2016 = path_MC+"G1Jet_Pt-100To250_TuneCUETP8M1_13TeV-amcatnlo-pythia8/"
G1Jet_Pt_250To400_2016 = path_MC+"G1Jet_Pt-250To400_TuneCUETP8M1_13TeV-amcatnlo-pythia8/"
G1Jet_Pt_400To650_2016 = path_MC+"G1Jet_Pt-400To650_TuneCUETP8M1_13TeV-amcatnlo-pythia8/"
G1Jet_Pt_650ToInf_2016 = path_MC+"G1Jet_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnlo-pythia8/"
GJets_HT_40To100_2016 = path_MC+"GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
GJets_HT_100To200_2016 = path_MC+"GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
GJets_HT_200To400_2016 = path_MC+"GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
GJets_HT_400To600_2016 = path_MC+"GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
GJets_HT_600ToInf_2016 = path_MC+"GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_2016 = path_MC+"QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/"
QCD_h1_2016 = path_MC+"QCD_Pt-15to7000_TuneCUETHS1_FlatP6_13TeV_herwigpp/"
QCD_h2_2016 = path_MC+"QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/"
QCD_HT_50to100_2016 = path_MC+"QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_HT_100to200_2016 = path_MC+"QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_HT_200to300_2016 = path_MC+"QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_HT_300to500_2016 = path_MC+"QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_HT_500to700_2016 = path_MC+"QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_HT_700to1000_2016 = path_MC+"QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_HT_1000to1500_2016 = path_MC+"QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_HT_1500to2000_2016 = path_MC+"QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
QCD_HT_2000toInf_2016 = path_MC+"QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"
TGJets_2016 = path_MC+"TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/"
TTGJets_2016 = path_MC+"TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/"
ST_s_channel_2016 = path_MC+"ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/"
ST_t_channel_antitop_2016 = path_MC+"ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"
ST_t_channel_top_2016 = path_MC+"ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"
ST_tW_antitop_2016 = path_MC+"ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"
ST_tW_top_2016 = path_MC+"ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"
TTJets_2016 = path_MC+"TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"

###xsect dictionary: valuses are taken from https://cms-gen-dev.cern.ch/xsdb/ Metin!!!!###
###Das paths are Added####
Samples = {2016: \
	{"signal":\
		{"GJets":\
			{"dir":GJets_2016,"nevents":19794775,"xsec":365400.0,"xsec_unc":382.7,"equivalent_lumi":0.002737,"fraction_negative_weight":0.0, "das_path":"/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8_20M/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
        	
        	"GJets_Pt":\
        			{	
            		"GJets_Pt_100To200":{"dir":GJets_Pt_100To200_2016,"nevents":498029,"xsec":1032.0,"xsec_unc":7.109,"equivalent_lumi":0.9342,"fraction_negative_weight":0.01085, "das_path":"/GJets_Pt-100To200_13TeV-sherpa/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
					"GJets_Pt_200To500":{"dir":GJets_Pt_200To500_2016,"nevents":476434,"xsec":70.15,"xsec_unc":0.6311,"equivalent_lumi":13.97,"fraction_negative_weight":0.01032, "das_path":"/GJets_Pt-200To500_13TeV-sherpa/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
					"GJets_Pt_500To1000":{"dir":GJets_Pt_500To1000_2016,"nevents":484865,"xsec":0.9904,"xsec_unc":0.00919,"equivalent_lumi":940.6,"fraction_negative_weight":0.01163, "das_path":"/GJets_Pt-500To1000_13TeV-sherpa/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
					"GJets_Pt_1000To2000":{"dir":GJets_Pt_1000To2000_2016,"nevents":399578,"xsec":0.02092,"xsec_unc":0.0001703,"equivalent_lumi":45040.0,"fraction_negative_weight":0.01466, "das_path":"/GJets_Pt-1000To2000_13TeV-sherpa/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
					"GJets_Pt_2000To5000":{"dir":GJets_Pt_2000To5000_2016,"nevents":299739,"xsec":0.00007451,"xsec_unc":0.0000007843,"equivalent_lumi":7537000.0,"fraction_negative_weight":0.1247, "das_path":"/GJets_Pt-2000To5000_13TeV-sherpa/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
					},\
			"G1Jet_Pt":\
					{
					"G1Jet_Pt_50To100":{"dir":G1Jet_Pt_50To100_2016,"nevents":97795100,"xsec":1.353e+4,"xsec_unc":55.01,"equivalent_lumi":0.02261,"fraction_negative_weight":0.2234, "das_path":"/G1Jet_Pt-50To100_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					"G1Jet_Pt_100To250":{"dir":G1Jet_Pt_100To250_2016,"nevents":9964624,"xsec":1.155e+3,"xsec_unc":4.489,"equivalent_lumi":0.2606,"fraction_negative_weight":0.2257, "das_path":"/G1Jet_Pt-100To250_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					"G1Jet_Pt_250To400":{"dir":G1Jet_Pt_250To400_2016,"nevents":997008,"xsec":2.548e+1,"xsec_unc":0.07909,"equivalent_lumi":11.18,"fraction_negative_weight":0.2331, "das_path":"/G1Jet_Pt-250To400_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					"G1Jet_Pt_400To650":{"dir":G1Jet_Pt_400To650_2016,"nevents":999000,"xsec":3.14,"xsec_unc":0.007797,"equivalent_lumi":91.08,"fraction_negative_weight":0.2326, "das_path":"/G1Jet_Pt-400To650_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					"G1Jet_Pt_650ToInf":{"dir":G1Jet_Pt_650ToInf_2016,"nevents":999314,"xsec":2.939e-1,"xsec_unc":0.0006189,"equivalent_lumi":1088.0,"fraction_negative_weight":0.2172, "das_path":"/G1Jet_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					},\
			"GJets_HT":\
					{
					"GJets_HT_40To100":{"dir":GJets_HT_40To100_2016,"nevents":4858154,"xsec":2.079e+4,"xsec_unc":59.82,"equivalent_lumi":0.04811,"fraction_negative_weight":0.0, "das_path":"/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					"GJets_HT_100To200":{"dir":GJets_HT_100To200_2016,"nevents":4972282,"xsec":9.238e+3,"xsec_unc":27.11,"equivalent_lumi":0.1087,"fraction_negative_weight":0.0, "das_path":"/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					"GJets_HT_200To400":{"dir":GJets_HT_200To400_2016,"nevents":10404907,"xsec":2.305e+3,"xsec_unc":6.945,"equivalent_lumi":0.4316,"fraction_negative_weight":0.0, "das_path":"/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					"GJets_HT_400To600":{"dir":GJets_HT_400To600_2016,"nevents":2530341,"xsec":2.744e+2,"xsec_unc":0.8368,"equivalent_lumi":3.612,"fraction_negative_weight":0.0, "das_path":"/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					"GJets_HT_600ToInf":{"dir":GJets_HT_600ToInf_2016,"nevents":2616911,"xsec":9.346e+1,"xsec_unc":0.2861,"equivalent_lumi":10.61,"fraction_negative_weight":0.0, "das_path":"/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
					},\

		},\
 	"bkg":{\
		"QCD":{"dir":QCD_2016,"nevents":9879256,"xsec":1370000000.0,"xsec_unc":2159000.0,"equivalent_lumi":7.301e-07,"fraction_negative_weight":0.0, "das_path":"/QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
		"QCD_h1":{"dir":QCD_h1_2016,"nevents":9497268,"xsec":964800.0,"xsec_unc":92360.0,"equivalent_lumi":7.301e-07,"fraction_negative_weight":0.0, "das_path":"/QCD_Pt-15to7000_TuneCUETHS1_FlatP6_13TeV_herwigpp/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
		"QCD_h2":{"dir":QCD_h2_2016,"nevents":9865688,"xsec":309800000.0,"xsec_unc":7932000.0,"equivalent_lumi":7.301e-07,"fraction_negative_weight":0.0, "das_path":"/QCD_Pt-15to7000_TuneCUETHS1_Flat_13TeV_herwigpp/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
 		"QCD_HT":\
 			{	
			"QCD_HT_50To100":{"dir":QCD_HT_50to100_2016,"nevents":4180469,"xsec":2.464e+8,"xsec_unc":218700.0,"equivalent_lumi":4.061e-06,"fraction_negative_weight":0.0, "das_path":"/QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
			"QCD_HT_100To200":{"dir":QCD_HT_100to200_2016,"nevents":82293477,"xsec":2.799e+7,"xsec_unc":26130.0,"equivalent_lumi":3.564e-05,"fraction_negative_weight":0.0, "das_path":"/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
			"QCD_HT_200To300":{"dir":QCD_HT_200to300_2016,"nevents":38857977,"xsec":1.712e+6,"xsec_unc":1626.0,"equivalent_lumi":0.0005846	,"fraction_negative_weight":0.0, "das_path":"/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
			"QCD_HT_300To500":{"dir":QCD_HT_300to500_2016,"nevents":37516961,"xsec":3.477e+5,"xsec_unc":332.9,"equivalent_lumi":0.002878,"fraction_negative_weight":0.0, "das_path":"/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
			"QCD_HT_500To700":{"dir":QCD_HT_500to700_2016,"nevents":44061488,"xsec":3.210e+4,"xsec_unc":30.88,"equivalent_lumi":0.03119	,"fraction_negative_weight":0.0, "das_path":"/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
			"QCD_HT_700To1000":{"dir":QCD_HT_700to1000_2016,"nevents":21604533,"xsec":6.831e+3,"xsec_unc":6.593,"equivalent_lumi":0.1464,"fraction_negative_weight":0.0, "das_path":"/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
			"QCD_HT_1000To1500":{"dir":QCD_HT_1000to1500_2016,"nevents":10360193,"xsec":1.207e+3,"xsec_unc":1.166,"equivalent_lumi":0.8285	,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
			"QCD_HT_1500To2000":{"dir":QCD_HT_1500to2000_2016,"nevents":7868538,"xsec":1.199e+2,"xsec_unc":0.1159,"equivalent_lumi":8.335,"fraction_negative_weight":0.0, "das_path":"/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
			"QCD_HT_2000ToInf":{"dir":QCD_HT_2000toInf_2016,"nevents":3812534,"xsec":2.524e+1,"xsec_unc":0.02437,"equivalent_lumi":39.6,"fraction_negative_weight":0.0, "das_path":"/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
			},\
 		"TGJets":{"dir":TGJets_2016,"nevents":1556996,"xsec":2.967,"xsec_unc":0.01052,"equivalent_lumi":13.27,"fraction_negative_weight":0.4008, "das_path":"/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"},\
 		"TTGJets":{"dir":TTGJets_2016,"nevents":9877942,"xsec":3.795,"xsec_unc":0.02629,"equivalent_lumi":27.63,"fraction_negative_weight":0.3381, "das_path":"/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"},\
		"ST_s_channel":{"dir":ST_s_channel_2016,"nevents":2917199, "xsec":10.12,"xsec_unc":0.01334,"equivalent_lumi":39.05,"fraction_negative_weight":0.1857, "das_path":"/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
		"ST_t_channel_antitop":{"dir":ST_t_channel_antitop_2016,"nevents":38811017, "xsec":81.42,"xsec_unc":0.0,"equivalent_lumi":0.0,"fraction_negative_weight":0.0, "das_path":"/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
		"ST_t_channel_top":{"dir":ST_t_channel_top_2016,"nevents":58403420, "xsec":136.82,"xsec_unc":0.0,"equivalent_lumi":0.0,"fraction_negative_weight":0.0, "das_path":"/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v2/NANOAODSIM"},\
		"ST_tW_antitop":{"dir":ST_tW_antitop_2016,"nevents":6933094, "xsec":38.06,"xsec_unc":0.03055,"equivalent_lumi":26.27,"fraction_negative_weight":0.0, "das_path":"/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
		"ST_tW_top":{"dir":ST_tW_top_2016,"nevents":6952830, "xsec":38.09,"xsec_unc":0.0305,"equivalent_lumi":26.25,"fraction_negative_weight":0.0, "das_path":"/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
		"TTJets":{"dir":TTJets_2016,"nevents":10199051,"xsec":511.3,"xsec_unc":1.412,"equivalent_lumi":1.956,"fraction_negative_weight":0.0, "das_path":"/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
	},\
	# closes bkg
	"data":{\
		"SinglePhoton":{\
			"B":{"dir":path_data+"Run2016B_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016B-02Apr2020_ver2-v1/NANOAOD"},\
			"C":{"dir":path_data+"Run2016C_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016C-02Apr2020-v1/NANOAOD"},\
			"D":{"dir":path_data+"Run2016D_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016D-02Apr2020-v1/NANOAOD"},\
			"E":{"dir":path_data+"Run2016E_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016E-02Apr2020-v1/NANOAOD"},\
			"F":{"dir":path_data+"Run2016F_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016F-02Apr2020-v1/NANOAOD"},\
			"G":{"dir":path_data+"Run2016G_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016G-02Apr2020-v1/NANOAOD"},\
			"H":{"dir":path_data+"Run2016H_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SinglePhoton/Run2016H-02Apr2020-v1/NANOAOD"},\
			}, #single photon
		"SingleMuon":{\
			"B":{"dir":path_data_SM+"Run2016B_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SingleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"},\
			"C":{"dir":path_data_SM+"Run2016C_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SingleMuon/Run2016C-02Apr2020-v1/NANOAOD"},\
			"D":{"dir":path_data_SM+"Run2016D_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SingleMuon/Run2016D-02Apr2020-v1/NANOAOD"},\
			"E":{"dir":path_data_SM+"Run2016E_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SingleMuon/Run2016E-02Apr2020-v1/NANOAOD"},\
			"F":{"dir":path_data_SM+"Run2016F_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SingleMuon/Run2016F-02Apr2020-v1/NANOAOD"},\
			"G":{"dir":path_data_SM+"Run2016G_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SingleMuon/Run2016G-02Apr2020-v1/NANOAOD"},\
			"H":{"dir":path_data_SM+"Run2016H_02Apr2020-v1", "xsec":1,"xsec_unc":1,"equivalent_lumi":1,"fraction_negative_weight":0.0, "das_path":"/SingleMuon/Run2016H-02Apr2020-v1/NANOAOD"},\
			} #single muon
	} # closes data
	} # closes the 2016
	} # closes the sample dict
if save_orig:
	pickle.dump(Samples, open("samples_orig.pkl", "wb"))
else:
	pickle.dump(Samples, open("samples_ana.pkl", "wb"))
