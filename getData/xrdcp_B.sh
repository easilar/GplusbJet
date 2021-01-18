#!/bin/bash
filename=datasets/Run2017B-02Apr2020-v1.txt
    while read line1;
        do
        xrdcp root://cms-xrd-global.cern.ch/$line1 /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2017/data/SingleMuon/Run2017B-02Apr2020-v1/"$(basename "$line1")"
        done < "$filename"
    done 
