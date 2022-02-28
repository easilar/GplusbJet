import pickle
import pandas as pd
import numpy as np

data = pd.read_csv("SF_files/wp_deepJet_106XUL17_v3.csv")
data_central = data[data['sysType'] == 'central']
btag_SF_dict = {}
print(data.columns)
for index, row in data_central.iterrows():
    pt_range = (row['ptMin'   ],row['ptMax'   ])
    eta_range = (row['etaMin'   ],row['etaMax'   ])
    jet_flavor = row['jetFlavor']
    disc_range = (row['discrMin'   ],row['discrMax'   ])
    if not jet_flavor in btag_SF_dict.keys(): btag_SF_dict[jet_flavor] = {}
    if not pt_range in btag_SF_dict[jet_flavor].keys(): btag_SF_dict[jet_flavor][pt_range] = {}
    if not eta_range in btag_SF_dict[jet_flavor][pt_range].keys(): btag_SF_dict[jet_flavor][pt_range][eta_range] = {}
    if not disc_range in btag_SF_dict[jet_flavor][pt_range][eta_range].keys(): btag_SF_dict[jet_flavor][pt_range][eta_range][disc_range]={}
    btag_SF_dict[jet_flavor][pt_range][eta_range][disc_range]['formula'] = row['formula ']

for f in btag_SF_dict.keys():
	print(f)
	pt_lis_UB = np.array([x[1] for x in sorted(btag_SF_dict[f].keys(),key=lambda x:x[1])])
	pt_lis_LB = np.array([x[0] for x in sorted(btag_SF_dict[f].keys(),key=lambda x:x[0])])
	btag_SF_dict[f]["pt_lis_UB"] = pt_lis_UB
	btag_SF_dict[f]["pt_lis_LB"] = pt_lis_LB
	for pt in btag_SF_dict[f].keys():
		if len(pt) > 2 : continue
		print(pt)
		eta_list = btag_SF_dict[f][pt].keys()
		eta_lis_UB = np.array([x[1] for x in sorted(eta_list,key=lambda x:x[1])])
		eta_lis_LB = np.array([x[0] for x in sorted(eta_list,key=lambda x:x[0])])
		btag_SF_dict[f][pt]["eta_lis_UB"] = eta_lis_UB
		btag_SF_dict[f][pt]["eta_lis_LB"] = eta_lis_LB
		for eta in btag_SF_dict[f][pt].keys():
			if len(eta) > 2 : continue
			print(eta)
			disc_list = btag_SF_dict[f][pt][eta].keys()
			disc_lis_UB = np.array([x[1] for x in sorted(disc_list,key=lambda x:x[1])])
			disc_lis_LB = np.array([x[0] for x in sorted(disc_list,key=lambda x:x[0])])
			btag_SF_dict[f][pt][eta]["disc_lis_UB"] = disc_lis_UB
			btag_SF_dict[f][pt][eta]["disc_lis_LB"] = disc_lis_LB

pickle.dump(btag_SF_dict, open("SF_files/btag_SF_17UL.pkl", "wb"))
