import csv
import numpy

#defines variables
# count_votes = 0
# candidates = []
voter_IDs = []
counties = []
candidates = []


#opens csv
with open('PyPoll/Resources/election_data.csv', mode = 'r')as csv_file:
    reader = csv.reader(csv_file, delimiter = ',')
    next(reader, None)
        # for lines in reader:
        #     count_votes = count_votes + 1
        #     if not candidates.__contains__(lines[1]):
        #         candidates.append(lines[1])
    for line in reader:
        voter_IDs.append(line[0])
        counties.append(line[1])
        candidates.append(line[2])
    unique_candidates = numpy.unique(candidates)
    candidate_votes = []
    for candidate in unique_candidates:
        candidate_votes.append(candidates.count(candidate))
    print(unique_candidates)
    print(candidate_votes)
    candidate_vote_percentages = []
    for index in range(len(candidate_votes)):
        candidate_vote_percentages.append(candidate_votes[index]/sum(candidate_votes)*100)

        
print(candidate_vote_percentages)
winner_index = candidate_vote_percentages.index(max(candidate_vote_percentages))
print(unique_candidates[winner_index])
print("Total Votes " + str(len(voter_IDs)))




