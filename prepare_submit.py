import pickle
import os

pfile=os.environ["afs_dir"]+"/samples_orig.pkl"

sample_dic = pickle.load(open(pfile,'rb'))

year = 2018
sname = "GJets_DR_0p4_HT"
stype =  "bkg" #"bkg","signal",  "data"
sdict = sample_dic[year][stype][sname]
ndiv=20
targetdir_suffix = "High_PT_Tight"
for ci,bin_name in enumerate(sdict.keys()):
	cur_dir = sdict[bin_name]
	flist = os.listdir(cur_dir)
	if stype=="data":

		#print(os.environ["cern_box"]+"/data/"+sname+"/"+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		if not os.path.exists(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"):
			os.makedirs(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
	else:
		#print(os.environ["cern_box"]+"/MC/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		if not os.path.exists(os.environ["cern_box"]+"/MC/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"):
			os.makedirs(os.environ["cern_box"]+"/MC/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/")

	for f in flist:
		for indiv in range(ndiv+1):
			print("python "+os.environ["afs_dir"]+"analyse.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --filename="+f)
