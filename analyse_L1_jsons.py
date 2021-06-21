import json
import pickle

HLT_Photon36  = ["HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale1_2016_2p20.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale0_2016_0p00.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale10_2016_0p00.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale100_2016_1p98.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale120_2016_5p47.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale15_2016_0p01.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale150_2016_4p41.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale170_2016_2p70.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale180_2016_5p68.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale20_2016_0p00.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale210_2016_5p32.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale250_2016_0p61.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale300_2016_3p73.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale350_2016_2p52.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale4_2016_0p00.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale40_2016_0p01.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale400_2016_1p32.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale450_2016_0p62.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale50_2016_0p55.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale500_2016_0p20.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale550_2016_0p00.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale8_2016_0p00.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale80_2016_0p22.json",
		 "HLT_Photon36_R9Id90_HE10_IsoM_L1_prescale90_2016_1p13.json"]

trigger_name = (HLT_Photon36,"HLT_Photon36")
prescale = trigger_name[0] 
trig1 = prescale[0]
trig_list = prescale
trig_list.remove(trig1)
afs_dir = "/afs/cern.ch/user/m/myalvac/GPlusbJets/"
cert_json1 = afs_dir+"json/prescale_jsons/L1/"+trig1
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
		cert_jsonp = afs_dir+"json/prescale_jsons/L1/"+trig
		data = json.load(open(cert_jsonp))
		if not run in data.keys() : continue
		lumi_blocks = data[run]
		for lumi in lumi_blocks:
			lumi_list = [x for x in range(lumi[0],lumi[1]+1)]
			set_ = set(lumi_list)
			set_list.update(set_)
	print(run,list(set1_list-set_list))
	#Run_dict[run]=list(set1_list-set_list)
#pickle.dump(Run_dict, open(afs_dir+"json/prescale_jsons/L1/"+trigger_name[1]+"_prescale1.pkl", "wb"))
