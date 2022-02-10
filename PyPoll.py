#Add our dependencies
import csv
import os

# Define path to input file
input_file_path = os.path.join("resources","election_results.csv")

# Define path to output file
output_file_path = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# 2. Candidate List
candidate_options = []

# 3. Dictionary to hole candiate vote totals
candidate_votes = {}

# Open election file
with open(input_file_path) as election_data:

    #Read the file and load data to file_reader object (list like)
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Loop through ever row in file_reader
    for row in file_reader:
        # Add to total vote count
        total_votes += 1

        # Read candidate name and save
        candidate_name = row[2]

        # Use member functions to add candidate to list
        if candidate_name not in candidate_options:

            # Add candidate to the candidate list
            candidate_options.append(candidate_name)

            # Create a candidate key in the candidate dictionary
            candidate_votes[candidate_name] = 0

        # Add a vote each time the candidate appears
        candidate_votes[candidate_name] += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)

#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentag of vots each candiat won
# 4. The toal number of votes each candidate won
# 5. The winner of the election based on popular vote.

