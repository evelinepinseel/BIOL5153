#! /usr/bin/python3

##Python script to extract gene names from a GFF file

#open & read the GFF file
gff = open("watermelon.gff","r")

#create an empty list to store the gene names
gene_list = []

#extract the gene names from the GFF file and store them in a list
for line in gff:
    columns = line.rstrip("\n").split("\t")
    gene_info = columns[8].splitlines()
    
    for line in gene_info:
        gene_column = line.rstrip("\n").split(";")
        gene_info2 = gene_column[0].splitlines()
        
        for line in gene_info2:
            gene_split = line.rstrip("\n").split(" ")
            gene_list.append(gene_split[1])

#sort the list of gene names alphabetically
gene_list = sorted(gene_list)   

#remove "similar" from the list of gene names
gene_list = [item for item in gene_list if item != "similar"]

#remove double occurances of gene names from the list
genes = [] 
for gene in gene_list: 
    if gene not in genes: 
        genes.append(gene) 

#print the final gene list
print(genes)