#!/bin/bash
filename=./dasgo_lists/2018_MC2.txt
while read line1;
    do
    #echo $line1
    foldername=$(dirname $(dirname "$line1"))
    echo $foldername
    mkdir -p /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2018/MC/"$foldername"
    #mkdir -p ./xrdcp_lists/datasets/2018/

    (dasgoclient --query="file dataset=$line1") >>./xrdcp_lists/datasets/2018/"$foldername".txt
    filename2=./xrdcp_lists/datasets/2018"$foldername".txt
    while read line2;
    	do
	rname=$(basename "$line2")
    	echo $rname
	echo /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2018/MC"$foldername"/"$rname"
	echo $foldername
        xrdcp root://cms-xrd-global.cern.ch/"$line2" /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2018/MC"$foldername"/"$rname"
    done <"$filename2"
done <"$filename"
