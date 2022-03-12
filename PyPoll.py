#Import OS module
import os
#import csv module
import csv

# Assign variable and Read csv file
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers) 



# The Data we need to retreive

#1. The total number of votes cast

#2. A complete list of candidates who received votes

#3. The percentage of votes each candidate won

#4. The total number of votes each candidate won

#5. The winner of the election based on popular vote


## Write data to new text file

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # write three counties to the File
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
