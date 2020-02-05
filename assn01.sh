#! /bin/bash

#assn01-1
find . -name nad*

# assn01-2
top
#Q1: 2.0%
#Q2: PhysMem: 18G used (2763M wired), 14G unused

#assn01-3
grep misc_feature watermelon_files/watermelon.gff | sort -k7gr > watermelon_files/IR_regions.gff

#assn01-4
grep chloroplast watermelon_files/watermelon.gff | grep IR | wc -l; grep chloroplast watermelon_files/watermelon.gff | grep -v IR | wc -l
#More chloroplast regions come from outside the IR

#assn01-5
cat watermelon_files/watermelon_nt/*.fasta | tr '\n' '\t' | tr '>' '\n' | grep GGATCC | grep -v GAATTC | sed 's/^/>/' | tr '\t' '\n' | grep '\S' | less -SN

#assn01-6
head -n 1000 example_files/shaver_etal.csv | tail -n 501 > example_files/shaver_etal_500to1000.csv

#assn01-7
sort -k3 example_files/fruit.txt | sort -srk2,2 | column -t

echo done