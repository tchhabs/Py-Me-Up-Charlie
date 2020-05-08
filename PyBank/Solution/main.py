import os
import csv

csvpath= os.path.join("..", "Resources", "budget_data.csv")

months = []
monthly_change = []
monthly_profit = []
revenue=[]


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader, None)

    for row in csvreader:
    #total number of months 
        months.append(row[0])
    #net total of profit/losses 
        revenue.append(int(row[1]))
        #total_revenue += int(row[1])
        
        total_months=len(months)

    max_inc = revenue[1]
    max_dec = revenue[1]
    total_revenue = 0

    #loop through data to find monthly change
for r in range(len(revenue)):
    if revenue[r] >= max_inc:
        max_inc = revenue[r]
        max_inc_month = months[r]
    elif revenue[r] <= max_dec:
        max_dec = revenue[r]
        max_dec_month = months[r]
    total_revenue += revenue[r]

#calculate average_change
average_change = round(total_revenue/total_months, 2)


print("Financial Analysis")
print("----------------------------")
print(f'Total months: {total_months}')
print (f'Total: ${total_revenue}')
print(f'Average Change: $ {average_change}')
print(f'Greatest Increase in Profits: {max_inc_month} (${max_inc})')
print(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})')

output_path = os.path.join("PyBankResults.txt")
with open(output_path, 'w') as txtfile:

    txtfile.write('Financial Analysis')
    txtfile.write('\n----------------------------')
    txtfile.write(f'\nTotal Months: {total_months}')
    txtfile.write(f'\nTotal: ${total_revenue}')
    txtfile.write(f'\nAverage Change: $ {average_change}')
    txtfile.write(f'\nGreatest Increase in Profits:  {max_inc_month} (${max_inc})')
    txtfile.write(f'\nGreatest Decrease in Profits: {max_dec_month} (${max_dec})')
