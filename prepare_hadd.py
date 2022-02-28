import pickle
import os

pfile=os.environ["afs_dir"]+"/samples_orig.pkl"

sample_dic = pickle.load(open(pfile,'rb'))
year = 2017
sname = "SinglePhoton_UL"
stype =  "data" #"signal" #"bkg",  "data"
sdict = sample_dic[year][stype][sname]
ndiv=0
targetdir_suffix = "High_PT_Tight"
for ci,bin_name in enumerate(sdict.keys()):
	cur_dir = sdict[bin_name]["dir"]
	flist = os.listdir(cur_dir)
	if stype=="data":

		if not os.path.exists(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"):
			os.makedirs(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		print("cd "+os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		print("mkdir hadd")
	else:
		if not os.path.exists(os.environ["cern_box"]+"/MC/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"):
			os.makedirs(os.environ["cern_box"]+"/MC/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		print("cd "+os.environ["cern_box"]+"/MC/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		print("mkdir hadd")
	for f in flist:
		for indiv in range(ndiv+1):
			print("hadd hadd/"+f+" "+f.split(".root")[0]+"*.root")
