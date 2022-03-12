# Election_Analysis
This report is broken down into two parts.  The first part, or "Project", is the candidate analysis while the second part, or "Challenge", is the county analysis.

## Project Overview - Candidate Specific
This project completes an election audit of a recent local congressional election in Colorado.  This was tasked by a Colorado Board of Elections employee.  The items calculated are as follows:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

## Project Resources
- Data Source: election_results.csv
- Software: Python v3.10.2, Visual Studio Code v1.65.1

## Project Summary - Candidate Specific
The analysis of the election show that:
- There were 369,711 total votes cast in the election
- The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The individual candidate results were:
	- Charles Casper Stockham received 23.0% of the votes with 85,213 total votes
	- Diana DeGette received 73.8% of the total votes with 272,892 total votes
	- Raymon Anthony Doane received 3.1% of the total votes with 11,606 total votes
- The winner of the election was:
	- Diana DeGette who receieved 73.8% of the votes with 272,892 total votes 

## Challenge Overview - County Specific
This project completes an election audit of a recent local congressional election in Colorado.  This was tasked by a Colorado Board of Elections employee.  The "project" portion calculated the candidate results while the "Challenge" calculated county results.  The items calculated are as follows:

1. Calculate the total number of votes cast
2. Get a complete list counties where votes were cast from
3. Calculate the total voter turnout for each county
4. Calculate the percentage of votes from each county
5. Determine the county that had the highest voter turnout  

## Challenge Resources
- Data Source: election_results.csv
- Software: Python v3.10.2, Visual Studio Code v1.65.1

## Challenge Summary - County Specific 
The analysis of the election show that:
- There were 369,711 total votes cast in the election
- The counties that people voted from were and their respective numbers are:
	- Jefferson county had 10.5% of the total votes with 38,855 total votes
	- Denver county had 82.8% of the total votes with 306,055 total votes
	- Arapahoe county had 6.7% of the total votes with 24,801 total votes
- The county with the highest voter turnout was:
	- Denver with 82.8% of the total votes 

## Election Audit Summary
This script can be utilized as a simple and effective way to calculate the results for a future election.  It analyzes a simple .csv data file which is a common output file of election results and with a few simple changes could be applied to virtually any election.  These changes could include items such as changing a column reference if the raw data is in a slightly different format, or if the analysis is comparing states instead of counties the output results names would just need a simple modification.




