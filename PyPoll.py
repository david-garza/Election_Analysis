#Add our dependencies
import csv
import os

# Define path to input file
input_file_path = os.path.join("resources","election_results.csv")

# Define path to output file
output_file_path = os.path.join("analysis","election_analysis.txt")

# OPen electio file
with open(input_file_path) as election_data:

    #Read the file and load data to file_reader object (list like)
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentag of vots each candiat won
# 4. The toal number of votes each candidate won
# 5. The winner of the election based on popular vote.

