import os
import csv

months = [] 
profit_loss_change = []
  
count_months = 0
net_profit_loss = 0
previous_profit_loss = 0
currrent_monthly_change = 0
profit_monthly_change = 0

#pypoll_csv = os.path.join("..", "Resources", "pypoll.csv")
#with open(pypoll_csv), ("r") 
pybank_csv = os.path.join("..", "Resources", "pybank.csv")

with open(pybank_csv) as csv_file:
    cvs_reader = cvs_reader(csv_file, delimiter=",")

    csv_reader = next(csv_file)

    print(f"Financial Analysis: {csv_header}")
# 
#
#
    for row in csv_reader
#count of months 
    count_months += 1

    currrent_monthly_change = int(row[1])
    net_profit_loss += currrent_monthly_change

    if(count_months ==1):
       previous_month_profit_loss = current_month_profit_loss
            continue
    else 

    profit_loss_change = (currrent_monthly_change - previous_month_profit_loss)

    months.append(row[0])

    profit_loss_change.append(profit_loss_change)

    previous_month_profit_loss = currrent_monthly_change


sum_profit_loss = sum(profit_loss_change)
averages_profit_loss = (sum_profit_loss).mean()

highest_change = (profit_loss_changes).max()
lowest_change = (profit_loss_changes).max()


print ("Financial Analysis")
print ("-----------------------")

print(f"Total Months: {count_months}")
print(f"Net Total Ammount: {net_profit_loss}")
print(f"Average Profit / Loss: {averages_profit_loss}")
print(f"Greatest Increase : {highest_change}")
print(f"Greatest Decrease: {lowest_change}")


#__________________________________________________________________________________________________

import os
import csv

#variables 
voter_candidate = []
votes_per_candiate = []

#directory 
pypoll_csv = os.path.join("..", 'Resources', 'pypoll.csv')
#open and read
with open(py_poll) as csv_file:

    cvs_reader = cvs_reader(csv_file, delimiter=",")

    csv_reader = next(csv_file)

    for row in csv_reader:
        voter_candidate.append(row[2])

    sorted_list = sorted(voter_candidate)

    arrange_list = sorted_list 

    count_candidate = Counter (arrange_list)
    votes_per_candiate.append(count_candidate.most_common())

    for item in votes_per_candiate:
      

    print("---Election Results---")
    print("----------------------")

    print(f"Total Votes:  {sum(count_candidate.values())}")
   
    print("-------------------------")

    
    print("-------------------------")
   
    print(f"Winner:  {votes_per_candidate[0][0][0]}")
   
    print("-------------------------")