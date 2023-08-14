


#!/bin/bash

# Replace 'fastq-dump' with the appropriate SRA Toolkit command for downloading data
download_command="/mnt/d/Softwares/sratoolkit.3.0.6-ubuntu64/bin/fastq-dump"
path="/mnt/server/Rawdata/WGS"
file="wg.txt"


# Function to download an accession
download_accession() {
    accession="$1"
    echo "Downloading accession: $accession"
    $download_command --split-files "$accession" --outdir "$path"
}

# Read the accessions from the file and call the download function in the background
while IFS= read -r accession; do
    download_accession "$accession" &
done < "$file"

# Wait for all background jobs to complete
wait

echo "Download complete!"
