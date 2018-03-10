# Modules
import os
import csv

# Build initial vote count and percent vote lists
def list_builder():
    for candidate in range(candidate_count):
        individual_vote_count.append(0)
        percent_vote.append(0)

# Tally votes for each candidate Pt 2
def individual_vote_counter(row_num):
    for i in range(candidate_count):
        if row_num[2] == candidates[i]:
            individual_vote_count[i] += 1



# Prompt user for dataset
dataset = input('What dataset would you like to test?  (election_data_1.csv or election_data_2.csv)  ')

# Set path for file
csvpath = os.path.join('raw_data', dataset)

# Results storage
vote_count = 0
candidates = []
individual_vote_count = []
percent_vote = []

# Initiate the .csv reader
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Skip the header
    next(csvreader, None)

# Iterate through the .csv file
    for rows in csvreader:

# Count total votes
        vote_count += 1

# List the candidates
        if rows[2] not in candidates:
            candidates.append(rows[2])

# It's an imprtant number.  It deserves its own variable
candidate_count = int(len(candidates))

list_builder()

# Tally votes for each candidate Pt 1
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        individual_vote_counter(row)

# Finding each candidate's percentage of the votes
for k in range(candidate_count):
    percent_vote[k] = round(((individual_vote_count[k]/vote_count) * 100), 2)

# Finding the winner
winning_index = individual_vote_count.index(max(individual_vote_count))
winner = candidates[winning_index]

# Print results
print('')
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(vote_count))
print('-------------------------')

for j in range(candidate_count):
    print(str(candidates[j] + ': ' + str(percent_vote[j]) + '% ' + '(' + str(individual_vote_count[j]) + ')'))

print('-------------------------')
print('Winner: ' + str(winner))
print('-------------------------')
