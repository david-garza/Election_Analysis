# Election Analysis
## Overview of Election Audit
This simulated election audit performs voter counts by candidate, by county, and determines the winner of the election. 
### Statistics Computed by this Script
Several statistics are computed and printed to the terminal and saved to a text file called analysis\election_analysis.txt
1. Total number of votes
2. Name of counties where at least 1 vote was cast
3. Percentage of votes per county
4. Total number of votes per county
5. Identifies the county with the largest voter turnout
6. Name of candidates where at least 1 vote was cast
7. Percentage of votes cast for candidate
8. Total number ov votes cast for candidate
9. Determines the winning candidate by popular vote
10. Winning percentage of the vote
11. Winning total votes
## Election Audit Results
The results for the Colorado election are listed below:
* There were 369,711 votes cast in the election.
* Voter turnout by county:

    1. Jefferson: 10.5% (38,855)
    2. Denver: 82.8% (306,055)
    3. Arapahoe: 6.7% (24,801)

*  Denver county had the largest turnout with 306,055 voters.
* Votes cast per each candidate:

    1. Charles Casper Stockham: 23.0% (85,213)
    2. Diana DeGette: 73.8% (272,892)
    3. Raymon Anthony Doane: 3.1% (11,606)

* The winning candidate is Diana DeGette with 73.8% of the vote equaling 272,892 votes cast.

## Election Audit Summary
This script is pretty generic and can be used to tally vote totals by county and candidate given any CSV file that has county and candidate as the 2nd and 3rd column respectfuly. The capability of this file can be expanded in the following ways.

### Modifications
1. If the provided CSV file includes additional columns such as polling locations, voting method, etc then the column index for county and candiate will have to be updated to match the correct column in the provided CSV file.

2. file_to_load path can be updated to load any file with any name.

3. Using the NOT IN membership function, the code could be modified to deterine if each ballot ID is unique. This could be used to increase election integrity and verify that each ballot was only used and counted once.

4. The write to file statements can be modified to create two CSV files. One for vote counts by county and one vote counts by candidate. This would create two CSV of data that are distinct (county by row and candidate by row) and can be loaded up into Excel for further anaylsis / plotting.