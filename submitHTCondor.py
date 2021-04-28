#!/usr/bin/env python3


#https://research.cs.wisc.edu/htcondor/python_notebook_examples/HOWTO_Submit_bag_of_jobs.html

import argparse
import os
import sys
import tempfile, uuid
import shutil
#import htcondor


parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to the file to be read. Each line will be submitted as a job")
parser.add_argument("--name", default='job', help="job name")
parser.add_argument("--qtime", default='workday', help="qtime espresso(20 dk) , longlunch(2h)")
parser.add_argument("--keep_junk", default=False, action="store_true")
parser.add_argument("--dry_run", default=False, action="store_true")
parser.add_argument("--log_dir", default="/afs/cern.ch/work/e/ecasilar/GplusbJets/logs/", help="location of log files. Make sure dir exists or jobs will be held hostage.")
parser.add_argument("--junk_dir", default="/afs/cern.ch/work/e/ecasilar/GplusbJets/junk/")
args = parser.parse_args()

file_name = args.file
job_name  = args.name if args.name else args.file
#log_dir   = args.log_dir
log_dir   = f'{args.log_dir}/log/{job_name}/'
err_dir   = f'{args.log_dir}/err/{job_name}/'
out_dir   = f'{args.log_dir}/out/{job_name}/'
qtime = args.qtime

lines = []

if not os.path.isdir(log_dir):
    print('log directory does not exist...I will make them')
    os.makedirs(log_dir)
if not os.path.isdir(err_dir):
    print('err directory does not exist...I will make them')
    os.makedirs(err_dir)
if not os.path.isdir(out_dir):
    print('out directory does not exist...I will make them')
    os.makedirs(out_dir)
with open(file_name) as f:
    for line in f.read().split("\n"):
        if not line:
            continue
        if line.lstrip().startswith("#"):
            continue
        lines.append(line)


nlines = len(lines)




from pprint import pprint


os.makedirs(args.junk_dir, exist_ok=True)
tempdir = tempfile.mkdtemp(dir=args.junk_dir)
print('job scripts created in temp dir %s'%tempdir)
print('log files can be found in %s'%log_dir)


print('first 3 jobs look like this:')
pprint(lines[:3])

template_condor = '''
Executable   = {executable}
Args         = $(ITEM)

Log    = {log_dir}/$(Cluster).$(Process).log
Output = {out_dir}/$(Cluster).$(Process).out
Error  = {err_dir}/$(Cluster).$(Process).err
request_cpus = 2
request_memory = 300MB
request_disk = 300MB
+JobFlavour = {qtime}


Queue ITEM from {file_name} 
'''


template_jobrunner =\
'''\
#!/bin/bash
echo $@
$@
'''


#template_job =\
#'''\
##!/bin/bash
#{command}
#'''
import time


condor_args = [
                '--dry_run' if args.dry_run else '', 

              ]


jobrunner = template_jobrunner

job_temp_name = uuid.uuid4().hex

fname_jobrunner    = os.path.join( tempdir, "jobrunner.sh")
with open(fname_jobrunner, 'w') as f:
    print(template_jobrunner, file=f)
    os.system("chmod +x %s"%fname_jobrunner)


#fname_condor = os.path.join( tempdir, "condor_%s.submit"%job_temp_name )
fname_condor = os.path.join( tempdir, "condor_script.submit" )
condor_script = template_condor.format( log_dir=log_dir, out_dir=out_dir,err_dir=err_dir,qtime=qtime,file_name=file_name, job_name=job_name, executable=fname_jobrunner)
with open(fname_condor, 'w') as f:
    print(condor_script, file=f)

submit_command = "condor_submit %s %s"%(fname_condor, ' '.join(condor_args) )
os.system(submit_command)
time.sleep(0.1)

#if not args.keep_junk:
#    shutil.rmtree(tempdir)
#else:
#    print("please clean the junk:\n rm -rf %s"%tempdir)
 
#print("Jobs submitted (hopefully). Put an alarm to clean the junks when the jobs are done! \n rm -rf %s"%tempdir)

