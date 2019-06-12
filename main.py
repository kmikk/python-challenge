import os
import csv

bank_data = os.path.join("Resources", "budget_data.csv")

# In this challenge, you are tasked with creating a Python script for analyzing 
# the financial records of your company. You will give a set of financial data 
# called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is 
# composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company 
# has rather lax standards for accounting so the records are simple.)

month = []
pandl = []




with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        month.append(row[0])
        pandl.append(row[1])
        max_increase = max(pandl)
        max_decrease = min(pandl)
        
        if int(row[1]) == max_increase:
            print(row)


# Your task is to create a Python script that analyzes the records to calculate
# each of the following:
pandl = [int(i) for i in pandl]

  # The total number of months included in the dataset
num_of_months = len(month)
  
  # The net total amount of "Profit/Losses" over the entire period
net_total = sum(pandl)

  # The average of the changes in "Profit/Losses" over the entire period
from statistics import mean
average = mean(pandl,2)


  # The greatest increase in profits (date and amount) over the entire period



  # The greatest decrease in losses (date and amount) over the entire period

  
  
  # Lists to store data









# Final Print Out
print("Financial Analysis \n----------------------------")
print("Total Months: " + str(num_of_months))
print("Total: $" + str(net_total))
print("Average Change: $" + str(average))
#print("Greatest Increase in Profits: " + str(greatest_increase"))
print("Greatest Decrease in Profits: " + str(greatest_decrease))