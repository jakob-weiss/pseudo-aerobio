#!/usr/bin/env python

import csv, numpy, os, shutil, io
from subprocess import call
from optparse import OptionParser

options = OptionParser(usage='%prog [-g]',
                       description="Specify -gz for working with gzip files")

options.add_option("-g",action="store_true",dest="gzipped", default=False)

opts, args = options.parse_args()
iszipped = opts.gzipped

# get expname from exp-samplesheet
with io.open("Exp-SampleSheet.csv", "r", encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=",")
    expSheet = numpy.array(list(reader)).astype(str)

expName = expSheet[0,2]
    
# get rep names and sample tags from samplesheet
with io.open("SampleSheet.csv", "r", encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=",")
    sampleSheet = numpy.array(list(reader)).astype(str)

repNames = sampleSheet[2:None,1]
sampleTags = sampleSheet[2:None,2]

repDictionary = dict(zip(sampleTags, repNames))

# make ExpOut directories according to rep names
os.chdir("/ExpOut")
call("mkdir -p " + expName + "/Samples", shell=True)
os.chdir(expName + "/Samples")
for repName in repNames:
    call("mkdir " + repName, shell=True)
os.chdir("/ExpOut/" + expName)
call("mkdir -p Out/Rep/Bams", shell=True)
call("mkdir Out/Rep/Charts", shell=True)
call("mkdir Out/Rep/Fcnts", shell=True)

# copy fastqs from NextSeq2 to ExpOut according to sample names
os.chdir("/NextSeq2/" + expName)
with io.open("SRR_vs_sample.csv", "r", encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=",")
    srr2Sample = numpy.array(list(reader)).astype(str)

i=0
for sampleName in srr2Sample[:,1]:
    sheetIndex = expSheet[:,1].tolist().index(sampleName)
    tempi7Tag = expSheet[sheetIndex,2]
    tempi5Tag = expSheet[sheetIndex,3]
    if iszipped:
        shutil.copy("/NextSeq2/" + expName + "/Data/Intensities/BaseCalls/" + srr2Sample[i,0] + ".fastq.gz", "/ExpOut/" + expName + "/Samples/" + repDictionary[tempi7Tag] + "/" + sampleName + "-" + tempi5Tag + ".fastq.gz")
    else:
        shutil.copy("/NextSeq2/" + expName + "/Data/Intensities/BaseCalls/" + srr2Sample[i,0] + ".fastq", "/ExpOut/" + expName + "/Samples/" + repDictionary[tempi7Tag] + "/" + sampleName + "-" + tempi5Tag + ".fastq")
    i+=1
    
