import pickle
import os

pfile=os.environ["afs_dir"]+"/samples_orig.pkl"
#pfile="/afs/cern.ch/work/e/ecasilar/GplusbJets/samples_ana.pkl"

sample_dic = pickle.load(open(pfile,'rb'))
#sname = "G1Jet_Pt"
#sname = "QCD_HT"
sname = "SingleMuon"
#stype = "bkg"
#stype = "signal"
stype = "data"
sdict = sample_dic[2016][stype][sname]

for ci,bin_name in enumerate(sdict.keys()):
	#if not "_NOExt" in bin_name: continue
	cur_dir = sdict[bin_name]["dir"]
	#print(cur_dir)
	flist = os.listdir(cur_dir)
	if stype=="data":
		#print(os.environ["cern_box"]+"/data/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/")
		if not os.path.exists(os.environ["cern_box"]+"/data/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/"):
			os.makedirs(os.environ["cern_box"]+"/data/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/")
	else:
		#print(os.environ["cern_box"]+"/MC/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		if not os.path.exists(os.environ["cern_box"]+"/MC/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"):
			os.makedirs(os.environ["cern_box"]+"/MC/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")

	for f in flist:
		print("python "+os.environ["afs_dir"]+"analyse.py --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --filename="+f)
