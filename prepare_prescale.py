import pickle
import os
from prepare_dict import *

pfile=os.environ["afs_dir"]+"/samples_orig.pkl"

sample_dic = pickle.load(open(pfile,'rb'))
year = 2016
stype = "data"
sname = "SinglePhoton"
if year == 2016: target_filename_dict = target_filename_dict_2016
elif year == 2017: target_filename_dict = target_filename_dict_2017
elif year == 2018: target_filename_dict = target_filename_dict_2018

sdict = sample_dic[year][stype][sname]
targetdir_suffix = "Low_PT"
ndiv=10
for target_filename in  target_filename_dict.keys():
	print(target_filename)
	writing_file = open(target_filename, "a")
	for trigger in target_filename_dict[target_filename]:
		for ci,bin_name in enumerate(sdict.keys()):
			cur_dir = sdict[bin_name]["dir"]
			flist = os.listdir(cur_dir)
			if not os.path.exists(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/"):
				os.makedirs(os.environ["cern_box"]+"/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict[bin_name]["dir"].split("/")[-2]+"/")
			for f in flist:
				for indiv in range(ndiv+1):
					new_line="python "+os.environ["afs_dir"]+"analyse_trigger.py --year="+str(year)+" --sname="+sname+" --stype="+stype+" --letter="+bin_name+" --ndiv="+str(ndiv)+" --divIndex="+str(indiv)+" --trigname="+trigger+" --filename="+f+"\n"
					writing_file.write(new_line)
        writing_file.close()
