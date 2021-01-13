#!/bin/bash
filename=2017_MC.txt
while read line1;
    do
    #echo $line1
    foldername=$(dirname $(dirname "$line1"))
    echo $foldername
    #mkdir -p /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2017/MC/"$foldername"
    mkdir -p ./datasets/2017/

    (dasgoclient --query="file dataset=$line1") >>./datasets/2017/"$foldername".txt
    filename2=./datasets/2017"$foldername".txt
    while read line2;
    	do
	rname=$(basename "$line2")
    	echo $rname
	echo /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2017/MC"$foldername"/"$rname"
	echo $foldername
        xrdcp root://cms-xrd-global.cern.ch/"$line2" /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2017/MC"$foldername"/"$rname"
    done <"$filename2"
done <"$filename"
