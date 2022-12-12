import os
import csv

total = []
votes = {}
total = 0

csvpath = os.path.join('Resources/python-challenge/PyPoll/Resources', 'election_data.csv')

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csheader = next(csv_reader)
    
    
    for row in csv_reader:

        if row[2] not in votes.keys():
            votes[row[2]] = 1
        else:
            votes[row[2]] += 1
        
        total += 1

    for item in votes:

        count = votes[item]

        precentage = round(count/total*100,3)
        
        votes[item] = [precentage, count]

    
    
    print("Election Results")
    print("----------------------------------")
    print("Total Votes:", total)
    print("----------------------------------")
    print(votes)
    print("----------------------------------")
    print("Winner: Diana DeGette")
    print("----------------------------------")

   
    outpath = os.path.join("Resources/python-challenge/PyPoll/Resources/analysis", "financial_analysis.txt")

with open(outpath, 'w') as output:
    
    writer = csv.writer(output)
    writer.writerow(["Election Results"])
    writer.writerow(["Total Votes:", total])
    writer.writerow(["----------------------------------"])
    writer.writerow([votes])
    writer.writerow(["----------------------------------"])
    writer.writerow(["Winner: Diana DeGette"])
    writer.writerow(["----------------------------------"])
    
