#!/bin/bash
filename=2017.txt
while read line1;
    do
    echo $line1
    foldername=$(basename $(dirname "$line1"))
    echo $foldername
    fname=$(dasgoclient --query="file dataset=$line1")"\n"
    echo $fname

	echo $(basename "$fname")
    #xrdcp root://cms-xrd-global.cern.ch/"$fname" /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2017/data/SingleMuon/"$foldername"/"$(basename "$fname")"
	
done <"$filename"
