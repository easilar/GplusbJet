import ROOT
import pickle
import os, sys
import warnings
import numpy as np
pfile=os.environ["afs_dir"]+"/samples_orig.pkl"

sample_dic = pickle.load(open(pfile,'rb'))
year = 2016
#year = 2017
#year = 2018
stype = "data"
sname = "SinglePhoton"
if sname == "SinglePhoton":
        #sname = "SingleMuon"
	target_filename_dict={"HLT_Photon36_2016.sh":("HLT_Photon36_R9Id90_HE10_IsoM_prescale1_2016_36p12.json","HLT_Photon36_R9Id90_HE10_IsoM_prescale2_2016_0p40.json","HLT_Photon36_R9Id90_HE10_IsoM_prescale25_2016_0p04.json"),\
"HLT_Photon50_2016.sh":("HLT_Photon50_R9Id90_HE10_IsoM_prescale1_2016_2p20.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale10_2016_0p04.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale104_2016_2p70.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale120_2016_1p47.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale125_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale13_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale130_2016_2p16.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale150_2016_3p21.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale160_2016_0p12.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale170_2016_2p13.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale189_2016_1p81.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale20_2016_0p60.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale209_2016_0p20.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale26_2016_0p01.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale3_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale30_2016_1p13.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale46_2016_0p22.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale48_2016_5p47.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale5_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale60_2016_5p79.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale65_2016_1p98.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale7_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale80_2016_3p04.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale9_2016_0p01.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale91_2016_4p41.json"),\
"HLT_Photon75_2016.sh":("HLT_Photon75_R9Id90_HE10_IsoM_prescale1_2016_2p20.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale12_2016_6p43.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale13_2016_1p98.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale16_2016_3p04.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale18_2016_4p41.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale2_2016_0p05.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale21_2016_2p70.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale24_2016_1p48.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale26_2016_2p16.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale3_2016_0p00.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale30_2016_3p21.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale32_2016_0p12.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale34_2016_2p13.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale38_2016_1p81.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale4_2016_0p60.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale42_2016_0p20.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale5_2016_0p01.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale6_2016_1p13.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale8_2016_4p83.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale9_2016_0p22.json"),\
"HLT_Photon90_2016.sh":("HLT_Photon90_R9Id90_HE10_IsoM_prescale1_2016_2p21.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale10_2016_2p70.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale12_2016_1p48.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale13_2016_2p16.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale15_2016_3p21.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale16_2016_0p12.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale17_2016_2p13.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale19_2016_1p81.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale2_2016_0p60.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale21_2016_0p20.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale3_2016_1p14.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale4_2016_5p47.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale5_2016_0p22.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale6_2016_5p79.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale7_2016_1p98.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale8_2016_3p04.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale9_2016_4p41.json"),\
"HLT_Photon120_2016.sh":("HLT_Photon120_R9Id90_HE10_IsoM_prescale1_2016_3p42.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale2_2016_16p28.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale3_2016_7p10.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale4_2016_3p64.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale5_2016_3p21.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale6_2016_3p95.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale7_2016_0p20.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale8_2016_0p12.json"),\
"HLT_Photon165_2016.sh":("HLT_Photon165_R9Id90_HE10_IsoM_prescale1_2016_36p52.json",)\
#"HLT_Photon175_2016.sh":("HLT_Photon175_prescale1_2016_36p52.json",)\
}
if sname == "SingleMuon":
	target_filename_dict={"HLT_Muon36_2016.sh":("HLT_Photon36_R9Id90_HE10_IsoM_prescale1_2016_36p12.json","HLT_Photon36_R9Id90_HE10_IsoM_prescale2_2016_0p40.json","HLT_Photon36_R9Id90_HE10_IsoM_prescale25_2016_0p04.json"),\
"HLT_Muon50_2016.sh":("HLT_Photon50_R9Id90_HE10_IsoM_prescale1_2016_2p20.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale10_2016_0p04.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale104_2016_2p70.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale120_2016_1p47.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale125_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale13_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale130_2016_2p16.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale150_2016_3p21.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale160_2016_0p12.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale170_2016_2p13.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale189_2016_1p81.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale20_2016_0p60.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale209_2016_0p20.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale26_2016_0p01.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale3_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale30_2016_1p13.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale46_2016_0p22.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale48_2016_5p47.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale5_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale60_2016_5p79.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale65_2016_1p98.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale7_2016_0p00.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale80_2016_3p04.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale9_2016_0p01.json", "HLT_Photon50_R9Id90_HE10_IsoM_prescale91_2016_4p41.json"),\
"HLT_Muon75_2016.sh":("HLT_Photon75_R9Id90_HE10_IsoM_prescale1_2016_2p20.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale12_2016_6p43.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale13_2016_1p98.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale16_2016_3p04.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale18_2016_4p41.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale2_2016_0p05.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale21_2016_2p70.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale24_2016_1p48.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale26_2016_2p16.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale3_2016_0p00.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale30_2016_3p21.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale32_2016_0p12.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale34_2016_2p13.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale38_2016_1p81.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale4_2016_0p60.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale42_2016_0p20.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale5_2016_0p01.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale6_2016_1p13.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale8_2016_4p83.json","HLT_Photon75_R9Id90_HE10_IsoM_prescale9_2016_0p22.json"),\
"HLT_Muon90_2016.sh":("HLT_Photon90_R9Id90_HE10_IsoM_prescale1_2016_2p21.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale10_2016_2p70.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale12_2016_1p48.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale13_2016_2p16.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale15_2016_3p21.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale16_2016_0p12.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale17_2016_2p13.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale19_2016_1p81.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale2_2016_0p60.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale21_2016_0p20.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale3_2016_1p14.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale4_2016_5p47.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale5_2016_0p22.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale6_2016_5p79.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale7_2016_1p98.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale8_2016_3p04.json","HLT_Photon90_R9Id90_HE10_IsoM_prescale9_2016_4p41.json"),\
"HLT_Muon120_2016.sh":("HLT_Photon120_R9Id90_HE10_IsoM_prescale1_2016_3p42.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale2_2016_16p28.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale3_2016_7p10.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale4_2016_3p64.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale5_2016_3p21.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale6_2016_3p95.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale7_2016_0p20.json","HLT_Photon120_R9Id90_HE10_IsoM_prescale8_2016_0p12.json"),\
"HLT_Muon165_2016.sh":("HLT_Photon165_R9Id90_HE10_IsoM_prescale1_2016_36p52.json",)\
#"HLT_Muon175_2016.sh":("HLT_Photon175_prescale1_2016_36p52.json",)\
}
sdict = sample_dic[year][stype][sname]
targetdir_mainpath = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/"
targetdir_suffix = "Low_PT"
ndiv=10
for target_filename in  target_filename_dict.keys():
        writing_file = open(target_filename, "a")
        for trigger in target_filename_dict[target_filename]:
                for ci,bin_name in enumerate(sdict.keys()):
			targetdir = targetdir_mainpath+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"
                        cur_dir = sdict[bin_name]["dir"]
                        flist = os.listdir(cur_dir)
                        for f in flist:
                                for indiv in range(ndiv+1):
					targetfilename = targetdir+trigger.split("prescale")[0]+trigger.split("_")[-3]+"_"+f.split(".")[0]+"_"+str(indiv)+".root"
					if not os.path.isfile(targetfilename):
						print("# File does not exist")
						print("python "+os.environ["afs_dir"]+"analyse_trigger.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --trigname="+trigger+" --filename="+f+"\n")
					
					else :
						if os.path.getsize(targetfilename)/1024<90:
						
							print("# File exist but empty")
							print("python "+os.environ["afs_dir"]+"analyse_trigger.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --trigname="+trigger+" --filename="+f+"\n")
							
						else:
								#rootfilename = ROOT.TFile(targetfilename,'r')
								mfile = ROOT.TFile(targetfilename)
								if mfile.IsZombie():
									print("# File exist but not proper")
									print("python "+os.environ["afs_dir"]+"analyse_trigger.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --trigname="+trigger+" --filename="+f+"\n")
								#warnings.filterwarnings("error", "RuntimeWarning")
								#except RuntimeWarning:
