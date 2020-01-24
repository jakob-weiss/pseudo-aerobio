# pseudo-aerobio
This repository contains scripts to use in conjunction with aerobio to analyze preexisting RNA-seq datasets downloaded from online databases such as SRA (Sequence Read Archive) or ENA (European Nucleotide Archive).

## pseudo-phase-0.py
This script works with a complete `/NextSeq2` experiment directory to create a corresponding 
`/ExpOut` directory in which `.fastq`s are grouped and named according to parameters set in files in the expt's 
`/NextSeq2` directory, thereby mimicking the output of phase-0 of aerobio and saving time that would be spent manually renaming and copying files. To use with a certain experiment, the script should be placed in `/NextSeq2/<expt_title>`. 

In addition to the normally required `/NextSeq2` file structure (see below), it requires a manually created
`SRR_vs_sample.csv` file to be placed in `/NextSeq2/<expt_title>`. This file has, for each fastq file in the expt, 
the current `.fastq` name in the first column and the corresponding sample `.fastq` name (i.e. the desired output name) in the second column, as shown below:

<img src="https://raw.githubusercontent.com/weissjy/pseudo-aerobio/master/images/readme_SRR_vs_sample.png" align="center" height="300" width="300" >

The `.fastq` names listed in the first column should match up to the names of the `.fastq` files in `/NextSeq2/<expt_title>/Data/Intensities/BaseCalls`, as shown below:

<img src="https://raw.githubusercontent.com/weissjy/pseudo-aerobio/master/images/readme_BaseCalls.png" align="center" height="100" width="300" >

Note that these `.fastq` files should be demultiplexed beforehand. If the dataset you're working with has one `.fastq` file per sample, it's safe to assume the files are demultiplexed.

The `/NextSeq2/<expt_title>` directory should then look like this before running the script:

<img src="https://raw.githubusercontent.com/weissjy/pseudo-aerobio/master/images/example_NextSeq2_dir.png" align="center" height="50" width="300" >

To run, do `/NextSeq2/<expt_title>/pseudo-phase-0.py`. The script will take a few minutes to copy all of the `.fastq` files.

Once finished, check that the relevant directories have been properly created in `/ExpOut/<expt_title>`. In particular, check that the `.fastq` files have been copied, grouped, and renamed correctly in `/ExpOut/<expt_title>/Samples`, which should contain directories for all of the sample names listed in `/NextSeq2/<expt_title>/SampleSheet.csv`.

After running this script, proceed with phase-1 of aerobio.
