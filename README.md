# Solanum_Hugassi_Nuc_search
This repository contains python scripts to fetch the information (i.e nucleotide sequences, fastq reads, SNP information )stored for Solanum Hugassi including the chloroplast genome.

## Running .py scripts
Save the available scripts in your pc and use the following command to run it in a linux enviroment..
python solanum_hugassi_nuc.py

## For windows users:
Open your python IDLE, copy code and press F5.

## install prefetch to convert SRA into fastq

### 1:  Downloading the source
wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
### 2: Extract tar file
tar -xvf sratoolkit.current-ubuntu64.tar.gz
cd sratoolkit.3.0.5-ubuntu64/
export PATH=$PATH:$(pwd)/bin

### 3: Check version of the prefetch
prefetch --version

### Run the py script for fetching fastq files (Solanum_Hugassi_SRA_fastq_files.py)
No NGS data is available in NCBI SRA archive for the Solanum_Hugassii


