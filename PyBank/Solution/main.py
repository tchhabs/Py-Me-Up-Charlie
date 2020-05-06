import os
import csv

csvpath= os.path.join("..", "Resources", "budget_data.csv")

months = []
revenue = []

print("Financial Analysis")
print("----------------------------")

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader, None)
    revenue=0
    for row in csvreader:
        #total number of months 
        months.append(row[0])
        #net total of profit/losses 
        revenue += int(row[1])
        

total_months=len(months)
print(f'Total months: {total_months}')
print (f'Total: ${revenue}')



    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])

    # Write the second row
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(['Total months:' +str(total_months)+ '\n'])
    csvwriter.writerow(['Total: $:' +str(revenue)+ '\n'])
    csvwriter.writerow(['Average Change: $' + + '\n'])
    csvwriter.writerow(['Greatest Increase in Profits:' + + '\n'])
    csvwriter.writerow(['Greatest Decrease in Profits:' + + '\n'])

#The average of the changes in "Profit/Losses" over the entire period total rev/total months 

#The greatest increase in profits (date and amount) over the entire period (greatest profits/loses)

#The greatest decrease in losses (date and amount) over the entire period (most negative profits/loses)

#your final script should both print the analysis to the terminal and export a text file with the results. (udemy activity)