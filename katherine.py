import re
import numpy as np
import pandas as pd
import argparse

#create an argument parser object
parser = argparse.ArgumentParser(description = "This script calculates information about different versions of the name 'Katehrine'")

#add positional argument for the input file
parser.add_argument("input_file", help="Name of the input file (txt)")

#parse the arguments
args = parser.parse_args()

#open the file
text = open(args.input_file).read()

#create an empty list for the output
output = []

#find all the variations of 'Katherine' and print them to a list
match_list = re.findall(r"[kKC]ath[ae]?r[iy]ne?",text)
output.extend(match_list)

#create an empty list to hold the start, end, and length variables
start_list = []
end_list = []
length_list = []

#find all the variations of 'Katerhine' and extract the start and end positions and the length of each match
run = re.finditer(r"[kKC]ath[ae]?r[iy]ne?",text)

for match in run:
    #extract the start positions
    start = match.start() + 1
    start_list.append(start)
    
    #extract the end positions
    end = match.end()
    end_list.append(end)
    
    #calculate the length
    length = (end - start) + 1
    length_list.append(length)

#add the start, end and length variables to the output list
output.extend(start_list)
output.extend(end_list)
output.extend(length_list)

#convert the output into a one-dimensional array
array = np.array(output)

#turn the array into multiple dimensions
array = array.reshape(4,8).transpose()

#construct a table
pd.DataFrame(array, columns=['hit','start','end','length'])
