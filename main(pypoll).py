#!/usr/bin/env python
# coding: utf-8

# import
import os
import csv


# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")


# In[2]:


#Variables 

number_of_rows = 0
diana_total = 0
charles_total = 0
raymon_total = 0
raymon_percentage = 0
diana_percentage = 0
charles_percentage = 0 


# In[3]:


# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)



#Vote Calculations 
    for row in csvreader: 
        ballot_id = str(row[0])
        county = str(row[1])
        candidate = str(row[2])

        number_of_rows = number_of_rows + 1

        if candidate == "Charles Casper Stockham":
            charles_total = charles_total + 1 

        if candidate == "Diana DeGette":
            diana_total = diana_total + 1 

        if candidate == "Raymon Anthony Doane":
            raymon_total = raymon_total + 1 



# In[4]:


#Winner calculations 
if diana_total > charles_total and diana_total > raymon_total: 
    winner = "Diana DeGette"
if charles_total > diana_total and charles_total > raymon_total: 
    winner = "Charles Casper Stockham"
if raymon_total > charles_total and raymon_total > diana_total:
    winner = "Raymon Anthony Doane"
    


# In[5]:


#Percentage Calculations 
raymon_percentage = ((raymon_total / number_of_rows) * 100)
diana_percentage = ((diana_total / number_of_rows) * 100)
charles_percentage = ((charles_total / number_of_rows) * 100) 


# In[6]:


#print 
print("Election Results")
print("---------------------------")
print(f"Total Votes: {(number_of_rows)}")
print("---------------------------")
print(f" Charles Casper Stockham: {(charles_total)} {(charles_percentage)}%")
print(f" Diana DeGette: {(diana_total)} {(diana_percentage)}%")
print(f" Raymon Anthony Doane: {(raymon_total)} {(raymon_percentage)}%")
print("---------------------------")
print(f"Winner: {(winner)}")
print("---------------------------")




# #TextFile
#
# output_path =  os.path.join("..", "Resources", "PyPoll.Analysis")
#
# with open(output_path,"w") as txtfile:
#
#
#     output_path.write("Election Results")
#     output_path.write("---------------------------")
#     output_path.write(f"Total Votes: {(number_of_rows)}")
#     output_path.write("---------------------------")
#     output_path.write(f" Charles Casper Stockham: {(charles_total)} {(charles_percentage)}%")
#     output_path.write(f" Diana DeGette: {(diana_total)} {(diana_percentage)}%")
#     output_path.write(f" Raymon Anthony Doane: {(raymon_total)} {(raymon_percentage)}%")
#     output_path.write("---------------------------")
#     output_path.write(f"Winner: {(winner)}")
#     output_path.write("---------------------------")



