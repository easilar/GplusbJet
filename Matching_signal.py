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
parser.add_option("--b", dest="b", default="1", action="store", help="1b or 2b")
(options, args) = parser.parse_args()
b=int(options.b)

sample_dic=pickle.load(open("samples_ana.pkl",'rb'))
mychain_dict  =  getChain(year=2016, stype='signal', sname='G1Jet_Pt', pfile='samples_ana.pkl', datatype='all', test=False)
ch = mychain_dict[0]
number_events=ch.GetEntries()
number_events=50000

#Number of Particles in n events
Nph=set()  # N Photons per Event in goodPhotons
Nbj=set()
Nj=set()
NGbj=set()

#List of Variables for The dataset
nGPhotons=[]
GPhotons=[]
Sel_photons=[]
nJets=[]
Sel_jets=[]
Sublead_jets=[]
nbJets=[]
Sel_bjets=[]
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
	sel_jets_1b=[]
	sel_jets_lb=[]
	sel_jets_slb=[]
	lead_b=[]
	sublead_b=[]
	dRms=[]
	labels=[]

#---------- second loop : nVariables inside Particles-------------------

	for ID in range(int(nGenPart)): # Gen Photons   #List of Dict
		if ch.GetLeaf('GenPart_pdgId').GetValue(ID)==22:
			GenPhotons.append({'index':ID,'pt':ch.GetLeaf('GenPart_pt').GetValue(ID),'eta':ch.GetLeaf('GenPart_eta').GetValue(ID),'phi':ch.GetLeaf('GenPart_phi').GetValue(ID)})

	for I in range(int(nPhoton)): # Reco PHOTONS
		Photons.append({'index':I,'pt':ch.GetLeaf('goodPhoton_pt').GetValue(I),'eta':ch.GetLeaf('goodPhoton_eta').GetValue(I),'phi':ch.GetLeaf('goodPhoton_phi').GetValue(I)})

	for ID in range(int(nGenJet)): # Gen Jets   #List of Dictionary
		GenJets.append({'index':ID,'pt':ch.GetLeaf('GenJet_pt').GetValue(ID),'eta':ch.GetLeaf('GenJet_eta').GetValue(ID),'phi':ch.GetLeaf('GenJet_phi').GetValue(ID)})

        for ID in range(int(nGenJet)): # Gen Jets   #List of Dictionary
		if abs(ch.GetLeaf('GenJet_partonFlavour').GetValue(ID))==5:
                	GenbJets.append({'index':ID,'pt':ch.GetLeaf('GenJet_pt').GetValue(ID),'eta':ch.GetLeaf('GenJet_eta').GetValue(ID),'phi':ch.GetLeaf('GenJet_phi').GetValue(ID)})

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


# ------------PHOTON MATCHING INSIDE CONE dR----------------------------------------------

	dRm=[]
	for i,photon in enumerate(Photons):  # Matching GenPhoton-RecoPhoton in cone dR
		for j,GenPhoton in enumerate(GenPhotons):
			dR_Pho_Match = deltaR(photon["phi"],GenPhoton["phi"],photon["eta"],GenPhoton["eta"])
			PtRatio=(GenPhoton["pt"]-photon["pt"])/(GenPhoton["pt"])
			#print('dr',dR_Pho_Match)
			#print('PtR',abs(PtRatio))
			dRm.append({'index':j,'dR':dR_Pho_Match,'PtRatio':PtRatio })

	dRm=sorted(dRm,key=lambda x:x['dR'])

    	for i in  dRm :
            if abs(i['PtRatio']) < 0.1:
                    matched_photons.append(GenPhotons[dRm[0]['index']])
                    break
            else :
                    continue

    	if  dRm[0]['dR'] <= 0.5:
            sel_photons=Photons
	#print('matched_photons :',matched_photons)
	#print('Sel_photons:',sel_photons)

    	if len(matched_photons)   :
            good_event_Photon=True
    	if not good_event_Photon  : continue
	
#------------- 1b Matching ----------------------------------------
	
	print('GenbJets', GenbJets)
	print('bJets',bJets)

	if nbJet == 1 and b == 1 :
        	dRmJ=[]
        	for i,jet in enumerate(bJets):
                	for  j,GenJet in enumerate (GenbJets):
                        	dR_Jet_Match = deltaR(jet["phi"],GenJet["phi"],jet["eta"],GenJet["eta"])
                        	PtRatioJ=(GenJet["pt"]-jet["pt"])/(GenJet["pt"])
                 	      	print('drJ',dR_Jet_Match)
                        	print('PtRJ',abs(PtRatioJ))
				dRmJ.append({'index':j,'dR':dR_Jet_Match,'PtRatio':PtRatioJ})

        	if len(dRmJ) == 0 :continue # in case dRmj is empty due to empty GenbJets
		dRmJ=sorted(dRmJ,key=lambda x:x['dR'])
        	print('dRmJ',dRmJ)

        	for i in  dRmJ :
                	if abs(i['PtRatio']) < 0.1:
                        	matched_jets_1b.append(GenbJets[dRmJ[0]['index']])
                        break
                else :
                        continue

        	if  dRm[0]['dR'] <= 0.5:
                	sel_jets_1b=bJets
			lead_b=sel_jets_1b

          	print('matched_jet_1b :',matched_jets_1b)
		print('sel_jet_1b:',lead_b)

        	if matched_jets_1b   :
                	good_event_b=True
        	if not good_event_b  :
			pass
		
#----------------- 2b Matching ---------------------------------------------------------

	elif nbJet > 1 and b>1 :

		lead_bjets=sorted(bJets,key=lambda x:x['pt'],reverse=True)[:1]
        	sublead_bjets=sorted(bJets,key=lambda x:x['pt'],reverse=True)[1:2]

        	dRmJ_lb=[]
        	for i,jet in enumerate(lead_bjets):
            		for j,GenJet in enumerate(GenbJets):
                                dR_Jet_Match_lb = deltaR(jet["phi"],GenJet["phi"],jet["eta"],GenJet["eta"])
                                PtRatioJ_lb=(GenJet["pt"]-jet["pt"])/(GenJet["pt"])
                               	print('drJ_lb',dR_Jet_Match_lb)
                                print('PtRJ_lb',abs(PtRatioJ_lb))
				dRmJ_lb.append({'index':j,'dR':dR_Jet_Match_lb,'PtRatioJ_lb':PtRatioJ_lb})

            	if len(dRmJ_lb) == 0 :continue # in case dRmj is empty due to empty GenbJets

		dRmJ_lb=sorted(dRmJ_lb,key=lambda x:x['dR'])
            	print('dRmJ_lb',dRmJ_lb)

            	for i in  dRmJ_lb :
                	if abs(i['PtRatioJ_lb']) < 0.1:
                        	matched_jets_lb.append(GenbJets[dRmJ_lb[0]['index']])
                        	break
                	else :
                        	continue
        	if  len(matched_jets_lb) and dRm[0]['dR'] <= 0.5:
                	sel_jets_lb=lead_bjets
			lead_b=sel_jets_lb
			print('matched_jet_lb :',matched_jets_lb)
			print('sel_jet_lb:',sel_jets_lb)




            	dRmJ_slb=[]
            	for z,jt in enumerate(sublead_bjets):
                    for GenJt in GenbJets:
                                dR_Jet_Match_slb = deltaR(jt["phi"],GenJt["phi"],jt["eta"],GenJet["eta"])
                                PtRatioJ_slb=(GenJt["pt"]-jt["pt"])/(GenJt["pt"])
                                print('drJ_slb',dR_Jet_Match_slb)
                                print('PtRJ_slb',abs(PtRatioJ_slb))
				dRmJ_slb.append({'index':z,'dR':dR_Jet_Match_slb,'PtRatioJ_slb':PtRatioJ_slb})

            	if len(dRmJ_slb) == 0 :continue # in case dRmj is empty due to empty GenbJets
		dRmJ_slb=sorted(dRmJ_slb,key=lambda x:x['dR'])
            	print('dRmJ_slb',dRmJ_slb)

            	for d in  dRmJ_slb :
			print('ABS PT_SLB',abs(d['PtRatioJ_slb']))
                    	if abs(d['PtRatioJ_slb']) < 0.1:
                                matched_jets_slb.append(GenbJets[dRmJ_slb[0]['index']])
                                break
                        else :
                                continue

            	if len(matched_jets_slb) and  dRmJ_slb[0]['dR'] <= 0.5:
                        sel_jets_slb=sublead_bjets
                        sublead_b=sel_jets_slb

			print('matched_jet_slb :',matched_jets_slb)
			print('sel_jet_slb:',sel_jets_slb)
			if len( matched_jets_lb) or len(matched_jets_slb):
				good_event_2b=True
			print('lead_b',lead_b)
      		if  len(matched_jets_lb) or len(matched_jets_slb) :
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
	
        if len(matched_photons)==0:
                matched_photons.append({'pt':-999,'eta':-999,'phi':-999})
	GPhotons+=matched_photons		
        if len(GenPhotons)==0:
                nGPhotons.append({'nGPhotons':0})
	nGPhotons.append({'nGPhotons':len(GenPhotons)})		
        if len(sel_photons)==0:
                sel_photons.append({'pt':-999,'eta':-999,'phi':-999})
	Sel_photons+=sel_photons		
        if len(Jets)==0:
                nJets.append({'nJets':0})
	nJets.append({'nJets':len(Jets)})				        
        if len(bJets)==0:
                nbJets.append({'nbJets':0})
	nbJets.append({'nbJets':len(bJets)})				        
        if len(lead_jets)==0:
                lead_jets.append({'pt':-999,'eta':-999,'phi':-999})	
	Sel_jets+=lead_jets			        
        if len(sublead_jets)==0:
                sublead_jets.append({'pt':-999,'eta':-999,'phi':-999})
	Sublead_jets+=sublead_jets 
        if len(lead_b)==0:
                lead_b.append({'pt':-999,'eta':-999,'phi':-999})
	Sel_bjets+=lead_b				
        if len(sublead_b)==0:
                sublead_b.append({'pt':-999,'eta':-999,'phi':-999})
	SubLead_bJets+=sublead_b
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
    	Match_1b.append(len(sel_jets_1b))
    	Match_2b.append(len(sel_jets_lb)+len(sel_jets_slb))
	
for n in nbJets:
                Number_b += n['nbJets']
for m in Match_1b:
                M_1b += m
for k in Match_2b:
                M_2b += k

#---------Create Dataset's list---------------------------------
written=[]
biggest_len = len(GPhotons)
for i in range(biggest_len):
	temp_dict = {} #empty dict
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

	fields = [ 'nGphotons','ngooJets','ngoodbJets','Matched_GPhoton_pt','Matched_GPhoton_eta','Matched_GPhoton_phi','Photon_pt','Photon_eta','Photon_phi' ,'Lead_Jet_pt','Lead_Jet_eta','Lead_Jet_phi','SubLead_Jet_pt','SubLead_Jet_eta','SubLead_Jet_phi','Lead_bJet_pt','Lead_bJet_eta','Lead_bJet_phi','MET_pt','MET_phi','dR_Photon_Gen_Reco','Labels']



	rows = written
	with open('M1b_signal.csv', 'w') as f:

    		write = csv.writer(f)
    		write.writerow(fields)
    		for row in rows:
        		r = [row['nGPhotons'],row['nJets'],row['nbJets'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['photon_pt'],row['photon_eta'],row['photon_phi'], row['jet_pt'],row['jet_eta'],row['jet_phi'],row['SLjet_pt'],row['SLjet_eta'],row['SLjet_phi'],row['bjet_pt'],row['bjet_eta'],row['bjet_phi'],row['met_pt'],row['met_phi'],row['dRm'],row['Labels']]

        		write.writerow(r)
elif b>1:

        fields = [ 'nGphotons','ngooJets','ngoodbJets','Matched_GPhoton_pt','Matched_GPhoton_eta','Matched_GPhoton_phi','Photon_pt','Photon_eta','Photon_phi' ,'Lead_Jet_pt','Lead_Jet_eta','Lead_Jet_phi','SubLead_Jet_pt','SubLead_Jet_eta','SubLead_Jet_phi','Lead_bJet_pt','Lead_bJet_eta','Lead_bJet_phi','SubLead_bJet_pt','SubLead_bJet_eta','SubLeadbJet_phi','MET_pt','MET_phi','dR_Photon_Gen_Reco','Labels']



        rows = written
        with open('M2b_signal.csv', 'w') as f:

        	write = csv.writer(f)
        	write.writerow(fields)
        	for row in rows:
                	r = [row['nGPhotons'],row['nJets'],row['nbJets'],row['GPhoton_pt'],row['GPhoton_eta'],row['GPhoton_phi'],row['photon_pt'],row['photon_eta'],row['photon_phi'], row['jet_pt'],row['jet_eta'],row['jet_phi'],row['SLjet_pt'],row['SLjet_eta'],row['SLjet_phi'],row['bjet_pt'],row['bjet_eta'],row['bjet_phi'],row['SLbjet_pt'],row['SLbjet_eta'],row['SLbjet_phi'],row['met_pt'],row['met_phi'],row['dRm'],row['Labels']]

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
print(M_1b)
print(M_2b)
print(Number_b)
Match_eff =(M_1b+M_2b)/Number_b
print('Match_eff',Match_eff)
