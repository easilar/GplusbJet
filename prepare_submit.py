import pickle
import os

pfile=os.environ["afs_dir"]+"/samples_orig.pkl"

sample_dic = pickle.load(open(pfile,'rb'))
year = 2016
#year = 2017
#year = 2018
sname = "G1Jet_Pt"
#sname = "QCD_HT"
#sname = "SinglePhoton"
#sname = "SingleMuon_18"
#stype = "bkg"
stype = "signal"
#stype = "data"
sdict = sample_dic[year][stype][sname]
ndiv=5
#targetdir_suffix = "High_PT_LooseNotTight"
targetdir_suffix = "High_PT_Tight"
for ci,bin_name in enumerate(sdict.keys()):
	#if not "_NOExt" in bin_name: continue
	cur_dir = sdict[bin_name]["dir"]
	#print(cur_dir)
	flist = os.listdir(cur_dir)
	if stype=="data":
		#print(os.environ["cern_box"]+"/data/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/")
		if not os.path.exists(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/"):
			os.makedirs(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/")
	else:
		#print(os.environ["cern_box"]+"/MC/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		if not os.path.exists(os.environ["cern_box"]+"/MC/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"):
			os.makedirs(os.environ["cern_box"]+"/MC/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")

	for f in flist:
		for indiv in range(ndiv+1):
			print("python "+os.environ["afs_dir"]+"analyse.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --filename="+f)
