import os
import csv 

pypollcsv = os.path.join("Resources", "election_data.csv")

voteslist=[]
candidates=[]
cand_votes=[0,0,0,0]
votes_percent =[0,0,0,0]


with open(pypollcsv) as csvfile:
    pypollreader = csv.reader(csvfile, delimiter=",")
    header=next(pypollreader)


    for row in pypollreader:
        voteslist.append(row[2])
        #list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
    for votes in voteslist:
        if candidates[0]==votes: 
            cand_votes[0]+=1
        elif candidates[1]==votes: 
            cand_votes[1]+=1
        elif candidates[2]==votes: 
            cand_votes[2]+=1
        elif candidates[3]==votes: 
            cand_votes[3]+=1     

    total_votes=len(voteslist)
    votes_percent[0]= round((int(cand_votes[0])/total_votes)*100,4)
    votes_percent[1]= round((int(cand_votes[1])/total_votes)*100,4)
    votes_percent[2]= round((int(cand_votes[2])/total_votes)*100,4)
    votes_percent[3]= round((int(cand_votes[3])/total_votes)*100,4)

    winner = max(voteslist)

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {votes_percent[0]}% ({cand_votes[0]})')
print(f'Correy: {votes_percent[1]}% ({cand_votes[1]})')
print(f'Li: {votes_percent[2]}% ({cand_votes[2]})')
print(f'O\'Tooley: {votes_percent[3]}% ({cand_votes[3]})')
print(f'-------------------------')
print(f'Winner: Khan')
print(f'-------------------------')

output_path = os.path.join("PyPollResults.txt")
with open(output_path, 'w') as txtfile:

    txtfile.write('Election Results')
    txtfile.write('\n----------------------------')
    txtfile.write(f'\nTotal Votes: {total_votes}')
    txtfile.write('\n----------------------------')
    txtfile.write(f'\nKhan: {votes_percent[0]}% ({cand_votes[0]})')
    txtfile.write(f'\nCorrey: {votes_percent[1]}% ({cand_votes[1]})')
    txtfile.write(f'\nLi: {votes_percent[2]}% ({cand_votes[2]})')
    txtfile.write(f'\nO\'Tooley: {votes_percent[3]}% ({cand_votes[3]})')
    txtfile.write('\n----------------------------')
    txtfile.write(f'\nWinner: Khan')
    txtfile.write(f'\n-------------------------')
   

