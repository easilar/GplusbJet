import ROOT
import helper
from helper import *
import csv
import json
import os
import pickle
import operator
from optparse import OptionParser


parser = OptionParser()
parser.add_option("--b", dest="b", default="0", action="store", help="1b or 2b")
(options, args) = parser.parse_args()
b=int(options.b)

sample_dic=pickle.load(open("samples_ana.pkl",'rb'))
mychain_dict  =  getChain(year=2016, stype='signal', sname='G1Jet_Pt', pfile='samples_ana.pkl', datatype='all', test=False)
ch = mychain_dict[0]

<<<<<<< HEAD
number_events=ch.GetEntries()
number_events=100000

=======
#number_events=ch.GetEntries()
number_events=10000
>>>>>>> 1a46b043f130d24cf06ce2d16d346cc5782193c3
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

Met_pt=[] # Met_pt after Matching
Met_phi=[]
DRm=[]
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


for jentry in range(number_events):
	ch.GetEntry(jentry)

	good_event_Photon=False
	good_event_b=False
	good_event_2b=False

   	nGenPart=ch.GetLeaf('nGenPart').GetValue() # nGen Particles in one event#float
   	nGenJet=ch.GetLeaf('nGenJet').GetValue() # nGen Particles in one event
   	nPhoton = ch.GetLeaf('ngoodPhoton').GetValue() # nReco Photon inside one event
   	nJet = ch.GetLeaf('ngoodJet').GetValue() # nReco Jets inside one event
   	nbJet = ch.GetLeaf('ngoodbJet').GetValue() # nReco Jets inside one event
   	met_pt=ch.GetLeaf('MET_pt').GetValue()
   	met_phi=ch.GetLeaf('MET_phi').GetValue()

	Nph.add(nPhoton)
   	Nbj.add(nbJet)
   	Nj.add(nJet)
	
	# Matching Efficiency  = (nEvents with 1 matched Photon and 1/2 matched bJet + 1 RecoPhoton + 1/2 RecobJets ) / ( nEvents with 1 RecoPhoton + 1/2 RecobJets)
	
	# variable = Running for 1 b or 2 b


	#count_events_den += 1 # All 1 Photon 1 /2 bJet Events

	#lists of variables per event
	Photons=[]          # kin of Reco Photons
   	Jets=[]             # kin of Reco Jets
   	GenJets=[]              # kin of G jets
	GenbJets=[]
   	GenPhotons=[]           # kin of Gen Particles
   	bJets=[]

	matched_photons=[]
   	sel_photons=[]
	matched_jets_1b=[]
	matched_jets_lb=[]
	matched_jets_slb=[]
	lead_b=[]
	sublead_b=[]
	Glead_b=[]
	Lead_bJets=[]
	subGlead_b=[]
	dRms=[]
	labels=[]

	if nPhoton != 1 or nbJet == 0 : continue     # Denominator cut satisfied

	if b==0 and nbJet != 0:
		count_events_den += 1
		nbJets.append({'nbJets':nbJet})
		NPhotons.append(nPhoton)
        elif b==1 and nbJet == 1:
		count_events_den += 1
		nbJets.append({'nbJets':nbJet})
                NPhotons.append(nPhoton)
        elif b==2 and nbJet > 1:
		count_events_den += 1
		nbJets.append({'nbJets':nbJet})
                NPhotons.append(nPhoton)
        #elif b and nbJet == 0:
                #nbJets.append({'nbJets':nbJet})
	#for n in nbJets:
                #Number_b += n['nbJets']	

	
#---------- second loop : nVariables inside Particles-------------------
	temp_index = 0

	for ID in range(int(nGenPart)): # Gen Photons   #List of Dict
		
		if ch.GetLeaf('GenPart_pdgId').GetValue(ID)==22:
			GenPhotons.append({'index':temp_index,'orig_index':ID,'pt':ch.GetLeaf('GenPart_pt').GetValue(ID),'eta':ch.GetLeaf('GenPart_eta').GetValue(ID),'phi':ch.GetLeaf('GenPart_phi').GetValue(ID)})
			temp_index += 1

	if b==0  :	
		for I in range(int(nPhoton)): # Reco PHOTONS
			if  ch.GetLeaf('ngoodbJet').GetValue(I)>=1:
				Photons.append({'index':I,'pt':ch.GetLeaf('goodPhoton_pt').GetValue(I),'eta':ch.GetLeaf('goodPhoton_eta').GetValue(I),'phi':ch.GetLeaf('goodPhoton_phi').GetValue(I)})
        elif b==1 :
                for I in range(int(nPhoton)): # Reco PHOTONS
			if  ch.GetLeaf('ngoodbJet').GetValue(I)==1:
                        	Photons.append({'index':I,'pt':ch.GetLeaf('goodPhoton_pt').GetValue(I),'eta':ch.GetLeaf('goodPhoton_eta').GetValue(I),'phi':ch.GetLeaf('goodPhoton_phi').GetValue(I)})
        elif b==2 :
                for I in range(int(nPhoton)): # Reco PHOTONS
			if  ch.GetLeaf('ngoodbJet').GetValue(I)>1:
                        	Photons.append({'index':I,'pt':ch.GetLeaf('goodPhoton_pt').GetValue(I),'eta':ch.GetLeaf('goodPhoton_eta').GetValue(I),'phi':ch.GetLeaf('goodPhoton_phi').GetValue(I)})


	for ID in range(int(nGenJet)): # Gen Jets   #List of Dictionary
		GenJets.append({'index':ID,'pt':ch.GetLeaf('GenJet_pt').GetValue(ID),'eta':ch.GetLeaf('GenJet_eta').GetValue(ID),'phi':ch.GetLeaf('GenJet_phi').GetValue(ID)})
	temp_index = 0
        for ID in range(int(nGenJet)): # Gen Jets   #List of Dictionary
		if abs(ch.GetLeaf('GenJet_partonFlavour').GetValue(ID))==5:
                	GenbJets.append({'index':temp_index,'orig_index':ID,'pt':ch.GetLeaf('GenJet_pt').GetValue(ID),'eta':ch.GetLeaf('GenJet_eta').GetValue(ID),'phi':ch.GetLeaf('GenJet_phi').GetValue(ID)})
			temp_index += 1

	for j in range(int(nJet)): # Reco JETS
        	Jets.append({'index':j,'pt':ch.GetLeaf('goodJet_pt').GetValue(j),'phi':ch.GetLeaf('goodJet_phi').GetValue(j),'eta':ch.GetLeaf('goodJet_eta').GetValue(j)})

	for j in range(int(nbJet)): # Reco  bJets
		bJets.append({'index':j,'pt':ch.GetLeaf('goodbJet_pt').GetValue(j),'phi':ch.GetLeaf('goodbJet_phi').GetValue(j),'eta':ch.GetLeaf('goodbJet_eta').GetValue(j)})


	print(' ')
	print(' ')
	print('event#',jentry)
	if len(GenbJets) != 0:
		print('OK GEN b')

	#print("LenGenJets---LenGenPhotons----LenJets----LenGenbJets----LenRecobJets---LenPhotons")
   	print('GenPhotons',len(GenPhotons),'Photons',len(Photons),'GenJets' , len(GenJets) ,'Jets',len(Jets),'Gen bJets',len(GenbJets),'bJets' ,len(bJets))
	print(' ')
	#print('GenPhotons',GenPhotons)
	#print('Photons',Photons)

#-------------Append raw variables-----------------------------------------------------

	RRPhotons += Photons
	lead_bJets=sorted(bJets,key=lambda x:x['pt'],reverse=True)[:1]
	sublead_bJets=sorted(bJets,key=lambda x:x['pt'],reverse=True)[1:2]
	RLead_bJets += lead_bJets
	RSubLead_bJets += sublead_bJets
# ------------PHOTON MATCHING INSIDE CONE dR----------------------------------------------
	
	dRm=[]
	#dRm.append({'index':j,'dR':0})
	#if len(GenPhotons)==0:
		#continue
	
	for i,photon in enumerate(Photons):  # Matching GenPhoton-RecoPhoton in cone dR
		for j,GenPhoton in enumerate(GenPhotons):
			dR_Pho_Match = deltaR(photon["phi"],GenPhoton["phi"],photon["eta"],GenPhoton["eta"])
			PtRatio=abs(GenPhoton["pt"]-photon["pt"])/(GenPhoton["pt"])
			#print('dr',dR_Pho_Match)
			#print('PtR',abs(PtRatio))
			dRm.append({'index':GenPhoton['index'],'dR':dR_Pho_Match,'PtRatio':PtRatio })
			GenPhoton['dR'] = dR_Pho_Match
			GenPhoton['PtRatio']=  PtRatio
			
	if len(dRm) == 0 :continue

	dRm=sorted(dRm,key=lambda x:x['dR'])

    	for i in  dRm :
            if abs(i['PtRatio']) < 0.2:
		    matched_GenPhoton=[x for x in GenPhotons if x['index']==i['index']][0]	
                    matched_photons.append(matched_GenPhoton)
                    break
            else :
                    continue

    	if  len(matched_photons) and matched_photons[0]['dR'] <= 0.5:
            sel_photons=Photons
	#print('matched_photons :',matched_photons)
	#print('Sel_photons:',sel_photons)
	'''
	GenPhotons=sorted(GenPhotons,key=lambda x:x['pt'],reverse=True)
	matched_photons.append(GenPhotons[0])
	#sel_photons=Photons
	'''
    	if len(matched_photons)   :
            	good_event_Photon=True
		
    	#if not good_event_Photon  : continue
	
#------------- 1b Matching ----------------------------------------
	
	print('#'*10)
	print('GenbJets', len(GenbJets))
	print('bJets',len(bJets))
	print('#'*10)

	
	if nbJet == 1 and (b == 1 or b==0) :
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
			GenJet['dR']	= dR_Jet_Match			

        	if len(dRmJ) == 0 :continue # in case dRmj is empty due to empty GenbJets
		dRmJ=sorted(dRmJ,key=lambda x:x['dR'])
        	print('dRmJ',dRmJ)
        	for i in  dRmJ :
                	if abs(i['PtRatio']) < 0.5:
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
		
#----------------- 2b Matching ---------------------------------------------------------

	elif nbJet > 1  and (b>1 or b==0):
		
		bJets=sorted(bJets,key=lambda x:x['pt'],reverse=True)
		lead_bjet=(bJets[0])
        	sublead_bjet=(bJets[1])
		
        	dRmJ_lb=[]
                print('Start matching the first b')
            	for j,GenJet in enumerate(GenbJets):
                                dR_Jet_Match_lb = deltaR(lead_bjet["phi"],GenJet["phi"],lead_bjet["eta"],GenJet["eta"])
                                PtRatioJ_lb=abs(GenJet["pt"]-lead_bjet["pt"])/(GenJet["pt"])
				dRmJ_lb.append({'index':GenJet['index'],'dR':dR_Jet_Match_lb,'PtRatioJ_lb':PtRatioJ_lb})
				GenJet['PtRatioJ_lb'] =  PtRatioJ_lb
				GenJet['dR'] =  dR_Jet_Match_lb
                               	print('j:',j)
                               	print('drJ_lb',dR_Jet_Match_lb)
                                print('PtRJ_lb',abs(PtRatioJ_lb))
            	if len(dRmJ_lb) == 0 :continue # in case dRmj is empty due to empty GenbJets

		dRmJ_lb=sorted(dRmJ_lb,key=lambda x:x['dR'])
            	print('dRmJ_lb',dRmJ_lb)

            	for i in  dRmJ_lb :
                	if abs(i['PtRatioJ_lb']) < 0.5:
				matched_GenbJet=[x for x in GenbJets if x['index']==i['index']][0]
                        	matched_jets_lb.append(matched_GenbJet)
                        	break
                	else :
                        	continue
        	if  len(matched_jets_lb) and matched_jets_lb[0]['dR'] <= 0.5:
                        lead_b.append(lead_bjet)
		if len(GenbJets) != 0:
			Glead_b=matched_jets_lb
			res = list(filter(lambda i: i['index'] != Glead_b[0]['index'], GenbJets))
		print('matched_jet_lb :',matched_jets_lb)
		print('res:',res)
		
		GenbJets = res
		if len(GenbJets) == 0 : continue 

            	dRmJ_slb=[]
                for GenJt in res:
                                dR_Jet_Match_slb = deltaR(sublead_bjet["phi"],GenJt["phi"],sublead_bjet["eta"],GenJet["eta"])
                                PtRatioJ_slb=abs(GenJt["pt"]-sublead_bjet["pt"])/(GenJt["pt"])
				dRmJ_slb.append({'index':GenJt['index'],'dR':dR_Jet_Match_slb,'PtRatioJ_slb':PtRatioJ_slb})
				GenJt['PtRatioJ_slb'] =  PtRatioJ_slb
                                GenJt['dR'] =  dR_Jet_Match_slb
                                print('drJ_slb',dR_Jet_Match_slb)
                                print('PtRJ_slb',abs(PtRatioJ_slb))

            	if len(dRmJ_slb) == 0 :continue # in case dRmj is empty due to empty GenbJets
		dRmJ_slb=sorted(dRmJ_slb,key=lambda x:x['dR'])
            	print('dRmJ_slb',dRmJ_slb)

            	for i in  dRmJ_slb :
<<<<<<< HEAD
			print('ABS PT_SLB',abs(i['PtRatioJ_slb']))
			print('i index',i['index'],'Gleadb index',Glead_b[0]['index'],'len gbjets',len(GenbJets))
			if  i['index'] == Glead_b[0]['index']: continue
                    	if abs(i['PtRatioJ_slb']) < 0.2:
=======
                    	if abs(i['PtRatioJ_slb']) < 0.5:
>>>>>>> 1a46b043f130d24cf06ce2d16d346cc5782193c3
				matched_GenbJet=[x for x in GenbJets if x['index']==i['index']][0]
                                matched_jets_slb.append(matched_GenbJet)
                                break
                        else :
                                continue

            	if len(matched_jets_slb) and  matched_jets_slb[0]['dR'] <= 0.5:
                        sublead_b.append(sublead_bjet)
			subGlead_b=matched_jets_slb
			
		print('matched_jet_slb :',matched_jets_slb)
		if len( matched_jets_lb) or len(matched_jets_slb):
				good_event_b=True
		if len( matched_jets_lb) and len(matched_jets_slb):
				good_event_2b=True
   				good_event_b=True
	else: # BKG
		pass

	print(good_event_Photon)
	print(good_event_b)
	if good_event_b==True:
		labels.append({'label':'s'})
	else:
		labels.append({'label':'b'})
	print(labels)
	

#------------- Getting Leading & SubLeading Jet---------------------

    	lead_jets=sorted(Jets,key=lambda x:x['pt'],reverse=True)[:1]
	sublead_jets=sorted(Jets,key=lambda x:x['pt'],reverse=True)[1:2]
	
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
                sel_photons.append({'pt':-999,'eta':-999,'phi':-999})
	Sel_photons+=sel_photons		
        if len(Jets)==0:
                nJets.append({'nJets':0})
	nJets.append({'nJets':len(Jets)})				        
        if len(bJets)==0:
                nbJets.append({'nbJets':0})
	#nbJets.append({'nbJets':len(bJets)})				        
        if len(lead_jets)==0:
                lead_jets.append({'pt':-999,'eta':-999,'phi':-999})	
	Sel_jets+=lead_jets			        
        if len(sublead_jets)==0:
                sublead_jets.append({'pt':-9999,'eta':-9999,'phi':-9999})
	Sublead_jets+=sublead_jets 
        if len(lead_b)==0:
                lead_b.append({'pt':-99999,'eta':-99999,'phi':-99999})
	Sel_bjets+=lead_b				
        if len(sublead_b)==0:
                sublead_b.append({'pt':-999999,'eta':-999999,'phi':-999999})
	SubLead_bJets+=sublead_b
	if len(Glead_b)==0:
                Glead_b.append({'pt':-99999,'eta':-99999,'phi':-99999})
        Gbjets+=Glead_b
        if len(subGlead_b)==0:
                subGlead_b.append({'pt':-999999,'eta':-999999,'phi':-999999})
        SubLead_GbJets+=subGlead_b
        if len(dRm)==0:
                dRm.append({'dRm':0})				  
        dRms.append({'dRm':dRm[0]['dR']})
        DRm+=dRms
        if met_pt==0:
                met_pt=-999						
        Met_pt.append({'pt':met_pt})
        if met_phi==0:
                met_phi=-999
        Met_phi.append({'phi':met_phi})
        if len(labels)==0:
                labels.append({'label':-999})
        Labels+=labels
	NGbj.add(len(GenbJets))
    	#Match_1b.append(len(sel_jets_1b))
    	#Match_2b.append(len(sel_jets_lb)+len(sel_jets_slb))
	#Match_ph.append(len(sel_photons))
	#NPhotons.append(nPhoton)
	
	if good_event_Photon and good_event_b : # num cut satisfied
		count_events_num += 1
		
		

for n in nbJets:
                Number_b += n['nbJets']
for m in Match_1b:
                M_1b += m
for k in Match_2b:
                M_2b += k
for s in NPhotons:
                Npho += s
#for s1 in NPhotons:
                #Npho1 += s1
#for s2 in NPhotons:
                #Npho2 += s2
for n in nPhotons:
                npho += n['nPhotons']
#for k in Match_ph:
                #M_ph += k

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
        temp_dict['jet_pt'] = Sel_jets[i]['pt']
        temp_dict['jet_eta'] = Sel_jets[i]['eta']
        temp_dict['jet_phi'] = Sel_jets[i]['phi']
        temp_dict['SLjet_pt'] = Sublead_jets[i]['pt']
        temp_dict['SLjet_eta'] = Sublead_jets[i]['eta']
        temp_dict['SLjet_phi'] = Sublead_jets[i]['phi']

	temp_dict['Gbjet_pt'] = Gbjets[i]['pt']
        temp_dict['Gbjet_eta'] = Gbjets[i]['eta']
        temp_dict['Gbjet_phi'] = Gbjets[i]['phi']
        temp_dict['GSLbjet_pt'] = SubLead_GbJets[i]['pt']
        temp_dict['GSLbjet_eta'] = SubLead_GbJets[i]['eta']
        temp_dict['GSLbjet_phi'] = SubLead_GbJets[i]['phi']
        temp_dict['bjet_pt'] = Sel_bjets[i]['pt']
        temp_dict['bjet_eta'] = Sel_bjets[i]['eta']
        temp_dict['bjet_phi'] = Sel_bjets[i]['phi']
        temp_dict['SLbjet_pt'] = SubLead_bJets[i]['pt']
        temp_dict['SLbjet_eta'] = SubLead_bJets[i]['eta']
        temp_dict['SLbjet_phi'] = SubLead_bJets[i]['phi']
        temp_dict['met_pt'] = Met_pt[i]['pt']
        temp_dict['met_phi'] = Met_phi[i]['phi']
        temp_dict['dRm'] = DRm[i]['dRm']
        temp_dict['nGPhotons'] = nGPhotons[i]['nGPhotons']
        temp_dict['nJets'] = nJets[i]['nJets']
        temp_dict['nbJets'] = nbJets[i]['nbJets']
        temp_dict['Labels'] = Labels[i]['label']	
	written.append(temp_dict)


#------- Write to CSV -------------------

# field names
if b==1:

	fields = [ 'nGphotons','ngooJets','ngoodbJets','RMatched_GPhoton_pt','RMatched_GPhoton_eta','RMatched_GPhoton_phi','RPhoton_pt','RPhoton_eta','RPhoton_phi','Matched_GPhoton_pt','Matched_GPhoton_eta','Matched_GPhoton_phi','Photon_pt','Photon_eta','Photon_phi' ,'Lead_Jet_pt','Lead_Jet_eta','Lead_Jet_phi','SubLead_Jet_pt','SubLead_Jet_eta','SubLead_Jet_phi','GLead_bJet_pt','GLead_bJet_eta','GLead_bJet_phi','GSubLead_bJet_pt','GSubLead_bJet_eta','GSubLead_bJet_phi','Lead_bJet_pt','Lead_bJet_eta','Lead_bJet_phi','SubLead_bJet_pt','SubLead_bJet_eta','SubLead_bJet_phi','MET_pt','MET_phi','dR_Photon_Gen_Reco','Labels']


	rows = written
	with open('S_50_1.csv', 'w') as f:

    		write = csv.writer(f)
    		write.writerow(fields)
    		for row in rows:
			r = [row['nGPhotons'],row['nJets'],row['nbJets'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['Rphoton_pt'],row['Rphoton_eta'],row['Rphoton_phi'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['photon_pt'],row['photon_eta'],row['photon_phi'], row['jet_pt'],row['jet_eta'],row['jet_phi'],row['SLjet_pt'],row['SLjet_eta'],row['SLjet_phi'],row['Gbjet_pt'],row['Gbjet_eta'],row['Gbjet_phi'],row['GSLbjet_pt'],row['GSLbjet_eta'],row['GSLbjet_phi'],row['bjet_pt'],row['bjet_eta'],row['bjet_phi'],row['SLbjet_pt'],row['SLbjet_eta'],row['SLbjet_phi'],row['met_pt'],row['met_phi'],row['dRm'],row['Labels']]
                        
        		write.writerow(r)
elif b>1:

	fields = [ 'nGphotons','ngooJets','ngoodbJets','RMatched_GPhoton_pt','RMatched_GPhoton_eta','RMatched_GPhoton_phi','RPhoton_pt','RPhoton_eta','RPhoton_phi','Matched_GPhoton_pt','Matched_GPhoton_eta','Matched_GPhoton_phi','Photon_pt','Photon_eta','Photon_phi' ,'Lead_Jet_pt','Lead_Jet_eta','Lead_Jet_phi','SubLead_Jet_pt','SubLead_Jet_eta','SubLead_Jet_phi','GLead_bJet_pt','GLead_bJet_eta','GLead_bJet_phi','GSubLead_bJet_pt','GSubLead_bJet_eta','GSubLead_bJet_phi','Lead_bJet_pt','Lead_bJet_eta','Lead_bJet_phi','SubLead_bJet_pt','SubLead_bJet_eta','SubLead_bJet_phi','MET_pt','MET_phi','dR_Photon_Gen_Reco','Labels']

        rows = written
        with open('S_50_2.csv', 'w') as f:

        	write = csv.writer(f)
        	write.writerow(fields)
        	for row in rows:
                	r = [row['nGPhotons'],row['nJets'],row['nbJets'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['Rphoton_pt'],row['Rphoton_eta'],row['Rphoton_phi'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['photon_pt'],row['photon_eta'],row['photon_phi'], row['jet_pt'],row['jet_eta'],row['jet_phi'],row['SLjet_pt'],row['SLjet_eta'],row['SLjet_phi'],row['Gbjet_pt'],row['Gbjet_eta'],row['Gbjet_phi'],row['GSLbjet_pt'],row['GSLbjet_eta'],row['GSLbjet_phi'],row['bjet_pt'],row['bjet_eta'],row['bjet_phi'],row['SLbjet_pt'],row['SLbjet_eta'],row['SLbjet_phi'],row['met_pt'],row['met_phi'],row['dRm'],row['Labels']]
                        write.writerow(r)
elif b==0:

	fields = [ 'nGphotons','ngooJets','ngoodbJets','RMatched_GPhoton_pt','RMatched_GPhoton_eta','RMatched_GPhoton_phi','RPhoton_pt','RPhoton_eta','RPhoton_phi','Matched_GPhoton_pt','Matched_GPhoton_eta','Matched_GPhoton_phi','Photon_pt','Photon_eta','Photon_phi' ,'Lead_Jet_pt','Lead_Jet_eta','Lead_Jet_phi','SubLead_Jet_pt','SubLead_Jet_eta','SubLead_Jet_phi','GLead_bJet_pt','GLead_bJet_eta','GLead_bJet_phi','GSubLead_bJet_pt','GSubLead_bJet_eta','GSubLead_bJet_phi','Lead_bJet_pt','Lead_bJet_eta','Lead_bJet_phi','SubLead_bJet_pt','SubLead_bJet_eta','SubLead_bJet_phi','MET_pt','MET_phi','dR_Photon_Gen_Reco','Labels']


	rows = written
        with open('S_50_0.csv', 'w') as f:

                write = csv.writer(f)
                write.writerow(fields)
                for row in rows:
			r = [row['nGPhotons'],row['nJets'],row['nbJets'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['Rphoton_pt'],row['Rphoton_eta'],row['Rphoton_phi'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['photon_pt'],row['photon_eta'],row['photon_phi'], row['jet_pt'],row['jet_eta'],row['jet_phi'],row['SLjet_pt'],row['SLjet_eta'],row['SLjet_phi'],row['Gbjet_pt'],row['Gbjet_eta'],row['Gbjet_phi'],row['GSLbjet_pt'],row['GSLbjet_eta'],row['GSLbjet_phi'],row['bjet_pt'],row['bjet_eta'],row['bjet_phi'],row['SLbjet_pt'],row['SLbjet_eta'],row['SLbjet_phi'],row['met_pt'],row['met_phi'],row['dRm'],row['Labels']]
                        write.writerow(r)


#------- Check for n objects in goodParticles--------
if b==1:
	print('working with 1b')
else:
	print('working with 2b')
print('Nph',Nph)   # Check for extra photons in ngoodPhotons
#print(Nj)
print('nbJet', Nbj)
print('nGbj', NGbj)
#print('lenNPhotons',len(nPhotons))
#print('NPhotons',NPhotons)
#print('N 1 bJets after Selection', M_1b)
print('N bJets after Selection',M_2b)
print('N bJets before Selection',Number_b)
Match_eff_b =(M_1b+M_2b)/Number_b
print('Match_eff_b',Match_eff_b)
print('Nphoton after Selection',npho)
print('Nphoton Before Selection',Npho)
Match_eff_ph =(npho)/Npho
print('Match_eff_ph',Match_eff_ph)
print('count_events_num',count_events_num)
print('count_events_den',count_events_den)
Matching_Events_eff=(count_events_num)/(count_events_den*1.0)
print('Matching_Events_eff',Matching_Events_eff)
