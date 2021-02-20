# import csv
# from collections import Counter

# with open("Resources/election_data.csv", "r") as election_data:
#     csv_reader = csv.reader(election_data)
#     next(csv_reader)

#     candidates_dic={}
#     total_votes = 0
#     candidates_column=[]
#     unique_names=[]
#     candidate=0
#     for row in csv_reader:
#         candidates=row[2]
#         if candidates in dict.keys():
#             #if you found candidates increase the count by one 
#             candidates_column.append(row[2])

#         else:
#             #add the candidates to dict
#         #unique_names=set(candidates_column)
#         len(candidates_column)
#         # candidates_column.count(unique_names[i])

# # print(len)

import csv
import os
csvpath = os.path.join('Resources', 'election_data.csv')
#setting variables 
total_votes = 0
candidates_dict = {}
with open(csvpath, newline='') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')
    #skip header row
    header_row = next(csvreader)
    """
    read each row of data
    add up the total voters
    store the candiadetes in a dict 
    """
    for row in csvreader:
        total_votes += 1
        if row[2] in candidates_dict.keys():
            candidates_dict[row[2]] += 1
        else:
            candidates_dict[row[2]] = 1
    #print(total_votes)
    #print(candidates_dict)
#dic of all the candia...
winner = ''
total_vote = 0
vote_percentage =[]
with open ("Election Results.txt","w") as text:
    print(f"Election Results")
    text.write(f"Election Results\n")
    print(f"---------------------------")
    text.write(f"---------------------------\n")
    print(f"Total Votes: {total_votes}")
    text.write(f"Total Votes: {total_votes}\n")
    print(f"---------------------------")
    text.write(f"---------------------------\n")

    for candidate in candidates_dict:
        candidate_votes = candidates_dict[candidate]
            
        #this prints out candidate names
        #print(candidate)
        
        #total votes for each candidate
        #print(candidate_votes)
        #this % of votes for the candidats

        vote_percentage = (candidate_votes / total_votes )
        #print(vote_percentage)
        #winners


        if total_vote < candidate_votes:
            winner = candidate
            total_vote = candidate_votes
        print(candidate, "{:.3%}".format(vote_percentage), candidate_votes,)
        text.write(candidate+" " +"{:.3%}".format(vote_percentage)+" " +str(candidate_votes)+"\n")
    print(f'winner: {winner} '+str(total_vote))
    text.write(f'winner: {winner} '+str(total_vote))
        
    




