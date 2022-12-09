import os
import csv

csvpath = os.path.join('Resources/python-challenge/PyPoll/Resources', 'election_data.csv')

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)