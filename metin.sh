#!/bin/bash
for i in {2016,2017,2018};
do
        filename="$i".txt
        #mkdir -p /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/$i/data
        #mkdir -p /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/$i/MC
        while read line1;
    do
        a= dirname $(dirname "$line1")
        b= basename $(dirname "$line1")
        if [[  ${line1##*/} == NANOAOD ]] ;
            then
            mkdir -p /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/$i/data/$(basename $(dirname "$line1"))
            mkdir -p datasets/$i/$(basename $(dirname "$line1"))
            dasgoclient --query="file dataset=$line1" >>./datasets/$i/$(basename $(dirname "$line1"))/"$(basename $(dirname "$line1"))".txt
            filename2=datasets/$i/$(basename $(dirname "$line1"))/$(basename $(dirname "$line1")).txt
	    while read line2;
		do
		echo "$line2"
	    	xrdcp root://cms-xrd-global.cern.ch/$line2 /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/$i/data/$(basename $(dirname "$line1"))/"$(basename "$line2")"
#done
		done < "$filename2"

        else
            mkdir -p /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/$i/MC/$(dirname $(dirname "$line1"))
                        mkdir -p datasets/$i/$(dirname $(dirname "$line1"))
                        dasgoclient --query="file dataset=$line" >>./datasets/$i/$(dirname $(dirname "$line1"))/"$(dirname $(dirname "$line1"))".txt
	    filename3=datasets/$i/$(dirname $(dirname "$line1"))/$(dirname $(dirname "$line1")).txt
		while read line3;
		do
		echo "$line3"
		xrdcp root://cms-xrd-global.cern.ch/$line3 /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/$i/MC/$(dirname $(dirname "$line1"))/"$(dirname "$line3")"

		done < "$filename3"

        fi

    done < "$filename"

done