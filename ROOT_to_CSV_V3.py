import ROOT
import helper
from array import array
from helper import *
import csv
import json
import os
import pickle
import operator

sample_dic=pickle.load(open("samples_ana.pkl",'rb'))
sdic=sample_dic[2016]['signal']['G1Jet_Pt']['G1Jet_Pt_250To400_NOExt']
ch=ROOT.TChain("Events")
ch.Add(sdic['dir']+"/*.root")

number_events=ch.GetEntries()
number_events=1000

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
Met_pt=[]
Met_phi=[]
DRm=[]



#--------- First loop : Looping on Events ---------


for jentry in range(number_events):
	ch.GetEntry(jentry)
	good_event=False
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

	if nPhoton>1: continue
	if nbJet>1: continue

	#lists of variables per event
	RecoPhotons=[]          # kin of Reco Photons
   	RecoJets=[]             # kin of Reco Jets
   	GenJets=[]              # kin of G jets
	GenbJets=[]
   	GenPhotons=[]           # kin of Gen Particles
   	bJets=[]
   	sel_photons=[]
   	hpt_jet=[]
     
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
   

	print('event#',jentry)
	#if len(GenbJets) != 0:
		#print('OK')
	#print("LenGenJets---LenGenPhotons----LenRecoJets----LenGenbJets----LenRecobJets---LenRecoPhotons")
   	#print(len(GenJets)," " , len(GenPhotons) , " ",len(RecoJets),' ',len(GenbJets),' ',len(bJets)," ",len(RecoPhotons))

# ------------PHOTON MATCHING INSIDE CONE dR----------------------------------------------
	dR=[]
	dRm=[]	
	for i,photon in enumerate(RecoPhotons):  # Matching GenPhoton-RecoPhoton in cone dR
		for GenPhoton in GenPhotons:
			dR_Pho_Match = deltaR(photon["phi"],GenPhoton["phi"],photon["eta"],GenPhoton["eta"])
			PtRatio=(GenPhoton["pt"]-photon["pt"])/(GenPhoton["pt"])
			dR.append((dR_Pho_Match))
			#print('dr',dR_Pho_Match)
			#print('PtR',abs(PtRatio))
			if abs(PtRatio) < 0.1 :
				dRm.append(min(dR))
			else:
				dRm.append(200000)
					
	
	#print('dRm',dRm)
	#print('min dRm',min(dRm))
	#print(' ')

	min_index = dRm.index(min(dRm)) # index of the min value in dRm List

	matched_photons=[]
	if  min(dRm) <= 0.5:
		matched_photons.append(GenPhotons[min_index]) 
	#print('matched :',matched_photons)

        sel_photon=[]
        if min( dRm) <= 0.5:	
        	sel_photons=RecoPhotons
	
	PtRatio=0.
	for s in matched_photons:
		for i in sel_photons:
			PtRatio=(s["pt"]-i["pt"])/(s["pt"])
	#print(abs(PtRatio))


#----------- b Jet Matching --------------------------------------

        dRJ=[]
        dRmJ=[]
        for i,jet in enumerate(bJets): 
                for GenJet in GenbJets:
                        dR_Jet_Match = deltaR(jet["phi"],GenJet["phi"],jet["eta"],GenJet["eta"])
                        PtRatioJ=(GenJet["pt"]-jet["pt"])/(GenJet["pt"])
                        dRJ.append((dR_Jet_Match))
                        print('drJ',dR_Jet_Match)
                        print('PtRJ',abs(PtRatioJ))
                        if abs(PtRatioJ) < 0.1 :
                                dRmJ=dRJ
                        else:
                                dRmJ.append(200000)

	if len(dRmJ) == 0 : # in case dRmj is empty
                continue

        print('dRmJ',dRmJ)
        print('min dRmJ',min(dRmJ))
        #print(' ')

        min_indexJ = dRmJ.index(min(dRmJ)) # index of the min value in dRm List

        matched_jets=[]
        if  min(dRmJ) <= 0.5:
                matched_jets.append(GenJets[min_index])
        print('matched_jet :',matched_jets)

        sel_jets=[]
        if min( dRmJ) <= 0.5:
                sel_jets=bJets
	
	# TO GET ONE ROW PER EVENT:
        #lead_bjets=sorted(sel_jets,key=lambda x:x['pt'],reverse=True)[:1]
        #sublead_bjets=sorted(sel_jets,key=lambda x:x['pt'],reverse=True)[1:2]


#------------- Labeling -------------------------------------------

	#s=[]
	#b=[]
	#labels=[]
	#if good event labels.append s
	#if not good event labels.append b

#------------- Selecting good event-------------------------------

        if PtRatio < 0.1 and min(dRm)<0.5  :
                good_event=True #only after b matching
        if not good_event  : continue
        #if len(dRm) == 0 : # having ptRatio >= 0.12 so dRm empty list
                #continue



	
#------------- Getting Leading & SubLeading Jet---------------------

    	lead_jets=sorted(RecoJets,key=lambda x:x['pt'],reverse=True)[:1] 
	sublead_jets=sorted(RecoJets,key=lambda x:x['pt'],reverse=True)[1:2]
	pt_jet=[]
	for i in range(len(RecoJets)):
		pt_jet=RecoJets[i]['pt']
	        #print('pt_jets:',pt_jet)

#-----------Extract Selected Variables-----------------------------
        GPhotons+=matched_photons
        nGPhotons.append({'nGPhotons':len(GenPhotons)})
	nJets.append({'nJets':len(RecoJets)})
	nbJets.append({'nbJets':len(bJets)})
   	Sel_photons+=sel_photons
	if len(bJets)==0:
		bJets.append({'pt':0,'eta':0,'phi':0})
   	Sel_jets+=lead_jets
	Sublead_jets+=sublead_jets
   	Sel_bjets+=bJets
	dRms=[]
	dRms.append({'dRm':min(dRm)})
   	DRm+=dRms
   	Met_pt.append({'pt':met_pt})
   	Met_phi.append({'phi':met_phi})
	NGbj.add(len(GenbJets))
        #print('nJet',nJet)
        #print('RecoJets', RecoJets)
	print('GenbJet',GenbJets)
	print('bJet',bJets)
        #print('Lead:',lead_jets)
	#print('subLead:',sublead_jets)
	#print('GenPhotons',GenPhotons)
	#print('ReoPhotons',RecoPhotons)
	#print('matched :',matched_photons)
	#print('selected :',sel_photons)
	print(' ')
	#print(' sel bjets',Sel_bjets,' # ',jentry)
	
#---------Create Dataset's list---------------------------------

written = []
biggest_len = max(len(Sel_photons), len(Sel_jets),len(Sublead_jets) , len(Sel_bjets), len(Met_pt),len(Met_phi),len(DRm)) #Get biggest len
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
        written.append(temp_dict)



#------- Write to CSV -------------------


# field names

fields = [ 'nGphotons','ngooJets','ngoodbJets','Matched_GPhoton_pt','Matched_GPhoton_eta','Matched_GPhoton_phi','Photon_pt','Photon_eta','Photon_phi' ,'Lead_Jet_pt','Lead_Jet_eta','Lead_Jet_phi','SubLead_Jet_pt','SubLead_Jet_eta','SubLead_Jet_phi','bJet_pt','bJet_eta','bJet_phi','MET_pt','MET_phi','dR_Photon_Gen_Reco']


# data rows of csv file

rows = written
with open('GFG', 'w') as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    for row in rows:
        #r = [row[0]['pt'], row[0]['eta'], row[0]['phi'], row[0]['pt'], row[0]['eta'], row[0]['phi']]
        r = [row['nGPhotons'],row['nJets'],row['nbJets'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['photon_pt'],row['photon_eta'],row['photon_phi'], row['jet_pt'],row['jet_eta'],row['jet_phi'],row['SLjet_pt'],row['SLjet_eta'],row['SLjet_phi'],row['bjet_pt'],row['bjet_eta'],row['bjet_phi'],row['met_pt'],row['met_phi'],row['dRm']]

        write.writerow(r)


#------- Check for n objects in goodParticles--------

print('Nph',Nph)   # Check for extra photons in ngoodPhotons 
#print(Nj)
print('nbJet', Nbj)
print('nGbj', NGbj)
	
