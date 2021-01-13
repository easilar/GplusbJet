#!/bin/bash
filename=2018.txt
while read line1;
    do
    #echo $line1
    foldername=$(basename $(dirname "$line1"))
   # echo $foldername
    (dasgoclient --query="file dataset=$line1") >>./"$foldername".txt
    filename2="$foldername".txt
    while read line2;
    	do
	rname=$(basename "$line2")
    	#echo $rname
	#echo $line2
	#echo $foldername
        echo xrdcp root://cms-xrd-global.cern.ch/"$line2" /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2018/data/SingleMuon/"$foldername"/"$rname"
    done <"$filename2"
done <"$filename"
