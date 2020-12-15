# Sample dictionary for a GammaplusbJets Run II Analysis

import pickle
path_MC = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/MC/"
path_orig_data = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/data/SinglePhoton/data/"
path_data = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied/"
path_data_SM = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied/SingleMuon/"
path_data_SM_orig = "/eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/data/SingleMuon/"
GJets_2016 = path_MC+"GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8_20M/"
QCD_2016 = path_MC+"QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/"
TGJets_2016 = path_MC+"TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/"
TTGJets_2016 = path_MC+"TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/"
ST_s_channel_2016 = path_MC+"ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8"
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
			{"dir":GJets_2016,"xsec":365400.0,"xsec_unc":382.7,"equivalent_lumi":0.002737,"fraction_negative_weight":0.0, "das_path":"/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8_20M/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"}
	},\
 	"bkg":{\
		"QCD":{"dir":QCD_2016,"xsec":1370000000.0,"xsec_unc":2159000.0,"equivalent_lumi":7.301e-07,"fraction_negative_weight":0.0, "das_path":"/QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
 		"TGJets":{"dir":TGJets_2016,"xsec":2.967,"xsec_unc":0.01052,"equivalent_lumi":13.27,"fraction_negative_weight":0.4008, "das_path":"/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"},\
 		"TTGJets":{"dir":TTGJets_2016,"xsec":3.795,"xsec_unc":0.02629,"equivalent_lumi":27.63,"fraction_negative_weight":0.3381, "das_path":"/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"},\
		"ST_s_channel":{"dir":ST_s_channel_2016, "xsec":10.12,"xsec_unc":0.01334,"equivalent_lumi":39.05,"fraction_negative_weight":0.1857, "das_path":"/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
		"ST_t_channel_antitop":{"dir":ST_t_channel_antitop_2016, "xsec":81.42,"xsec_unc":0.0,"equivalent_lumi":0.0,"fraction_negative_weight":0.0, "das_path":"/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
		"ST_t_channel_top":{"dir":ST_t_channel_top_2016, "xsec":136.82,"xsec_unc":0.0,"equivalent_lumi":0.0,"fraction_negative_weight":0.0, "das_path":"/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v2/NANOAODSIM"},\
		"ST_tW_antitop":{"dir":ST_tW_antitop_2016, "xsec":38.06,"xsec_unc":0.03055,"equivalent_lumi":26.27,"fraction_negative_weight":0.0, "das_path":"/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
		"ST_tW_top":{"dir":ST_tW_top_2016, "xsec":38.09,"xsec_unc":0.0305,"equivalent_lumi":26.25,"fraction_negative_weight":0.0, "das_path":"/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"},\
		"TTJets":{"dir":TTJets_2016,"xsec":511.3,"xsec_unc":1.412,"equivalent_lumi":1.956,"fraction_negative_weight":0.0, "das_path":"/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"},\
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

pickle.dump(Samples, open("samples.pkl", "wb"))
