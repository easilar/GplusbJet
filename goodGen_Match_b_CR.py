import ROOT
import helper
from helper import *
import csv
import json
import os
import pickle
import operator
from helper import deltaR , matching
from configure import *
from ROOT import TFile, TTree, gRandom
from array import array
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--sname", dest="sname", default="G1Jet_Pt", action="store", help="can be QCD , GJets_Pt ... ")
parser.add_option("--stype", dest="stype", default="signal", action="store", help="can be data or signal or bkg")
parser.add_option("--ndiv", dest="ndiv", default="42", action="store", help="number of divitions for one root file")
parser.add_option("--divIndex", dest="divIndex", default="0", action="store", help="index of divitions for one root file")
parser.add_option("--year", dest="year", default="2016", action="store", help="can be 2016,2017,2018")
(options, args) = parser.parse_args()
exec("ndiv="+options.ndiv)
exec("divIndex="+options.divIndex)
exec("year="+options.year)
stype = options.stype
sname = options.sname
year = options.year

pfile = "samples_ana.pkl"
sample_dic = pickle.load(open(pfile,'rb'))
mychain_dict  =  getChain(year=2016, stype=stype, sname=sname, pfile=pfile, datatype='all', test=False)

ch = mychain_dict[0]

CR = "goodPhoton_hoe>0.03"
SR = "goodPhoton_hoe<=0.03"

if stype == "signal" and (sname == "G1Jet_Pt" or sname == "CR_G1Jet_Pt") :
	ch.Draw(">>eList", "goodPhoton_hoe>0.03&&(ngoodbJet==1||ngoodbJet==0)&&ngoodPhoton==1&&(abs(goodGenPhoton_pt-goodPhoton_pt)/goodPhoton_pt<0.1)") # Apply ROOT cuts here
 	elist = ROOT.gDirectory.Get("eList")
 	number_events = elist.GetN()
	#number_events = 1000
if stype == "bkg" and (sname == "QCD_HT" or sname == "CR_QCD_HT") :
        ch.Draw(">>eList", "goodPhoton_hoe>0.03&&(ngoodbJet==1||ngoodbJet==0)&&ngoodPhoton==1&&ngoodGenPhoton==0") # Apply ROOT cuts here
        elist = ROOT.gDirectory.Get("eList")
        number_events = elist.GetN()
	#number_events = 1000

nEventsPerChunk = number_events/float(ndiv)
ini_event = divIndex*int(nEventsPerChunk)
fin_event = min((divIndex+1)*int(nEventsPerChunk),number_events)

#Number of Particles in n events
Nph=set()  # N Photons per Event in goodPhotons
Nbj=set()
Nj=set()
NGbj=set()

#List of Variables for The dataset

NPhotons=[] # NPhotons before Matching
nPhotons=[] # nPhotons after Matching
nGPhotons=[] # nGenPhotons after Matching 
GPhotons=[] # List of GenPhotns variables
RGPhotons=[] # list of 'Raw' GenPhotons before Matching
RRPhotons=[] # List of Photons before matching
Sel_photons=[] # List of Photons after Matching

nJets=[] # nJets after selection
Sel_jets=[] # Lead Jets after selection
Sublead_jets=[]	# SubLead Jets after Selection

nbJets=[] # 1/2 nbJets before Matching 
Sel_bjets=[] # Lead bJets after Matching 
SubLead_bJets=[] # SubLead bJets after Matching
RLead_bJets=[] # Lead bJets before Matching 
RSubLead_bJets=[] # SubLead bJets before Matching

Gbjets=[] # Lead GenbJets after Matching
SubLead_GbJets=[] # SubLead GenbJets after Matching
RGbjets=[] # Lead GenbJets before Matching
RSubLead_GbJets=[] # SubLead GenbJets before Matching 

HT=[]
nPVs=[]
PVs=[]
nSVs=[]
SVs=[]
Met_pt=[] # Met_pt after Matching
Met_phi=[]

dPhi= []
dPhi_b= []

DRm=[]
dR_GJet_lead = []
dR_GJet_sublead = []
Labels=[]
#Match_ph=[]
Match_1b=[] # 1b Jets after Matching
Match_2b=[] # 2b Jets after Matching
Number_b=0. # Number 1/2b before Matching
M_1b=0. # N 1b after
M_2b=0. # N 2b after
npho=0. # N Pho After 
#M_ph=0.
Npho=0. # N Pho  before
#Npho1=0.
#Npho2=0.
count_events_num=0
count_events_den=0
#--------- First loop : Looping on Events ---------

for jentry in range(ini_event,fin_event):
	#ch.GetEntry(jentry)
	ch.GetEntry(elist.GetEntry(jentry))

	good_event_Photon=False
	good_event_b=False
	good_event_2b=False

   	nGenPhoton=ch.GetLeaf('ngoodGenPhoton').GetValue() # nGen Particles in one event#float
   	nGenJet=ch.GetLeaf('nGenJet').GetValue() # nGen Particles in one event
   	nPhoton = ch.GetLeaf('ngoodPhoton').GetValue() # nReco Photon inside one event
   	nJet = ch.GetLeaf('ngoodJet').GetValue() # nReco Jets inside one event
   	nbJet = ch.GetLeaf('ngoodbJet').GetValue() # nReco Jets inside one event
   	met_pt=ch.GetLeaf('MET_pt').GetValue()
   	met_phi=ch.GetLeaf('MET_phi').GetValue()
	nPV=ch.GetLeaf('PV_npvsGood').GetValue()
	nSV=ch.GetLeaf('nSV').GetValue()
	Nph.add(nPhoton)
   	Nbj.add(nbJet)
   	Nj.add(nJet)
	
		

	#if nPhoton != 1 or nGenPhoton  != 1 or nbJet != 0 : continue     # add control plotter cuts

	#count_events_den += 1 # All 1 Photon 1 /2 bJet Events

	#lists of variables per event
	Photons=[]          # kin of Reco Photons
   	Jets=[]             # kin of Reco Jets
   	GenJets=[]              # kin of G jets
	GenbJets=[]
   	GenPhotons=[]           # kin of Gen Particles
   	bJets=[]
	ht=[]
	matched_photons=[]
   	sel_photons=[]
	matched_jets_1b=[]
	matched_jets_lb=[]
	matched_jets_slb=[]
	sel_jets_1b=[]
	sel_jets_lb=[]
	sel_jets_slb=[]
	lead_b=[]
	sublead_b=[]
	Glead_b=[]
	Lead_bJets=[]
	subGlead_b=[]
	dRms=[]
	dphi=[]
	dphi_b= []
	labels=[]
	SV=[]
	PV=[]
	count_events_den += 1
       	#nbJets.append({'nbJets':nbJet})
      	NPhotons.append(nPhoton)
	
#---------- second loop : nVariables inside Particles-------------------
	temp_index = 0
	
	for ID in range(int(nGenPhoton)): # Gen Photons   #List of Dict
			GenPhotons.append({'index':temp_index,'orig_index':ID,'pt':ch.GetLeaf('goodGenPhoton_pt').GetValue(ID),'eta':ch.GetLeaf('goodGenPhoton_eta').GetValue(ID),'phi':ch.GetLeaf('goodGenPhoton_phi').GetValue(ID)})
			temp_index += 1

	for I in range(int(nPhoton)): # Reco PHOTONS
			#Looping on ngoodPhotons Make sure that other Variables corresponds to a goodPhoton
			Photons.append({'index':I,'pt':ch.GetLeaf('goodPhoton_pt').GetValue(I),'eta':ch.GetLeaf('goodPhoton_eta').GetValue(I),'phi':ch.GetLeaf('goodPhoton_phi').GetValue(I),'hoe':ch.GetLeaf('goodPhoton_hoe').GetValue(I),'sieie':ch.GetLeaf('goodPhoton_sieie').GetValue(I),'r9':ch.GetLeaf('goodPhoton_r9').GetValue(I),'Iso_all':ch.GetLeaf('goodPhoton_pfRelIso03_all').GetValue(I),'Iso_chg':ch.GetLeaf('goodPhoton_pfRelIso03_chg').GetValue(I)})

	for j in range(int(nJet)): # Reco JETS
        	Jets.append({'index':j,'pt':ch.GetLeaf('goodJet_pt').GetValue(j),'phi':ch.GetLeaf('goodJet_phi').GetValue(j),'eta':ch.GetLeaf('goodJet_eta').GetValue(j)})

        temp_index = 0
        for ID in range(int(nGenJet)): # Gen Jets   #List of Dictionary
                if abs(ch.GetLeaf('GenJet_partonFlavour').GetValue(ID))==5:
                        GenbJets.append({'index':temp_index,'orig_index':ID,'pt':ch.GetLeaf('GenJet_pt').GetValue(ID),'eta':ch.GetLeaf('GenJet_eta').GetValue(ID),'phi':ch.GetLeaf('GenJet_phi').GetValue(ID)})
                        temp_index += 1

	for j in range(int(nbJet)): # Reco  bJets
		bJets.append({'index':j,'pt':ch.GetLeaf('goodbJet_pt').GetValue(j),'phi':ch.GetLeaf('goodbJet_phi').GetValue(j),'eta':ch.GetLeaf('goodbJet_eta').GetValue(j)})

	for P in range(int(nPV)) :
                PV.append({'index':P,'PV_ndof':ch.GetLeaf('PV_ndof').GetValue(P),'PV_x':ch.GetLeaf('PV_x').GetValue(P),'PV_y':ch.GetLeaf('PV_y').GetValue(P),'PV_z':ch.GetLeaf('PV_z').GetValue(P),'PV_chi2':ch.GetLeaf('PV_chi2').GetValue(P),'PV_score':ch.GetLeaf('PV_score').GetValue(P)})

	for S in range(int(nSV)) : 
		SV.append({'index':S,'SV_dlen':ch.GetLeaf('SV_dlen').GetValue(S),'SV_dlenSig':ch.GetLeaf('SV_dlenSig').GetValue(S),'SV_dxy':ch.GetLeaf('SV_dxy').GetValue(S),'SV_dxySig':ch.GetLeaf('SV_dxySig').GetValue(S),'SV_pAngle':ch.GetLeaf('SV_pAngle').GetValue(S),'SV_chi2':ch.GetLeaf('SV_chi2').GetValue(S),'SV_eta':ch.GetLeaf('SV_eta').GetValue(S),'SV_chi2':ch.GetLeaf('SV_chi2').GetValue(S),'SV_phi':ch.GetLeaf('SV_phi').GetValue(S),'SV_pt':ch.GetLeaf('SV_pt').GetValue(S),'SV_ndof':ch.GetLeaf('SV_ndof').GetValue(S)})

	print(' ')
	print('event#',jentry)
   	print('GenPhotons',len(GenPhotons),'Photons',len(Photons),'GenJets' , len(GenJets) ,'Jets',len(Jets),'Gen bJets',len(GenbJets),'bJets' ,len(bJets))
	print(' ')

# ------------PHOTON MATCHING INSIDE CONE dR----------------------------------------------
	
	RRPhotons += Photons
		
    	if  len(Photons)  :
            	sel_photons = Photons
            	good_event_Photon=True
		
	
#-------------- Matching bJets--------------------------------------


        print('#'*10)
        print('GenbJets', len(GenbJets))
        print('bJets',len(bJets))
        print('#'*10)


        if nbJet ==  1 :
                dRmJ=[]
                jet = bJets[0]
                if len(GenbJets) == 0 : continue
                for  j,GenJet in enumerate (GenbJets):
                        dR_Jet_Match = deltaR(jet["phi"],GenJet["phi"],jet["eta"],GenJet["eta"])
                        PtRatioJ=abs(GenJet["pt"]-jet["pt"])/(GenJet["pt"])
                        print('drJ',dR_Jet_Match)
                        print('PtRJ',abs(PtRatioJ))
                        dRmJ.append({'index':GenJet['index'],'dR':dR_Jet_Match,'PtRatio':PtRatioJ})
                        GenJet['PtRatio'] =  PtRatioJ
                        GenJet['dR']    = dR_Jet_Match

                if len(dRmJ) == 0 :continue # in case dRmj is empty due to empty GenbJets
                dRmJ=sorted(dRmJ,key=lambda x:x['dR'])
                print('dRmJ',dRmJ)
                for i in  dRmJ :
                        if abs(i['PtRatio']) < 0.4:
                                jt=[j for j in GenbJets if j['index'] == i['index']][0]
                                matched_jets_1b.append(jt)
                                break
                	else :
                        	continue

                if  len(matched_jets_1b) and matched_jets_1b[0]['dR']  <= 0.5:
                        lead_b=bJets
                if len(GenbJets) != 0:
                        Glead_b=matched_jets_1b
                print('matched_jet_1b :',matched_jets_1b)
                print('sel_jet_1b:',lead_b)

                if len(matched_jets_1b)   :
                        good_event_b=True
                if not good_event_b  :
                        pass

        if good_event_b==True and good_event_Photon==True :
                labels.append({'label':'s'})
        else:
                labels.append({'label':'b'})
        print(labels)
	print('Len Lead b',len(lead_b))












#------------- Getting Leading & SubLeading Jet---------------------


    	lead_jets=sorted(Jets,key=lambda x:x['pt'],reverse=True)[:1]
	sublead_jets=sorted(Jets,key=lambda x:x['pt'],reverse=True)[1:2]
	Jets = sorted(Jets,key=lambda x:x['pt'],reverse=True)	
	SV=sorted(SV,key=lambda x:x['SV_pt'],reverse=True)[:1]
	PV=sorted(PV,key=lambda x:x['PV_score'],reverse=True)[:1]
	dRs_lead = []
	dRs_sublead= []
	dRm= []

	'''
	dR_Pho_Jet_Lead = deltaR(Photons[0]["phi"],lead_jets[0]["phi"],Photons[0]["eta"],lead_jets[0]["eta"])
	dRs_lead.append(dR_Pho_Jet_Lead)
	dR_Pho_Jet_SubLead = deltaR(Photons[0]["phi"],sublead_jets[0]["phi"],Photons[0]["eta"],sublead_jets[0]["eta"])
        dRs_sublead.append(dR_Pho_Jet_SubLead)


	'''
	if len(lead_b) :
		for i,photon in enumerate(Photons):
           		for jet in lead_b:
                		dR_Pho_bJet_Lead = deltaR(photon["phi"],jet["phi"],photon["eta"],jet["eta"])
                		dRm.append({'dR_GbJet_lead':dR_Pho_bJet_Lead})
		
		for i,photon in enumerate(Photons):
                        for jet in lead_b:
                                dPhi_Pho_bJet_Lead = deltaPhi(photon["phi"],jet["phi"])
                                dphi_b.append({'dPhi_GbJet_lead':dPhi_Pho_bJet_Lead})
	for i,photon in enumerate(Photons):
                        for jet in lead_jets:
                                dPhi_Pho_Jet_Lead = deltaPhi(photon["phi"],jet["phi"])
                                dphi.append({'dPhi_GJet_lead':dPhi_Pho_Jet_Lead}) 
	for i,photon in enumerate(Photons):
	   for jet in lead_jets:
		dR_Pho_Jet_Lead = deltaR(photon["phi"],jet["phi"],photon["eta"],jet["eta"])
		dRs_lead.append({'dR_GJet_lead':dR_Pho_Jet_Lead})
	for i,photon in enumerate(Photons):
           for jet in sublead_jets:
                dR_Pho_Jet_SubLead = deltaR(photon["phi"],jet["phi"],photon["eta"],jet["eta"])
                dRs_sublead.append({'dR_GJet_sublead':dR_Pho_Jet_SubLead})

	Sum_Jet_pt=0.
	for i,jet in enumerate(Jets) : 
		Jet_pt = jet["pt"]
		Sum_Jet_pt += Jet_pt
	ht.append({'HT':Sum_Jet_pt})		
#-----------Extract Selected Variables----------------------------
	Match_1b.append(0)
        Match_2b.append(len(lead_b)+len(sublead_b))
        #Match_ph.append(len(sel_photons))	
        if len(matched_photons)==0:
                matched_photons.append({'pt':-999,'eta':-999,'phi':-999})
	GPhotons+=matched_photons
	if len(GenPhotons)==0:
              	RGPhotons.append({'pt':-999,'eta':-999,'phi':-999})
	RGPhotons+=GenPhotons
	if len(Photons)==0:
                RRPhotons.append({'pt':-999,'eta':-999,'phi':-999})
	#RRPhotons+=Photons		
        if len(GenPhotons)==0:
                nGPhotons.append({'nGPhotons':0})
	nGPhotons.append({'nGPhotons':len(GenPhotons)})
	if len(Photons)==0:
                nPhotons.append({'nPhotons':0})
        nPhotons.append({'nPhotons':len(Photons)})		
        if len(sel_photons)==0:
                sel_photons.append({'pt':-999,'eta':-999,'phi':-999,'hoe':-999,'sieie':-999,'r9':-999,'Iso_all':-999,'Iso_chg':-999})
	Sel_photons+=sel_photons		
        if len(Jets)==0:
                nJets.append({'nJets':0})
		ht.append({'HT':0})
		
	#if len(lead_b)==0:
                #nbJets.append({'nbJets':0})
	nbJets.append({'nbJets':len(lead_b)})
	nJets.append({'nJets':len(Jets)})
	HT += ht
	if len(lead_b)==0:
                lead_b.append({'pt':-999,'eta':-999,'phi':-999})
		dphi_b.append({'dPhi_GbJet_lead': -999})
	dPhi_b+=dphi_b
        Sel_bjets+=lead_b
        if len(lead_jets)==0:
                lead_jets.append({'pt':-999,'eta':-999,'phi':-999})
		dphi.append({'dPhi_GJet_lead': -999})
	dPhi+=dphi	
	Sel_jets+=lead_jets			        
        if len(sublead_jets)==0:
                sublead_jets.append({'pt':-9999,'eta':-9999,'phi':-9999})
	Sublead_jets+=sublead_jets 
        if met_pt==0:
                met_pt=-999						
        Met_pt.append({'pt':met_pt})
        if met_phi==0:
                met_phi=-999
        Met_phi.append({'phi':met_phi})
        if len(labels)==0:
                labels.append({'label':-999})
	if len(dRm)==0:
                dRm.append({'dR_GbJet_lead':-999})
	DRm+=dRm
	if len(dRs_lead) == 0 :
                dRs_lead.append({'dR_GJet_lead':-999})
	dR_GJet_lead+=dRs_lead
	if len(dRs_sublead) == 0 :
                dRs_sublead.append({'dR_GJet_sublead':-999})
	dR_GJet_sublead+=dRs_sublead
	#if len(SV)==0:
                #nSVs.append({'nSV':0})
        nSVs.append({'nSV':nSV})
	nPVs.append({'nPV':nPV})
	if nSV==0:
                SV.append({'SV_dlen':-999,'SV_dlenSig':-999,'SV_dxy':-999,'SV_dxySig':-999,'SV_pAngle':-999,'SV_chi2':-999,'SV_eta':-999,'SV_eta':-999,'SV_phi':-999,'SV_pt':-999,'SV_ndof':-999})
        SVs+=SV
	if nPV==0:
                PV.append({'PV_ndof':-999,'PV_x':-999,'PV_y':-999,'PV_z':-999,'PV_chi2':-999,'PV_score':-999,})
	PVs+=PV
        Labels+=labels
	if good_event_Photon : # num cut satisfied
		count_events_num += 1
		
		

for n in nPhotons:
                npho += n['nPhotons']

#---------Create Dataset's list---------------------------------
written=[]
biggest_len = len(GPhotons)
for i in range(biggest_len):
	temp_dict = {} #empty dict
	temp_dict['RGPhoton_pt'] = RGPhotons[i]['pt']
        temp_dict['RGPhoton_eta'] = RGPhotons[i]['eta']
        temp_dict['RGPhoton_phi'] = RGPhotons[i]['phi']
        temp_dict['Rphoton_pt'] = RRPhotons[i]['pt']
        temp_dict['Rphoton_eta'] = RRPhotons[i]['eta']
        temp_dict['Rphoton_phi'] = RRPhotons[i]['phi']
        temp_dict['GPhoton_pt'] = GPhotons[i]['pt']
        temp_dict['GPhoton_eta'] = GPhotons[i]['eta']
        temp_dict['GPhoton_phi'] = GPhotons[i]['phi']
        temp_dict['photon_pt'] = Sel_photons[i]['pt']
        temp_dict['photon_eta'] = Sel_photons[i]['eta']
        temp_dict['photon_phi'] = Sel_photons[i]['phi']
	temp_dict['photon_hoe'] = Sel_photons[i]['hoe']
        temp_dict['photon_sieie'] = Sel_photons[i]['sieie']
        temp_dict['photon_r9'] = Sel_photons[i]['r9']
	temp_dict['photon_Iso_all'] = Sel_photons[i]['Iso_all']
        temp_dict['photon_Iso_chg'] = Sel_photons[i]['Iso_chg']
	temp_dict['bjet_pt'] = Sel_bjets[i]['pt']
        temp_dict['bjet_eta'] = Sel_bjets[i]['eta']
        temp_dict['bjet_phi'] = Sel_bjets[i]['phi']
        temp_dict['jet_pt'] = Sel_jets[i]['pt']
        temp_dict['jet_eta'] = Sel_jets[i]['eta']
        temp_dict['jet_phi'] = Sel_jets[i]['phi']
        temp_dict['SLjet_pt'] = Sublead_jets[i]['pt']
        temp_dict['SLjet_eta'] = Sublead_jets[i]['eta']
        temp_dict['SLjet_phi'] = Sublead_jets[i]['phi']
	temp_dict['nbJets'] = nbJets[i]['nbJets']
	temp_dict['nPhotons'] = nPhotons[i]['nPhotons']
	temp_dict['nJets'] = nJets[i]['nJets']
        temp_dict['met_pt'] = Met_pt[i]['pt']
        temp_dict['met_phi'] = Met_phi[i]['phi']
        temp_dict['nGPhotons'] = nGPhotons[i]['nGPhotons']
        temp_dict['Labels'] = Labels[i]['label']
	
	temp_dict['dPhi_GJet_lead'] = dPhi[i]['dPhi_GJet_lead']
	temp_dict['dPhi_GbJet_lead'] = dPhi_b[i]['dPhi_GbJet_lead']
	temp_dict['dR_GJet_lead'] = dR_GJet_lead[i]['dR_GJet_lead']
	temp_dict['dR_GJet_sublead'] = dR_GJet_sublead[i]['dR_GJet_sublead']
	temp_dict['dR_GbJet_lead'] = DRm[i]['dR_GbJet_lead']
	temp_dict['nSV'] = nSVs[i]['nSV']
	temp_dict['nPV'] = nPVs[i]['nPV']
	temp_dict['SV_dlen'] = SVs[i]['SV_dlen']	
	temp_dict['SV_dlenSig'] = SVs[i]['SV_dlenSig']
	temp_dict['SV_dxy'] = SVs[i]['SV_dxy']
	temp_dict['SV_dxySig'] = SVs[i]['SV_dxySig']
	temp_dict['SV_pAngle'] = SVs[i]['SV_pAngle']
	temp_dict['SV_chi2'] = SVs[i]['SV_chi2']
	temp_dict['SV_eta'] = SVs[i]['SV_eta']
	temp_dict['SV_phi'] = SVs[i]['SV_phi']
	temp_dict['SV_pt'] = SVs[i]['SV_pt']
	temp_dict['SV_ndof'] = SVs[i]['SV_ndof']

	temp_dict['PV_ndof'] = PVs[i]['PV_ndof']
        temp_dict['PV_x'] = PVs[i]['PV_x']
        temp_dict['PV_y'] = PVs[i]['PV_y']
        temp_dict['PV_z'] = PVs[i]['PV_z']
        temp_dict['PV_chi2'] = PVs[i]['PV_chi2']
	temp_dict['PV_score'] = PVs[i]['PV_score']
	temp_dict['HT'] = HT[i]['HT']
	written.append(temp_dict)


#------- Write to CSV -------------------

fields = ['dPhi_GJet_lead','dPhi_GbJet_lead','HT','nPV','PV_ndof','PV_x','PV_y','PV_z','PV_chi2','PV_score','nSV','SV_dlen','SV_dlenSig','SV_dxy','SV_dxySig','SV_pAngle','SV_chi2','SV_eta','SV_phi','SV_pt','SV_ndof','dR_GbJet_lead','dR_GJet_lead','dR_GJet_sublead', 'nPhotons','nJets','nbJets','RMatched_GPhoton_pt','RMatched_GPhoton_eta','RMatched_GPhoton_phi','RPhoton_pt','RPhoton_eta','RPhoton_phi','Matched_GPhoton_pt','Matched_GPhoton_eta','Matched_GPhoton_phi','Photon_pt','Photon_eta','Photon_phi','Photon_hoe','Photon_sieie','Photon_r9','Iso_all','Iso_chg' ,'Lead_bJet_pt','Lead_bJet_eta','Lead_bJet_phi','Lead_Jet_pt','Lead_Jet_eta','Lead_Jet_phi','SubLead_Jet_pt','SubLead_Jet_eta','SubLead_Jet_phi','MET_pt','MET_phi','Labels']


rows = written
with open('/afs/cern.ch/user/m/mbarakat/gamma_b/looseCSVFix/PhotonNb_'+str(sname)+'_Train'+str(divIndex)+'_'+str(stype)+'.csv', 'w') as f:

    		write = csv.writer(f)
    		write.writerow(fields)
    		for row in rows:
			r = [row['dPhi_GJet_lead'],row['dPhi_GbJet_lead'],row['HT'],row['nPV'],row['PV_ndof'],row['PV_x'],row['PV_y'],row['PV_z'],row['PV_chi2'],row['PV_score'],row['nSV'],row['SV_dlen'],row['SV_dlenSig'],row['SV_dxy'],row['SV_dxySig'],row['SV_pAngle'],row['SV_chi2'],row['SV_eta'],row['SV_phi'],row['SV_pt'],row['SV_ndof'],row['dR_GbJet_lead'],row['dR_GJet_lead'],row['dR_GJet_sublead'],row['nPhotons'],row['nJets'],row['nbJets'],row['RGPhoton_pt'],row['RGPhoton_eta'],row['RGPhoton_phi'],row['Rphoton_pt'],row['Rphoton_eta'],row['Rphoton_phi'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['photon_pt'],row['photon_eta'],row['photon_phi'],row['photon_hoe'],row['photon_sieie'],row['photon_r9'],row['photon_Iso_all'],row['photon_Iso_chg'], row['bjet_pt'],row['bjet_eta'],row['bjet_phi'],row['jet_pt'],row['jet_eta'],row['jet_phi'],row['SLjet_pt'],row['SLjet_eta'],row['SLjet_phi'],row['met_pt'],row['met_phi'],row['Labels']]
                        
        		write.writerow(r)


print('OK'*10)

#------- Check for n objects in goodParticles--------
print('Nph',Nph)   # Check for extra photons in ngoodPhotons
print('nbJet', Nbj)
print('nGbj', NGbj)
print('count_events_num',count_events_num)
print('count_events_den',count_events_den)
Matching_Events_eff=(count_events_num)/(count_events_den*1.0)
print('Matching_Events_eff',Matching_Events_eff)
