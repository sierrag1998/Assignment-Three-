#!/usr/bin/env python
# coding: utf-8


import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")


# In[2]:


# variables
number_of_rows = 2;
rev = 0
prev_rev = 0
total_rev = 0
total_change = 0
profit_difference = 0 
greatest_increase = 0
greatest_decrease = 0
avg_change = 0 


# In[3]:


#ReadTheCSV   
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)


#Greatest Increase and Decrease 

    for row in csvreader:
        month = row[0]
        rev = int(row[1])
        total_rev = rev + total_rev

        if number_of_rows== 2:
            prev_rev = rev


        if number_of_rows > 2:

            profit_difference= rev - prev_rev

            if profit_difference > greatest_increase:
                greatest_increase = profit_difference
                gi_month = month
            if profit_difference < greatest_decrease:
                greatest_decrease = profit_difference
                gd_month = month

            prev_rev = rev
            
#Update rows and total change 
        
        number_of_rows = number_of_rows + 1
        total_change = profit_difference + total_change


# In[4]:


#Avg Change Calculation 
number_of_rows = number_of_rows-2

avg_change = total_change / number_of_rows

#Print 

print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {str(number_of_rows)}") 
print(f"Total: $ {str(total_rev)}")
print(f"Average Change: $ {str(avg_change)}")
print(f"Greatest Increase in Profits: $ {str(greatest_increase)} {str(gi_month)} ")
print(f"Greatest Decrease in Profits: $ {str(greatest_decrease)} {str(gd_month)}")


# #TextFile
#
# output_path =  os.path.join("..", "Resources", "PyBank.Analysis")
#
# with open(output_path,"w") as txtfile:

# output_path.write(f"Financial Analysis")
# output_path.write(f"--------------------------")
# output_path.write(f"Total Months: {str(number_of_rows)}")
# output_path.write(f"Total: $ {str(total_rev)}")
# output_path.write(f"Average Change: $ {str(avg_change)}")
# output_path.write(f"Greatest Increase in Profits: $ {str(greatest_increase)} {str(gi_month)} ")
# output_path.write(f"Greatest Decrease in Profits: $ {str(greatest_decrease)} {str(gd_month)}")




