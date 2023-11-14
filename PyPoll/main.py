import os
import csv

# This is the path of the CSV file relative to this file
election_csv = os.path.join("Resources", "election_data.csv")

# Opening CSV file to read
with open(election_csv) as csvfile:

    # Reading in the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Saving the header row in case for later and to skip the header row for analysis
    csv_header = next(csvreader)
    
    # Initializing variables for each candidate and total votes
    # This will be used to enter in the unique candidate names
    candidates = []
    # This will be used to track each candidates number of votes
    cand_votes = []

    # This will iterate through the csv.reader file once and will add the candidate name to the 
    # candidates list if it's not there already and add a new item in the cand_votes list, giving their 1st vote.
    # Each time that candidate is found after, it will add one more vote to the cand_votes count for that candidate.
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            cand_votes.append(1)
        else:
            cand_votes[candidates.index(row[2])] += 1

# This calculates the total number of votes
n_votes = sum(cand_votes)

# The output_file_start is the first 4 rows of the output file to print.
output_file_start = ["Election Results", "-------------------------", \
    f"Total Votes: {n_votes}", "-------------------------"]
# The outpyut_file_end is the last 4 rows of the output file.
output_file_end = ["-------------------------", \
    f"Winner: {candidates[cand_votes.index(max(cand_votes))]}", \
    "-------------------------"]

# I originally had all 10 rows of the output file in one list to print below. Instead, I've changed it so 
# that it will work for any number of candidates, and not just 3.

# This is the output path, relative to the python file.
output_path = os.path.join("Analysis", "pypoll.txt")

# Zipping the candidate name and their count of the votes here so the callback for the print is easier. :)

zipped = zip(candidates,cand_votes)

with open(output_path, "w") as pypath:
    # This writes out the initial lines to the output file
    for item in output_file_start:
        print(item)
        pypath.write(item)
        pypath.write('\n')
    # This writes out the candidates, their percent of votes cast, and the number of votes.
    for item in zipped:
        print(f"{item[0]}: {round(100 * item[1] / n_votes, 3)}% ({item[1]})")
        pypath.write(f"{item[0]}: {round(100 * item[1] / n_votes, 3)}% ({item[1]})")
        pypath.write('\n')
    # This writes out the ending lines to the output file
    for item in output_file_end:
        print(item)
        pypath.write(item)
        pypath.write('\n')