#! /usr/bin/env python3

import csv
import argparse

#create an argument parser object
parser = argparse.ArgumentParser(description = "This script parses a GFF file and extracts information")

#add positional argument for the input position in the Fib sequence
parser.add_argument("GFF", help="Name of the GFF file")
parser.add_argument("FASTA", help="Name of the fasta file")

#parse the arguments
args = parser.parse_args()

#create empty lists to store the variables
gene_names = []
start_positions = []
end_positions = []

#create a csv reader object
with open(args.GFF, 'r') as gff:
    
    #create csv.reader object
    reader = csv.reader(gff, delimiter="\t")
    
    #access data in the GFF file
    for field in reader:
        
        #get start positions
        start_positions.append(field[3])
        
        #get end positions
        end_positions.append(field[4])
        
        #get gene names
        gene_field = field[8].split(" ; ")
        gene = gene_field[0].split("Gene ")
        gene_names.append(gene[1])
            
#sort the list of gene names alphabetically
gene_names = sorted(gene_names)   

#print the final lists with data
print(gene_names)
print(start_positions)
print(end_positions)

#open the fasta file
FASTA = open(args.FASTA,"r")