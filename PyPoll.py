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

# 4. Winning Candidate and Trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
    
    # Winning calculation

print(f"Total votes cast: {total_votes:,}")

# Find the percentage of votes
for candidate in candidate_options:
    votes = candidate_votes[candidate]
    percentage = votes/total_votes*100
    print(f"{candidate}: {percentage:.1f}% ({votes:,})")

    # Determine the winning candidate
    if (votes>winning_count) and (percentage>winning_percentage):
        #if condition is true set winning variables to this value
        winning_count = votes
        winning_percentage = percentage
        winning_candidate = candidate

# Prin the winning candidate
print(
    f"-------------------------\n",
    f"Winner\n",
    f"-------------------------\n",
    f"Candidate: {winning_candidate}\n",
    f"Percentage: {winning_percentage:.1f}%\n",
    f"Votes: {winning_count:,}\n")

# Module code, doesn't produce indent
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentag of vots each candiat won
# 4. The toal number of votes each candidate won
# 5. The winner of the election based on popular vote.

