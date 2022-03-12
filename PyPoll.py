#Import OS module
import os
#import csv module
import csv
# Assign variable and Read csv file
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


# 1. Initialize a total vote counter
total_votes = 0

# Candidate options List
candidate_options = []
# Create empty dictionary
candidate_votes = {}

# Open the election results and read file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidates vote count
            candidate_votes[candidate_name] =0

        # Add a vote to that candidates count
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.     
    for candidate_name in candidate_votes:
        # Retreieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the % of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
# 3. Print the total votes
print(total_votes) 
# Print the candidate list
print(candidate_options) 
# Print Candiate vote dictionary
print(candidate_votes)

#2. A complete list of candidates who received votes

#3. The percentage of votes each candidate won

#4. The total number of votes each candidate won

#5. The winner of the election based on popular vote


## Write data to new text file


# using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # write three counties to the File
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
