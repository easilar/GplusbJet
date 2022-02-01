import numpy as np
import pandas as pd
from   pandas import DataFrame
import random
import os , sys

import seaborn as sns
import matplotlib.pyplot as plt

# Machine Learning
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers, optimizers, regularizers
from tensorflow.keras.layers import Flatten , Activation
from tensorflow.keras.layers import Dense
from   sklearn.preprocessing import LabelEncoder, StandardScaler, OrdinalEncoder
from   sklearn.impute import SimpleImputer
from   sklearn.model_selection import train_test_split, GridSearchCV
from   sklearn.metrics import confusion_matrix , classification_report, accuracy_score, roc_auc_score #plot_roc_curve
from   sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score, classification_report,accuracy_score, roc_auc_score
from  sklearn import datasets, metrics, model_selection, svm
import pickle

# Maths
import math
#import GetSamples
#from GetSamples import FOLDS
from optparse import OptionParser
# add GPU parlalize########################################################
from tensorflow.keras.callbacks import TensorBoard
import tensorflow.keras.backend as tfback


'''
def _get_available_gpus():
    """Get a list of available gpu devices (formatted as strings).
    # Source of this function: https://github.com/keras-team/keras/issues/13684
    # Returns
        A list of available GPU devices.
    """
    global _LOCAL_DEVICES
    if _LOCAL_DEVICES is None:
        devices = tf.config.list_logical_devices()
        tfback._LOCAL_DEVICES = [x.name for x in devices]
    return [x for x in tfback._LOCAL_DEVICES if 'device:gpu' in x.lower()]


gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[1], True)
tf.config.set_visible_devices(gpus[1], 'GPU')

tfback._get_available_gpus = _get_available_gpus
print(_get_available_gpus())
'''


# Opitons
Adam = tf.keras.optimizers.Adam
Adamax = tf.keras.optimizers.Adamax
Nadam = tf.keras.optimizers.Nadam
Adadelta = tf.keras.optimizers.Adadelta
Adagrad = tf.keras.optimizers.Adagrad
SGD = tf.keras.optimizers.SGD
RMSprop = tf.keras.optimizers.RMSprop

opt_dict={'Adam':Adam , 'Adadelta':Adadelta ,'SGD':SGD}
parser = OptionParser()
parser.add_option("--optimizer", dest="optimizer", default='Adam', action="store", help="can be Adam , Adadelta ... ")
parser.add_option("--lr", dest="lr", default="0.001",type=float, action="store", help="can be 0.1 , 0.001")
parser.add_option("--param1", dest="param1", default="0.1",type=float, action="store", help="can be 0.1, 0.01 ... ")
parser.add_option("--param2", dest="param2", default="0.1",type=float, action="store", help="can be 0.1, 0.01 ... ")
parser.add_option("--param3", dest="param3", default="0.1",type=float, action="store", help="can be 0.1, 0.01 ... ")
parser.add_option("--weights_ini", dest="weights_ini", default="uniform", action="store", help="can be uniform , ... ")
parser.add_option("--n_deep_layers", dest="n_deep_layers",type=int, default="5", action="store", help="can be 10,20 ... ")
parser.add_option("--n_neuron_layer", dest="n_neuron_layer",type=int, default="100", action="store", help="can be 100,200 ... ")
parser.add_option("--activ_func_deep", dest="activ_func_deep", default="relu", action="store", help="can be sigmoid , ... ")
parser.add_option("--activ_func_last", dest="activ_func_last", default="sigmoid", action="store", help="can be sigmoid , ... ")
parser.add_option("--DnnShape", dest="DnnShape", default='Rectangle', action="store", help="can be Rectangle , Papillon ... ")
(options, args) = parser.parse_args()

optimizer = opt_dict[options.optimizer]
lr = options.lr
param1 = options.param1
param2 = options.param2
param3 = options.param3

weights_ini = options.weights_ini
n_deep_layers = options.n_deep_layers
n_neuron_layer = options.n_neuron_layer
activ_func_deep = options.activ_func_deep
activ_func_last = options.activ_func_last
DnnShape = options.DnnShape

#import data
dfb = pd.read_csv('/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/DeepLearning/1b_loose_CSV/MergedSignalLoose.csv')
dfb['Labels'] = dfb['Labels'].apply({'s':1, 'b':0}.get)

dfb=dfb[dfb['Labels']==1]
dfb=dfb[dfb['nbJets']==1]
dfb=dfb[dfb['Photon_hoe']>0.03]

dfQ =pd.read_csv('/eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/DeepLearning/1b_loose_CSV/MergedQCDLoose.csv')
dfQ['Labels'] = dfQ['Labels'].apply({'s':1, 'b':0}.get)
dfQ['Labels'] = dfQ['Labels'].replace(1,0)
#dfb=dfb[dfb['nbJets']==1]
                                                                                                 99,1          18%
dfQ=dfQ[dfQ['Labels']==0]
dfQ=dfQ[dfQ['Photon_hoe']>0.03]
dfQ.head()

dfb_train = dfb[dfb['Iso_chg'] < 0.003]
#dfb_train = dfb[dfb.index < 200000]
dfQ_train = dfQ[dfQ['Iso_chg'] > 0.003]
dfQ_test = dfQ[dfQ['Iso_chg'] < 0.003]
print('Signal_Train: ',len(dfb_train),'QCD_Train: ',len(dfQ_train),'QCD_Test: ',len(dfQ_test) )

frames = [dfb_train, dfQ_train]
df_train = pd.concat(frames)
df_train = df_train.sample(frac=1).reset_index(drop=True )

df_train = df_train.drop(['SV_dlen', 'SV_dxy', 'SV_pt',



        'Iso_chg','nPV', 'PV_ndof', 'PV_x',
       'PV_y', 'PV_z', 'PV_chi2', 'PV_score', 'nSV',  'SV_dlenSig',
        'SV_dxySig', 'SV_pAngle', 'SV_chi2',  'SV_eta',
       'SV_phi',  'SV_ndof', 'dR_GbJet_lead',
       'dR_GJet_sublead', 'nPhotons', 'nJets', 'nbJets', 'RMatched_GPhoton_pt','dPhi_GbJet_lead',
       'RMatched_GPhoton_eta', 'RMatched_GPhoton_phi', 'RPhoton_pt',
       'RPhoton_eta', 'RPhoton_phi', 'Matched_GPhoton_pt',
       'Matched_GPhoton_eta', 'Matched_GPhoton_phi',],axis=1)

df_train.columns

dfQ_test = dfQ_test.drop([
     'SV_dlen', 'SV_dxy', 'SV_pt',


        'Iso_chg','nPV', 'PV_ndof', 'PV_x',
       'PV_y', 'PV_z', 'PV_chi2', 'PV_score', 'nSV',  'SV_dlenSig',
        'SV_dxySig', 'SV_pAngle', 'SV_chi2',  'SV_eta',
       'SV_phi',  'SV_ndof', 'dR_GbJet_lead',
       'dR_GJet_sublead', 'nPhotons', 'nJets', 'nbJets', 'RMatched_GPhoton_pt',
       'RMatched_GPhoton_eta', 'RMatched_GPhoton_phi', 'RPhoton_pt','dPhi_GbJet_lead',
       'RPhoton_eta', 'RPhoton_phi', 'Matched_GPhoton_pt',
       'Matched_GPhoton_eta', 'Matched_GPhoton_phi',],axis=1)
def get_metric (model, x_test , y_test) :

    val_loss, val_acc = model.evaluate(x_test , y_test)
    y_pred = model.predict(x_test)
    y_pred =(y_pred>0.5)
    cm = confusion_matrix(y_test, y_pred)
    sensitivity=cm[1,1]/(cm[1,1]+cm[1,0])
    specificity=cm[0,0]/(cm[0,0]+cm[0,1])
    return sensitivity , specificity , val_acc , val_loss

def get_score(model , x_train , x_test , y_train , y_test) :

    val_loss, val_acc = model.evaluate(x_test , y_test)
    model.fit(x_train, y_train, epochs=20 ,batch_size=16)
    y_pred = model.predict(x_test)
    y_pred =(y_pred>0.5)

    cm = confusion_matrix(y_test, y_pred)

    sensitivity=cm[1,1]/(cm[1,1]+cm[1,0])
    specificity=cm[0,0]/(cm[0,0]+cm[0,1])
    return sensitivity , specificity , model, val_acc , val_loss




def create_model(init_mode='random_uniform',lr=0.1, param1=0.9, optimizer='Adam',activ_func_deep = 'relu',activ_func_last = 'sigmoid'):

    model = Sequential()
    model.add(Flatten())

    model.add(Dense(125,kernel_initializer=init_mode))
    model.add(Activation(activ_func_deep))

    model.add(Dense(75,kernel_initializer=init_mode))
    model.add(Activation(activ_func_deep))

    model.add(Dense(45,kernel_initializer=init_mode))
    model.add(Activation(activ_func_deep))

    model.add(Dense(35,kernel_initializer=init_mode))
    model.add(Activation(activ_func_deep))


    model.add(Dense(10,kernel_initializer=init_mode))
    model.add(Activation(activ_func_deep))

    model.add(Dense(1, activation=activ_func_last))

    if options.optimizer in ['SGD'] :
        model.compile(loss="binary_crossentropy", optimizer = optimizer(lr=lr,momentum = param1), metrics=tf.keras.metrics.AUC())
    if options.optimizer in ['Adam'] :
        model.compile(loss="binary_crossentropy", optimizer = optimizer(lr=lr,beta_1 = param1), metrics=tf.keras.metrics.AUC())
    if options.optimizer in ['Adadelta'] :
        model.compile(loss="binary_crossentropy", optimizer = optimizer(lr=lr,rho = param1), metrics=tf.keras.metrics.AUC())
    if options.optimizer in ['Adagrad'] :
        model.compile(loss="binary_crossentropy", optimizer = optimizer(lr=lr,initial_accumulator_value= param1), metrics=tf.keras.metrics.AUC())
    if options.optimizer in ['Adamax',] :
        model.compile(loss="binary_crossentropy", optimizer = optimizer(lr=lr,beta_1 = param1), metrics=tf.keras.metrics.AUC())
    if options.optimizer in ['Nadam'] :
        model.compile(loss="binary_crossentropy", optimizer = optimizer(lr=lr,beta_1 = param1), metrics=tf.keras.metrics.AUC())
    if options.optimizer in ['Ftrl',] :
        model.compile(loss="binary_crossentropy", optimizer = optimizer(lr=lr,initial_accumulator_value= param1), metrics=tf.keras.metrics.AUC())
    if options.optimizer in ['RMSprop'] :
        model.compile(loss="binary_crossentropy", optimizer = optimizer(lr=lr,momentum = param1), metrics=tf.keras.metrics.AUC())


    return model

model_results = []
results_AUC = []
results = []
results_test =[]
# One Point
#for i,j in zip(Folds_train,Folds_test) :
print('Len DF TRain :',len(df_train))
Folds=[df_train,df_train,df_train]
for i in Folds:

    random.seed(1234122)
    random.shuffle([i])

    x_train,x_test,y_train,y_test = train_test_split(i.drop(['Labels'], axis=1), i['Labels'], test_size=0.1, random_state=55 )


    x_test_store = x_test
    y_test_store = y_test
    x_test_store = pd.DataFrame(x_test_store, columns = df_train.columns[:-1])
    y_test_store = pd.DataFrame(y_test_store ,  columns = df_train.columns[-1::])

    x_test_store['Labels'] = y_test_store

    y_train = y_train.to_numpy()
    y_test = y_test.to_numpy()

    scaler = StandardScaler().fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    df_test1 = x_test_store

    frames = [dfQ_test , df_test1]
    df_test = pd.concat(frames)
    df_test = df_test.sample(frac=1).reset_index(drop=True )

    y_test2 = df_test['Labels']
    x_test2 = df_test.drop(['Labels'], axis=1)
    y_test2 = y_test2.to_numpy()
    scaler = StandardScaler().fit(x_test2)
    x_test2 = scaler.transform(x_test2)



    model = create_model(param1 = param1,init_mode=weights_ini,optimizer=optimizer,lr=lr,activ_func_deep = activ_func_deep ,activ_func_last = activ_func_last)
                    #print(model.summary())
    model.fit(x_train, y_train, batch_size = 16, epochs = 30)
    print("[INFO] serializing network...")


    print('train_done')
    sens2 , spec2 , val_acc , val_loss = get_metric(model, x_test2 , y_test2)

                    #add val_acc average

    results_AUC.append({'AUC':val_acc})
    results.append({'sens': sens2 , 'spec':spec2})
    results_test.append({'sens': sens2 , 'spec':spec2})
print('ENNNNDDDDDD LOOOOOOOOOOOOOP')
AUC_avg = 0.
sens_avg = 0.
spec_avg = 0.
for x in results_AUC :
    AUC_avg += x['AUC']/len(results_AUC)
for x in results :
    sens_avg += x['sens']/len(results)
    spec_avg += x['spec']/len(results)
print(' ')
print('AUC average:',AUC_avg)
print('sensitivity average:',sens_avg)
print('specificity average:',spec_avg)

print('OK'*10)
model_save_name = '_optAlg:'+str(options.optimizer)+'_Learning_rate:'+str(lr)+'_Momentum:'+str(param1)+'_Weights_ini: '+str(weights_ini)+'_sens'+str(sens2)+'_spec'+str(spec2)+'_'

model_results.append({'optAlg':options.optimizer,'weights_ini':weights_ini ,'Learning_rate':lr ,'Momentum':param1 ,'activ_func_last':activ_func_last, 'activ_func_deep':activ_func_deep  ,'sens':sens_avg , 'spec': spec_avg , 'AUC_score':AUC_avg })

if val_acc > 0.97 :
    model.save_weights("/home/cms/barakat/looseGridSearch/goodModelsWeights/"+model_save_name+"_.h5")
    model.save("/home/cms/barakat/looseGridSearch/goodModels/"+model_save_name+"_")
df_GridResults = pd.DataFrame(model_results)
df_GridResults.to_csv('looseGridSearchSGD_Results.csv', mode='a', index = False, header = False)






























































