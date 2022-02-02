import json
import pickle


HLT_Photon50  = [
                 #"HLT_Photon50_R9Id90_HE10_IsoM_prescale10_2016_0p04.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale104_2016_2p70.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale120_2016_1p47.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale125_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale13_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale130_2016_2p16.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale150_2016_3p21.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale160_2016_0p12.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale170_2016_2p13.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale189_2016_1p81.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale20_2016_0p60.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale209_2016_0p20.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale26_2016_0p01.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale3_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale30_2016_1p13.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale46_2016_0p22.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale48_2016_5p47.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale5_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale60_2016_5p79.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale65_2016_1p98.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale7_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale80_2016_3p04.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale9_2016_0p01.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale91_2016_4p41.json"]



HLT_Photon36  = ["HLT_Photon36_R9Id90_HE10_IsoM_prescale1_2016_36p12.json",
                 "HLT_Photon36_R9Id90_HE10_IsoM_prescale2_2016_0p40.json",
                 "HLT_Photon36_R9Id90_HE10_IsoM_prescale25_2016_0p04.json"]
'''
HLT_Photon50  = ["HLT_Photon50_R9Id90_HE10_IsoM_prescale1_2016_2p20.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale10_2016_0p04.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale104_2016_2p70.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale120_2016_1p47.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale125_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale13_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale130_2016_2p16.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale150_2016_3p21.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale160_2016_0p12.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale170_2016_2p13.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale189_2016_1p81.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale20_2016_0p60.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale209_2016_0p20.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale26_2016_0p01.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale3_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale30_2016_1p13.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale46_2016_0p22.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale48_2016_5p47.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale5_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale60_2016_5p79.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale65_2016_1p98.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale7_2016_0p00.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale80_2016_3p04.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale9_2016_0p01.json",
                 "HLT_Photon50_R9Id90_HE10_IsoM_prescale91_2016_4p41.json"]
'''
HLT_Photon75  = ["HLT_Photon75_R9Id90_HE10_IsoM_prescale1_2016_2p20.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale12_2016_6p43.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale13_2016_1p98.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale16_2016_3p04.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale18_2016_4p41.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale2_2016_0p05.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale21_2016_2p70.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale24_2016_1p48.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale26_2016_2p16.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale3_2016_0p00.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale30_2016_3p21.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale32_2016_0p12.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale34_2016_2p13.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale38_2016_1p81.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale4_2016_0p60.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale42_2016_0p20.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale5_2016_0p01.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale6_2016_1p13.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale8_2016_4p83.json",
                 "HLT_Photon75_R9Id90_HE10_IsoM_prescale9_2016_0p22.json"]
HLT_Photon90  = ["HLT_Photon90_R9Id90_HE10_IsoM_prescale1_2016_2p21.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale10_2016_2p70.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale12_2016_1p48.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale13_2016_2p16.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale15_2016_3p21.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale16_2016_0p12.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale17_2016_2p13.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale19_2016_1p81.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale2_2016_0p60.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale21_2016_0p20.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale3_2016_1p14.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale4_2016_5p47.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale5_2016_0p22.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale6_2016_5p79.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale7_2016_1p98.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale8_2016_3p04.json",
                 "HLT_Photon90_R9Id90_HE10_IsoM_prescale9_2016_4p41.json"]
HLT_Photon120 = ["HLT_Photon120_R9Id90_HE10_IsoM_prescale1_2016_3p42.json",
                 "HLT_Photon120_R9Id90_HE10_IsoM_prescale2_2016_16p28.json",
                 "HLT_Photon120_R9Id90_HE10_IsoM_prescale3_2016_7p10.json",
                 "HLT_Photon120_R9Id90_HE10_IsoM_prescale4_2016_3p64.json",
                 "HLT_Photon120_R9Id90_HE10_IsoM_prescale5_2016_3p21.json",
                 "HLT_Photon120_R9Id90_HE10_IsoM_prescale6_2016_3p95.json",
                 "HLT_Photon120_R9Id90_HE10_IsoM_prescale7_2016_0p20.json",
                 "HLT_Photon120_R9Id90_HE10_IsoM_prescale8_2016_0p12.json"]
golden = ["Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"]

trigger_name = (HLT_Photon50,"HLT_Photon50")
prescale = trigger_name[0] 
trig1 = prescale[0]
trig_list = prescale
trig_list.remove(trig1)
afs_dir = "/afs/cern.ch/user/m/myalvac/GPlusbJets/"
cert_json1 = afs_dir+"json/prescale_jsons/"+trig1
data1 = json.load(open(cert_json1))
run_number1 = data1.keys()
#Run_dict = {}
for run in run_number1:
	lumi_blocks1 = data1[run]
	set1_list = set([])
	for lumi1 in lumi_blocks1:
		lumi1_list = [x for x in range(lumi1[0],lumi1[1]+1)]
		set1 = set(lumi1_list)
		set1_list.update(set1)
	set_list = set([])
	for trig in trig_list:
		cert_jsonp = afs_dir+"json/prescale_jsons/"+trig
		data = json.load(open(cert_jsonp))
		if not run in data.keys() : continue
		lumi_blocks = data[run]
		for lumi in lumi_blocks:
			lumi_list = [x for x in range(lumi[0],lumi[1]+1)]
			set_ = set(lumi_list)
			set_list.update(set_)
	print(run,list(set1_list-set_list))
#	Run_dict[run]=list(set1_list-set_list)
#pickle.dump(Run_dict, open(afs_dir+"json/prescale_jsons/pickles/"+trigger_name[1]+"_prescale1.pkl", "wb"))
