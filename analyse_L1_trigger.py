import ROOT
import json
import os
import pickle
import operator
from helper import deltaR
from configure import *

from ROOT import TFile, TTree, gRandom
from array import array

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--year", dest="year", default="2016", action="store", help="can be 2016,2017,2018")
parser.add_option("--sname", dest="sname", default="SinglePhoton", action="store", help="can be QCD , GJets_Pt ... ")
parser.add_option("--stype", dest="stype", default="data", action="store", help="can be data or signal or bkg")
parser.add_option("--letter", dest="letter", default="B", action="store", help="if data can be B,C,D,E,F,G,H;if signal GJets_Pt_100To200")
parser.add_option("--filename", dest="filename", default="sample.root", action="store", help="should be the individual root file name")
parser.add_option("--ndiv", dest="ndiv", default="1", action="store", help="number of divitions for one root file")
parser.add_option("--divIndex", dest="divIndex", default="0", action="store", help="index of divitions for one root file")
parser.add_option("--trigname", dest="trigname", default="HLT_Photon36_R9Id90_HE10_IsoM_prescale1_2016_36p12.json", action="store", help="can be any json file from Json directory")
(options, args) = parser.parse_args()

data_letter = options.letter
f = options.filename
exec("year="+options.year)
exec("ndiv="+options.ndiv)
exec("divIndex="+options.divIndex)
stype = options.stype
sname = options.sname
trigname = options.trigname

afs_dir = "/afs/cern.ch/user/m/myalvac/GPlusbJets/"
targetdir_mainpath = "/eos/user/m/myalvac/GPlusBJets/HLT_36_L1_Prescaled/"
pfile = afs_dir+"/samples_ana.pkl"
sample_dic = pickle.load(open(pfile,'rb'))
sdict = sample_dic[year][stype][sname][data_letter]
print("Trigname:",trigname)
cert_json = afs_dir+"json/prescale_jsons/L1/"+trigname
if ".pkl" in cert_json :
	eff_lumi = 2.20
	print("eff_Lumi:",eff_lumi)
else : 
	split_name = trigname.split("_")[-1]
	#print(split_name)
	eff_lumi = split_name.split(".")[0]
	print("eff_Lumi:",eff_lumi)
	eff_lumi = eff_lumi.replace("p",".")
	eff_lumi = float(eff_lumi)
	print("eff_Lumi:",eff_lumi)
#orig_dir = "/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/data_lumiapplied_HLT_Photon175_MetFilters/SinglePhoton/Run2016"+data_letter+"_02Apr2020-v1/"
if year == 2016:
   act_Lumi = 36.47
   trigger_list = ["HLT_Photon36_R9Id90_HE10_IsoM","HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM"]
   offline_pt_dict = {"HLT_Photon36_R9Id90_HE10_IsoM":(40,60),"HLT_Photon50_R9Id90_HE10_IsoM":(60,90),"HLT_Photon75_R9Id90_HE10_IsoM":(90,100),"HLT_Photon90_R9Id90_HE10_IsoM":(100,145),"HLT_Photon120_R9Id90_HE10_IsoM":(145,180),"HLT_Photon165_R9Id90_HE10_IsoM":(180,225)}

   #cert_json = afs_dir+"/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
   print("working on 2016")
elif year == 2017:
   act_Lumi = 41.54
   trigger_list = ["HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon200"]
   offline_pt_dict = {"HLT_Photon50_R9Id90_HE10_IsoM":(60,90),"HLT_Photon75_R9Id90_HE10_IsoM":(90,100),"HLT_Photon90_R9Id90_HE10_IsoM":(100,145),"HLT_Photon120_R9Id90_HE10_IsoM":(145,180),"HLT_Photon165_R9Id90_HE10_IsoM":(180,225),"HLT_Photon200":(225,2000)}
   #cert_json = afs_dir+"/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
   print("working on 2017")
elif year == 2018:
   act_Lumi = 59.96
   trigger_list = ["HLT_Photon50_R9Id90_HE10_IsoM","HLT_Photon75_R9Id90_HE10_IsoM","HLT_Photon90_R9Id90_HE10_IsoM","HLT_Photon120_R9Id90_HE10_IsoM","HLT_Photon165_R9Id90_HE10_IsoM","HLT_Photon200"]
   offline_pt_dict = {"HLT_Photon50_R9Id90_HE10_IsoM":(60,90),"HLT_Photon75_R9Id90_HE10_IsoM":(90,100),"HLT_Photon90_R9Id90_HE10_IsoM":(100,145),"HLT_Photon120_R9Id90_HE10_IsoM":(145,180),"HLT_Photon165_R9Id90_HE10_IsoM":(180,225),"HLT_Photon200":(225,2000)}
   #cert_json = afs_dir+"/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"   
   print("working on 2018")
targetdir_suffix = "Low_PT"
orig_dir = sdict["dir"]+"/"
targetdir = targetdir_mainpath+"/L1_Prescaled/data/"+str(year)+"/"+sname+"/"+targetdir_suffix+"/"+sdict["dir"].split("/")[-2]+"/"
if ".pkl" in cert_json : 
	data = pickle.load(open(cert_json,'rb'))
else:
	data = json.load(open(cert_json))
print("Working on data ",data_letter)

targetfilePath = targetdir+trigname.split("prescale")[0]+trigname.split("_")[-3]+"_"+f.split(".")[0]+".root"
origFilePath = orig_dir+f
print("Target path:" , targetfilePath)
ch = ROOT.TChain("Events")
ch.Add(origFilePath)
number_events = ch.GetEntries()
nEventsPerChunk = number_events/float(ndiv)
print(nEventsPerChunk)
ini_event = divIndex*int(nEventsPerChunk)
fin_event = min((divIndex+1)*int(nEventsPerChunk),number_events)
print(ini_event,fin_event)
print(" Creating new root-file ...")
newFile = ROOT.TFile(targetfilePath,"recreate")
print(" Creating new tree ...")
newchain = ch.CloneTree(0)
tree = newchain.GetTree()

weight_trig_L1_Photon36  = array('f',[0])
tree.Branch("weight_trig_L1_Photon36",weight_trig_L1_Photon36 ,"weight_trig_L1_Photon36/F")

print("number of events:",number_events)
weight_v=-999.
for jentry in range(ini_event,fin_event):
   ch.GetEntry(jentry)
   run = ch.GetLeaf('run').GetValue()
   event = ch.GetLeaf('event').GetValue()
   lumi = ch.GetLeaf('luminosityBlock').GetValue()
   weight_HLT_36 = ch.GetLeaf('weight_trig_HLT_Photon36').GetValue()
   if (jentry%50000 == 0) : print(jentry,run,lumi)
   if options.stype == "data":
  	if eff_lumi <= 0.00: continue
				
	###L1 Starts###
	if not str(int(run)) in data.keys(): continue
	if str(int(run)) in data.keys():
		if not ".pkl" in cert_json : 
			for lumiBlock in data[str(int(run))]:
				if (lumi >= lumiBlock[0] and lumi <= lumiBlock[1] ) :
					weight_v = float(trigname.split("_")[-3].split("prescale")[1])
					print("weight_v : ", weight_v)
		else: 
			for lumiBlock in data[str(int(run))]:
				if lumi == lumiBlock :
					weight_v = 1
					print("PRESCLAE1 from pkl", weight_v)
   weight_trig_L1_Photon36[0] = weight_v
   tree.Fill()			
    

newFile.cd()
tree.Write()
newFile.Write()
newFile.Close()
print("CIMBOM")
