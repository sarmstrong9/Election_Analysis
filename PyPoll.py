# Add dependencies
import os
import csv
# Assign variable and Read csv file
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
# Candidate options List
candidate_options = []
# Candidate votes dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
        # Get the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidates vote count
            candidate_votes[candidate_name] =0
        # Add a vote to that candidates count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
        #f"{candidate_results}\n"
        #f"--------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results) 

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.     
    for candidate_name in candidate_votes:
        # Retreieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the % of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # print out the winning candidate, vote count and percentage to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save candidate results to text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winnig count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true, set winning_count = votes and winning_percentrage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning_candidate = candidates name
            winning_candidate = candidate_name
         
    #Print winning candidates results to terminal
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")    
    print(winning_candidate_summary)
    # Save the winning candidates results to the text file
    txt_file.write(winning_candidate_summary)

# Print the total votes
#print(total_votes) 
# Print the candidate list
#print(candidate_options) 
# Print Candiate vote dictionary
#print(candidate_votes)


