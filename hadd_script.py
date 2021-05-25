import pickle
import os
pfile="/afs/cern.ch/user/m/myalvac/GPlusbJets/samples_orig.pkl"
sample_dic = pickle.load(open(pfile,'rb'))
sdict = sample_dic[2016]["data"]["SinglePhoton"]["H"]
slist = os.listdir(sdict["dir"])
hadd_target_dir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/merged_HLT_120/"
hadd_orig_dir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016H_02Apr2020-v1/"
for s in slist:
	print("hadd -f "+hadd_target_dir+"HLT_Photon120_R9Id90_HE10_IsoM_"+s+" "+hadd_orig_dir+"HLT_Photon120_R9Id90_HE10_IsoM_prescale"+"*"+s.split(".root")[0]+"*"+".root")

