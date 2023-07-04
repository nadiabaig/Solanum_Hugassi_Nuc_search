from Bio import Entrez

# Set your email address (required by NCBI)
Entrez.email = "nadiabeg.comsats@gmail.com"

# Set the species name
species_name = "Solanum hougasii"  # Replace with the actual species name

# Search for SNPs related to the species
search_term = f"{species_name} [ORGN]"
search_handle = Entrez.esearch(db="snp", term=search_term, retmax=10)
search_results = Entrez.read(search_handle)
search_handle.close()

# Print the search results
print("Search Results:")
print(search_results)

# Retrieve SNP information for each SNP ID
snp_ids = search_results["IdList"]
for snp_id in snp_ids:
    # Retrieve SNP information using ESummary
    handle = Entrez.esummary(db="snp", id=snp_id)
    snp_record = Entrez.read(handle)
    handle.close()

    if snp_record:
        snp_info = snp_record[0]

        snp_id = snp_info["Rs"]
        snp_gene = snp_info["GENE"]
        snp_description = snp_info["DESC"]

        print("SNP ID:", snp_id)
        print("Gene:", snp_gene)
        print("Description:", snp_description)
        print("")

    else:
        print("SNP information not found for SNP ID:", snp_id)
        print("")
