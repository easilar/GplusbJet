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
#if sname == "SinglePhoton":
#if sname == "SingleMuon":

sdict = sample_dic[year][stype][sname]
targetdir_mainpath = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/"
#targetdir_suffix = "Low_PT"
targetdir_suffix = "High_PT_LooseNotTight"
ndiv=40
#for target_filename in  target_filename_dict.keys():
#writing_file = open(target_filename, "a")
writing_file = open("TEST.sh", "a")
#for trigger in target_filename_dict[target_filename]:
for ci,bin_name in enumerate(sdict.keys()):
	targetdir = targetdir_mainpath+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"
	print(targetdir)
	if "Run2016C" in targetdir: continue
	if "Run2016B" in targetdir: continue
	
        cur_dir = sdict[bin_name]["dir"]
        flist = os.listdir(cur_dir)
        for f in flist:
                for indiv in range(ndiv+1):
			#targetfilename = targetdir+trigger.split("prescale")[0]+trigger.split("_")[-3]+"_"+f.split(".")[0]+"_"+str(indiv)+".root"
			targetfilename = targetdir+f.split(".")[0]+"_"+str(indiv)+".root"
			if not os.path.isfile(targetfilename):
				print("# File does not exist")
				#print("python "+os.environ["afs_dir"]+"analyse_trigger.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --trigname="+trigger+" --filename="+f+"\n")
				print("python "+os.environ["afs_dir"]+"analyse.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --filename="+f)
			else :
				if os.path.getsize(targetfilename)/1024<80:
					print("# File exist but empty")
					#print("python "+os.environ["afs_dir"]+"analyse_trigger.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --trigname="+trigger+" --filename="+f+"\n")
					print("python "+os.environ["afs_dir"]+"analyse.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --filename="+f)
					
				else:
						#rootfilename = ROOT.TFile(targetfilename,'r')
						mfile = ROOT.TFile(targetfilename)
						if mfile.IsZombie():
							print("# File exist but not proper")
							#print("python "+os.environ["afs_dir"]+"analyse_trigger.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --trigname="+trigger+" --filename="+f+"\n")
							print("python "+os.environ["afs_dir"]+"analyse.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --filename="+f)
						#warnings.filterwarnings("error", "RuntimeWarning")
						#except RuntimeWarning:
