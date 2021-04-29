import ROOT
import helper
from array import array
from helper import *
import csv
import json
import os
import pickle
import operator

#sample_dic=pickle.load(open("samples_ana.pkl",'rb'))
#sdic=sample_dic[2016]['signal']['G1Jet_Pt']['G1Jet_Pt_250To400_NOExt']
#ch=ROOT.TChain("Events")
#ch.Add(sdic['dir']+"/*.root")
mychain_dict  =  getChain(year=2016, stype='signal', sname='G1Jet_Pt', pfile='samples_ana.pkl', datatype='all', test=False)

ch = mychain_dict[0]


number_events=ch.GetEntries()
print(number_events)
number_events=500
#nevents=100

#Number of Particles in n events
Nph=set()  # N Photons per Event in goodPhotons
Nbj=set()
Nj=set()
NGbj=set()

#List of Variables for The dataset
Sel_photons=[]
Sel_jets=[]
Sel_bjets=[]
Sublead_jets=[]
HPT_jet=[]
GPhotons=[]
nGPhotons=[]
nJets=[]
nbJets=[]
Lead_bJets=[]
SubLead_bJets=[]
Met_pt=[]
Met_phi=[]
DRm=[]
Labels=[]
Match_1b=[]
Match_2b=[] # List of int
Number_b=0.
M_1b=0.
M_2b=0.


#--------- First loop : Looping on Events ---------


for jentry in range(number_events):
	ch.GetEntry(jentry)

	good_event_Photon=False

	good_event_b=False

	good_event_2b=False
	
	Bkg=True
	Signal=False

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

	# variable = Running for 1 b or 2 b
	if nPhoton>1: continue

	

	#lists of variables per event
	RecoPhotons=[]          # kin of Reco Photons
   	RecoJets=[]             # kin of Reco Jets
   	GenJets=[]              # kin of G jets
	GenbJets=[]
   	GenPhotons=[]           # kin of Gen Particles
   	bJets=[]
   	sel_photons=[]
   	hpt_jet=[]
     	labels=[]
	#if nbJet = 1 :
#---------- second loop : nVariables inside Particles-------------------

	for ID in range(int(nGenPart)): # Gen Photons   #List of Dict
		if ch.GetLeaf('GenPart_pdgId').GetValue(ID)==22:
			GenPhotons.append({'index':ID,'pt':ch.GetLeaf('GenPart_pt').GetValue(ID),'eta':ch.GetLeaf('GenPart_eta').GetValue(ID),'phi':ch.GetLeaf('GenPart_phi').GetValue(ID)})

	for I in range(int(nPhoton)): # Reco PHOTONS
		RecoPhotons.append({'index':I,'pt':ch.GetLeaf('goodPhoton_pt').GetValue(I),'eta':ch.GetLeaf('goodPhoton_eta').GetValue(I),'phi':ch.GetLeaf('goodPhoton_phi').GetValue(I)})
		
	for ID in range(int(nGenJet)): # Gen Jets   #List of Dictionary
		GenJets.append({'index':ID,'pt':ch.GetLeaf('GenJet_pt').GetValue(ID),'eta':ch.GetLeaf('GenJet_eta').GetValue(ID),'phi':ch.GetLeaf('GenJet_phi').GetValue(ID)})

        for ID in range(int(nGenJet)): # Gen Jets   #List of Dictionary
		if abs(ch.GetLeaf('GenJet_partonFlavour').GetValue(ID))==5:
                	GenbJets.append({'index':ID,'pt':ch.GetLeaf('GenJet_pt').GetValue(ID),'eta':ch.GetLeaf('GenJet_eta').GetValue(ID),'phi':ch.GetLeaf('GenJet_phi').GetValue(ID)})

	for j in range(int(nJet)): # Reco JETS 
        	RecoJets.append({'index':j,'pt':ch.GetLeaf('goodJet_pt').GetValue(j),'phi':ch.GetLeaf('goodJet_phi').GetValue(j),'eta':ch.GetLeaf('goodJet_eta').GetValue(j)})

	for j in range(int(nbJet)): # Reco  bJets 
		bJets.append({'index':j,'pt':ch.GetLeaf('goodbJet_pt').GetValue(j),'phi':ch.GetLeaf('goodbJet_phi').GetValue(j),'eta':ch.GetLeaf('goodbJet_eta').GetValue(j)})
   
	
	print(' ')
	print(' ')
	print('event#',jentry)
	if len(GenbJets) != 0:
		print('OK GEN b')

	#print("LenGenJets---LenGenPhotons----LenRecoJets----LenGenbJets----LenRecobJets---LenRecoPhotons")
   	print('GenPhotons',len(GenPhotons),'Photons',len(RecoPhotons),'GenJets' , len(GenJets) ,'Jets',len(RecoJets),'Gen bJets',len(GenbJets),'bJets' ,len(bJets))
	print(' ')
	#print('GenPhotons',GenPhotons)
	#print('RecoPhotons',RecoPhotons)


# ------------PHOTON MATCHING INSIDE CONE dR----------------------------------------------
	
	dRm=[]	
	for i,photon in enumerate(RecoPhotons):  # Matching GenPhoton-RecoPhoton in cone dR
		for GenPhoton in GenPhotons:
			dR_Pho_Match = deltaR(photon["phi"],GenPhoton["phi"],photon["eta"],GenPhoton["eta"])
			PtRatio=(GenPhoton["pt"]-photon["pt"])/(GenPhoton["pt"])
			#print('dr',dR_Pho_Match)
			#print('PtR',abs(PtRatio))
			if abs(PtRatio) < 0.1 :
				dRm.append(dR_Pho_Match)
			else:
				dRm.append(200000) #to avoid empty list and conserve index
	
	print('dRm',dRm)
	print('min dRm',min(dRm))

	min_index = dRm.index(min(dRm)) # index of the min value in dRm List
	sel_photons=[]
	matched_photons=[]
	if  min(dRm) <= 0.5:
		matched_photons.append(GenPhotons[min_index]) 
		sel_photons=RecoPhotons
	#print('matched :',matched_photons)
	#print('sel:',sel_photons)	

        if len(matched_photons)   :
                good_event_Photon=True #only after b matching
        if not good_event_Photon  : continue
	print(good_event_Photon)

#------------- 1b Matching ----------------------------------------

	print('GenbJets', GenbJets)
	print('bJets',bJets)
	
	matched_jets_1b=[]
	matched_jets_lb=[]
	matched_jets_slb=[]
	sel_jets_1b=[]
	sel_jets_lb=[]
	sel_jets_slb=[]
	lead_b=[]
	sublead_b=[]

	if nbJet == 1 :

        	dRmJ=[]
        	for i,jet in enumerate(bJets): 
                	for GenJet in GenbJets:
                        	dR_Jet_Match = deltaR(jet["phi"],GenJet["phi"],jet["eta"],GenJet["eta"])
                        	PtRatioJ=(GenJet["pt"]-jet["pt"])/(GenJet["pt"])
                 	      	print('drJ',dR_Jet_Match)
                        	print('PtRJ',abs(PtRatioJ))
                        	if abs(PtRatioJ) < 0.1 :
                                	dRmJ.append(dR_Jet_Match)
                        	else:
                                	dRmJ.append(200000)

        	if len(dRmJ) == 0 :continue # in case dRmj is empty due to empty GenbJets

        	print('dRmJ',dRmJ)
        	print('min dRmJ',min(dRmJ))
        	#print(' ')

        	min_indexJ = dRmJ.index(min(dRmJ)) # index of the min value in dRm List

        	if  min(dRmJ) <= 0.5:
                	matched_jets_1b.append(GenJets[min_index])
			sel_jets_1b=bJets
                        lead_b=sel_jets_1b
        	print('matched_jet :',matched_jets_1b)
		print('sel_jet_1b:',sel_jets_1b)

        	if len(matched_jets_1b)   :
                	good_event_b=True
        	if not good_event_b  :
			pass
		#print(good_event_1b)
	
#----------------- 2b Matching ---------------------------------------------------------
	'''
	elif nbJet > 1 :
 
		lead_bjets=sorted(bJets,key=lambda x:x['pt'],reverse=True)[:1]
        	sublead_bjets=sorted(bJets,key=lambda x:x['pt'],reverse=True)[1:2]
		
                dRmJ_lb=[]
                for i,jet in enumerate(lead_bjets):
                        for GenJet in GenbJets:
                                dR_Jet_Match_lb = deltaR(jet["phi"],GenJet["phi"],jet["eta"],GenJet["eta"])
                                PtRatioJ_lb=(GenJet["pt"]-jet["pt"])/(GenJet["pt"])
                               	print('drJ_lb',dR_Jet_Match_lb)
                                print('PtRJ_lb',abs(PtRatioJ_lb))
                                if abs(PtRatioJ_lb) < 0.1 :
                                        dRmJ_lb.append(dR_Jet_Match_lb)
                                else:
                                        dRmJ_lb.append(200000)

                if len(dRmJ_lb) == 0 :continue # in case dRmj is empty due to empty GenbJets

                print('dRmJ_lb',dRmJ_lb)
                print('min dRmJ_lb',min(dRmJ_lb))

                min_indexJ_lb = dRmJ_lb.index(min(dRmJ_lb)) # index of the min value in dRm List

                if  min(dRmJ_lb) <= 0.5:
                        matched_jets_lb.append(GenJets[min_index])
                        sel_jets_lb=lead_bjets
			lead_b=sel_jets_lb
		print('matched_jet_lb :',matched_jets_lb)	
		print('sel_jet_lb:',sel_jets_lb)



		
                dRmJ_slb=[]
                for i,jet in enumerate(sublead_bjets):
                        for GenJet in GenbJets:
                                dR_Jet_Match_slb = deltaR(jet["phi"],GenJet["phi"],jet["eta"],GenJet["eta"])
                                PtRatioJ_slb=(GenJet["pt"]-jet["pt"])/(GenJet["pt"])
                                print('drJ_slb',dR_Jet_Match_slb)
                                print('PtRJ_slb',abs(PtRatioJ_slb))
                                if abs(PtRatioJ_slb) < 0.1 :
                                        dRmJ_slb.append(dR_Jet_Match_slb)
                                else:
                                        dRmJ_slb.append(200000)

                if len(dRmJ_slb) == 0 :continue # in case dRmj is empty due to empty GenbJets

                print('dRmJ_slb',dRmJ_slb)
                print('min dRmJ_slb',min(dRmJ_slb))
                #print(' ')

                min_indexJ_slb = dRmJ_slb.index(min(dRmJ_slb)) # index of the min value in dRm List

                if  min(dRmJ_slb) <= 0.5:
                        matched_jets_slb.append(GenJets[min_index])
                        sel_jets_slb=sublead_bjets
			sublead_b=sel_jets_slb
		print('matched_jet_slb :',matched_jets_slb)
		print('sel_jet_slb:',sel_jets_slb)
		if len( matched_jets_lb) or len(matched_jets_slb):
			good_event_2b=True
	'''		
      	if len(matched_jets_1b) : #or len(matched_jets_lb) or len(matched_jets_slb) :
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

    	lead_jets=sorted(RecoJets,key=lambda x:x['pt'],reverse=True)[:1] 
	sublead_jets=sorted(RecoJets,key=lambda x:x['pt'],reverse=True)[1:2]

#-----------Extract Selected Variables-----------------------------
        GPhotons+=matched_photons
        nGPhotons.append({'nGPhotons':len(GenPhotons)})
	nJets.append({'nJets':len(RecoJets)})
	nbJets.append({'nbJets':len(bJets)})
   	Sel_photons+=sel_photons
	if len(lead_b)==0:
		lead_b.append({'pt':0,'eta':0,'phi':0})
        if len(sublead_b)==0:
                 sublead_b.append({'pt':0,'eta':0,'phi':0})

   	Sel_jets+=lead_jets
	Sublead_jets+=sublead_jets
   	Sel_bjets+=lead_b
	SubLead_bJets+=sublead_b
	dRms=[]
	dRms.append({'dRm':min(dRm)})
   	DRm+=dRms
   	Met_pt.append({'pt':met_pt})
   	Met_phi.append({'phi':met_phi})
	NGbj.add(len(GenbJets))
	Labels+=labels

	Match_1b.append(len(sel_jets_1b))
	Match_2b.append(len(sel_jets_lb)+len(sel_jets_slb))
for n in nbJets:
		Number_b += n['nbJets']
for m in Match_1b:
                M_1b += m
for k in Match_2b:
                M_2b += k	
        #print('nJet',nJet)
        #print('RecoJets', RecoJets)
	#print('GenbJet',GenbJets)
	#print('bJet',bJets)
        #print('Lead:',lead_jets)
	#print('subLead:',sublead_jets)
	#print('GenPhotons',GenPhotons)
	#print('ReoPhotons',RecoPhotons)
	#print('matched :',matched_photons)
	#print('selected :',sel_photons)
	#print(' ')
	#print(' sel bjets',Sel_bjets,' # ',jentry)
	
#---------Create Dataset's list---------------------------------

written = []
biggest_len = max(len(nGPhotons),len(nJets),len(nbJets),len(GenPhotons),len(Sel_photons), len(Sel_jets),len(Sublead_jets) , len(Sel_bjets), len(Met_pt),len(Met_phi),len(DRm),len(Labels),len(Sel_bjets),len(SubLead_bJets)) #Get biggest len
#print(biggest_len)
for i in range(biggest_len): # from 0 to largest index
        temp_dict = {} #empty dict

        try:
                temp_dict['GPhoton_pt'] = GPhotons[i]['pt']
                temp_dict['GPhoton_eta'] = GPhotons[i]['eta']
                temp_dict['GPhoton_phi'] = GPhotons[i]['phi']
        except IndexError:
                temp_dict['GPhoton_pt'] =0
                temp_dict['GPhoton_eta'] =0
                temp_dict['GPhoton_phi'] =0
        try:
                temp_dict['photon_pt'] = Sel_photons[i]['pt']
                temp_dict['photon_eta'] = Sel_photons[i]['eta']
        	temp_dict['photon_phi'] = Sel_photons[i]['phi']
	except IndexError:
                temp_dict['photon_pt'] =0
                temp_dict['photon_eta'] =0
                temp_dict['photon_phi'] =0
        try:
                temp_dict['jet_pt'] = Sel_jets[i]['pt']
                temp_dict['jet_eta'] = Sel_jets[i]['eta']
                temp_dict['jet_phi'] = Sel_jets[i]['phi']
        except IndexError:
                temp_dict['jet_pt'] =0
                temp_dict['jet_eta'] =0
                temp_dict['jet_phi'] =0
        try:
                temp_dict['SLjet_pt'] = Sublead_jets[i]['pt']
                temp_dict['SLjet_eta'] = Sublead_jets[i]['eta']
                temp_dict['SLjet_phi'] = Sublead_jets[i]['phi']
        except IndexError:
                temp_dict['SLjet_pt'] =0
                temp_dict['SLjet_eta'] =0
                temp_dict['SLjet_phi'] =0
        try:
                temp_dict['bjet_pt'] = Sel_bjets[i]['pt']
                temp_dict['bjet_eta'] = Sel_bjets[i]['eta']
                temp_dict['bjet_phi'] = Sel_bjets[i]['phi']
        except IndexError:
                temp_dict['bjet_pt'] =0
                temp_dict['bjet_eta'] =0
                temp_dict['bjet_phi'] =0
  	try:
                temp_dict['SLbjet_pt'] = SubLead_bJets[i]['pt']
                temp_dict['SLbjet_eta'] = SubLead_bJets[i]['eta']
                temp_dict['SLbjet_phi'] = SubLead_bJets[i]['phi']
        except IndexError:
                temp_dict['SLbjet_pt'] =0
                temp_dict['SLbjet_eta'] =0
                temp_dict['SLbjet_phi'] =0
        try:
                temp_dict['met_pt'] = Met_pt[i]['pt']
        except IndexError:
                temp_dict['met_pt'] =0
        try:
                temp_dict['met_phi'] = Met_phi[i]['phi']
        except IndexError:
                temp_dict['met_phi'] =0
        try:
                temp_dict['dRm'] = DRm[i]['dRm']
        except IndexError:
                temp_dict['dRm'] =0
        try:
                temp_dict['nGPhotons'] = nGPhotons[i]['nGPhotons']
        except IndexError:
                temp_dict['nGPhotons'] =0
        try:
                temp_dict['nJets'] = nJets[i]['nJets']
        except IndexError:
                temp_dict['nJets'] =0
        try:
                temp_dict['nbJets'] = nbJets[i]['nbJets']
        except IndexError:
                temp_dict['nbJets'] =0
	try:
                temp_dict['Labels'] = Labels[i]['label']
        except IndexError:
                temp_dict['Labels'] =0
        written.append(temp_dict)
	


#------- Write to CSV -------------------


# field names

fields = [ 'nGphotons','ngooJets','ngoodbJets','Matched_GPhoton_pt','Matched_GPhoton_eta','Matched_GPhoton_phi','Photon_pt','Photon_eta','Photon_phi' ,'Lead_Jet_pt','Lead_Jet_eta','Lead_Jet_phi','SubLead_Jet_pt','SubLead_Jet_eta','SubLead_Jet_phi','Lead_bJet_pt','Lead_bJet_eta','LeadbJet_phi','SubLead_bJet_pt','SubLead_bJet_eta','SubLeadbJet_phi','MET_pt','MET_phi','dR_Photon_Gen_Reco','Labels']


# data rows of csv file

rows = written
with open('GFG_V3_signal_1b', 'w') as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    for row in rows:
        #r = [row[0]['pt'], row[0]['eta'], row[0]['phi'], row[0]['pt'], row[0]['eta'], row[0]['phi']]
        r = [row['nGPhotons'],row['nJets'],row['nbJets'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['photon_pt'],row['photon_eta'],row['photon_phi'], row['jet_pt'],row['jet_eta'],row['jet_phi'],row['SLjet_pt'],row['SLjet_eta'],row['SLjet_phi'],row['bjet_pt'],row['bjet_eta'],row['bjet_phi'],row['SLbjet_pt'],row['SLbjet_eta'],row['SLbjet_phi'],row['met_pt'],row['met_phi'],row['dRm'],row['Labels']]

        write.writerow(r)


#------- Check for n objects in goodParticles--------

print('Nph',Nph)   # Check for extra photons in ngoodPhotons 
#print(Nj)
print('nbJet', Nbj)
print('nGbj', NGbj)
print(M_1b)
print(M_2b)
print(Number_b)
#Match_eff=0.
Match_eff =M_1b/Number_b	
print('Match_eff',Match_eff)
