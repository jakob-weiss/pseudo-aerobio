# pseudo-aerobio
This repository contains scripts to use in conjunction with aerobio to analyze preexisting RNA-seq datasets downloaded from SRA.

## pseudo-phase-0.py
This script works with a completely and properly formatted `/NextSeq2` experiment directory to create a corresponding 
`/ExpOut` directory in which `.fastq`s are grouped and named according to parameters set in files in the expt's 
`/NextSeq2` directory, thereby mimicking the output of phase-0 of aerobio.

In addition to the normally required `/NextSeq2` structure and files, it requires a manually created
`SRR_vs_sample.csv` file to be placed in the expt's `/NextSeq2` directory. This file has, for each sample in the expt, 
the corresp SRR run accession number in the first column and the corresp sample title in the second column, as shown below:

<img src="https://raw.githubusercontent.com/weissjy/pseudo-aerobio/master/images/readme_SRR_vs_sample.jpg" align="center" height="300" width="300" >

To use, include the file in `/NextSeq2/<expt_title>`, along with `SRR_vs_sample.csv`. 
Ensure all `.fastq`s have been dumped into `/NextSeq2/<expt_title>/Data/Intensities/BaseCalls` with `SRRxxxxxxx.fastq` names.

After running this script, proceed with phase-1 of aerobio.
