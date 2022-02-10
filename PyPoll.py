import csv
import os

# The path to the file 
file_path = os.path.join("resources","election_results.csv")

# Open the file using with
with open(file_path) as election_data:
    print(election_data)


# File to save
path_to_output_file = os.path.join("analysis","election_analysis.txt")

# Create file using with
with open(path_to_output_file,"w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentag of vots each candiat won
# 4. The toal number of votes each candidate won
# 5. The winner of the election based on popular vote.

