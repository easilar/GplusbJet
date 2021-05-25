import pickle
import os

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--letter", dest="letter", default="B", action="store", help="can be B , C, .....")
parser.add_option("--trig_num", dest="trig_num", default="120", action="store", help="can be 120 ,50,75....")
(options, args) = parser.parse_args()

letter = options.letter
trig_num = options.trig_num

pfile=pfile=os.environ["afs_dir"]+"/samples_orig.pkl"
sample_dic = pickle.load(open(pfile,'rb'))
sdict = sample_dic[2016]["data"]["SinglePhoton"][letter]
slist = os.listdir(sdict["dir"])
hadd_target_dir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016"+letter+"_02Apr2020-v1/merged_HLT_"+trig_num+"/"
hadd_orig_dir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data/2016/SinglePhoton/Low_PT/Run2016"+letter+"_02Apr2020-v1/"
for s in slist:
	print("hadd -f "+hadd_target_dir+"HLT_Photon"+trig_num+"_R9Id90_HE10_IsoM_"+s+" "+hadd_orig_dir+"HLT_Photon"+trig_num+"_R9Id90_HE10_IsoM_prescale"+"*"+s.split(".root")[0]+"*"+".root")

