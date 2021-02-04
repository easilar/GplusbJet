import pickle
import os

pfile="/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_orig.pkl"

sample_dic = pickle.load(open(pfile,'rb'))
#sname = "G1Jet_Pt"
sname = "SingleMuon"
#stype = "signal"
stype = "data"
sdict = sample_dic[2016][stype][sname]

for ci,bin_name in enumerate(sdict.keys()):
	cur_dir = sdict[bin_name]["dir"]
	flist = os.listdir(cur_dir)
	for f in flist:
		print("python /afs/cern.ch/work/e/ecasilar/GplusbJets/analyse.py --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --filename="+f)
