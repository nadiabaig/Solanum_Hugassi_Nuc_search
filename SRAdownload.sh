

#!/bin/bash

# Replace 'accessions.txt' with the actual name of your file containing the list of SRA accessions
file="accessions.txt"

# Check if the file exists
if [ ! -f "$file" ]; then
    echo "Error: File '$file' not found."
    exit 1
fi

# Loop through each line in the file and download the SRA data
while IFS= read -r accession; do
    echo "Downloading accession: $accession"
    fastq-dump "$accession" # Replace 'fastq-dump' with the appropriate SRA Toolkit command for downloading data
done < "$file"
