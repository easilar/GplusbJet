import pickle
import os

pfile=os.environ["afs_dir"]+"/samples_orig.pkl"
#pfile="/afs/cern.ch/user/m/myalvac/GPlusbJets/samples_orig.pkl"

sample_dic = pickle.load(open(pfile,'rb'))
#year = 2016
#year = 2017
year = 2018
#sname = "G1Jet_Pt"
#sname = "QCD_HT"
sname = "SingleMuon"
#sname = "SingleMuon_18"
#stype = "bkg"
#stype = "signal"
stype = "data"
sdict = sample_dic[year][stype][sname]

for ci,bin_name in enumerate(sdict.keys()):
	#if not "_NOExt" in bin_name: continue
	cur_dir = sdict[bin_name]["dir"]
	#print(cur_dir)
	flist = os.listdir(cur_dir)
	if stype=="data":
		#print(os.environ["cern_box"]+"/data/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/")
		if not os.path.exists(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/"):
			os.makedirs(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-1]+"/")
	else:
		#print(os.environ["cern_box"]+"/MC/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
		if not os.path.exists(os.environ["cern_box"]+"/MC/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"):
			os.makedirs(os.environ["cern_box"]+"/MC/"+sname+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")

	for f in flist:
		print("python "+os.environ["afs_dir"]+"analyse.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --filename="+f)
