import os
import csv 

pypollcsv = os.path.join("Resources", "election_data.csv")

voteslist=[]
candidates=[]
cand_votes={}

with open(pypollcsv) as csvfile:
    pypollreader = csv.reader(csvfile, delimiter=",")
    header=next(pypollreader)

    for votes in pypollreader:
        voteslist.append(votes[0])
        #list of candidates
        if votes[2] not in candidates:
            candidates.append(votes[2])
            cand_votes[votes[2]]=0

        cand_votes[votes[2]]=cand_votes[votes[2]] +1

total_votes=len(voteslist)
print (total_votes)
print (candidates)
print (cand_votes)
#The total number of votes cast 
# number of rows in the csv 

#A complete list of candidates who received votes
#list from candiate row PRINT

#The percentage of votes each candidate won
#candiate votes/total votes *100

#The total number of votes each candidate won


#The winner of the election based on popular vote.
#candidate with most votes 



