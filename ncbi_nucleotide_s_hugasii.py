###################################################################
###                   Author: Nadia Baig                        ###
###                   Dated: 04-07.2023                         ###
###################################################################

import os
os.chdir('/1data/Nadia/BNA_test')
#downloading all information in ncbi nuc for Solanum HUgasii
from Bio import Entrez, SeqIO

# Set your email address (required by NCBI)
Entrez.email = "xyz@gmail.com"   #change this with your email address

# Search for sequences related to Solanum hougasii
search_term = "Solanum hougasii"
search_handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=108) #as I found 108 records in NCBI Nucleotide database
search_results = Entrez.read(search_handle) #list of solanum HUgassi keywords in NCBI SRA database
search_handle.close()

# Retrieve the sequence records
ids = search_results["IdList"]
records = []
for seq_id in ids:
    handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    records.append(record)
''' Not necessary to print it.. If you wish you can do it. It will print the ID, Description and Fasta sequence
# Process the retrieved records
for record in records:
    print("ID:", record.id)
    print("Description:", record.description)
    print("Sequence:", record.seq)
    print("")
'''

# Save the fasta files
for record in records:
    filename = record.id + ".fasta"
    with open(filename, "w") as file:
        SeqIO.write(record, file, "fasta")
        print(f"Saved {filename}")

