#!/bin/bash
filename=gjet.txt
while read line; do
xrdcp root://cms-xrd-global.cern.ch/$line /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/MC/GJet_Pt/$line
done < $filename
