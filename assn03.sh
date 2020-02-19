#! /bin/bash

# assn03-1
for number in {808..8008}; do echo TR-$number; done > numbers.txt

# assn03-2
alias cl='clear'
alias razor='ssh eapinsee@razor.uark.edu'
alias trestles='ssh eapinsee@trestles.uark.edu'
alias pinnacle='ssh eapinsee@pinnacle.uark.edu'

# assn03-3
ls gene_trees/ | grep "\.fasta" | wc -l
# 15085

# assn03-4
ls gene_trees/ | grep "\.tre" | wc -l
# 14640

# assn03-5
ls gene_trees/ | grep "\.sched" | wc -l
# 15262

# assn03-6
ls gene_trees/ | grep "\.tre" | sed "s/_raxml.tre//" > tre_names.txt; ls gene_trees/ | grep "\.fasta" | sed "s/.fasta//" > fasta_names.txt; diff tre_names.txt fasta_names.txt | grep ">" | wc -l
# 445

# assn03-7
for i in gene_trees/*sched;do grep -l "Program Return Code: 0" $i;done | wc -l
#15217 successful jobs
for i in gene_trees/*sched;do grep -L "Program Return Code: 0" $i;done | wc -l
#45 unsuccessful jobs

# assn03-8
ls gene_trees/ | grep "\.tre" | sed "s/_raxml.tre//" > tre_names.txt; ls gene_trees/ | grep "\.fasta" | sed "s/.fasta//" > fasta_names.txt; diff tre_names.txt fasta_names.txt | grep ">" | sed "s/> //" > failed_files.txt;
for i in $(cat failed_files.txt);do echo "write_raxml_job_script.py $i.fasta > $i.pbs";done > job_scripts.txt

echo done
