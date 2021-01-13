#!/bin/bash
export X509_USER_PROXY=$1
voms-proxy-info -all
voms-proxy-info -all -file $1

xrdcp root://cms-xrd-global.cern.ch//store/data/Run2017B/SingleMuon/NANOAOD/02Apr2020-v1/230000/EAFA98BD-2052-844D-A94C-B874536E83E7.root /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2017/data/SingleMuon/Run2017B-02Apr2020-v1/EAFA98BD-2052-844D-A94C-B874536E83E7.root

