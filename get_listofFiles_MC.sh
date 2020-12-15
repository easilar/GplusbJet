slist='
GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8_20M/
QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/
TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/
TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/
ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8
ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/
ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/
ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/
ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/
TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'

#mkdir /eos/user/e/ecasilar/SMPVJ_Gamma_BJETS/MC_filtered/${mc};

for mc in $slist;
do
for x in `ls /eos/cms/store/group/phys_smp/AnalysisFramework/Baobab/Metin/gammaplusb/2016/MC/${mc}`; 
do 
echo python /afs/cern.ch/work/e/ecasilar/GplusbJets/filter_MC.py --path=${mc}  --filename=$x ; 
done
done
