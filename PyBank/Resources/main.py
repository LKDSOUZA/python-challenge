import os
import csv

months = []
profitandloss = []
total_pnl = []
total_months = []

csvpath = os.path.join('Resources/python-challenge/PyBank/Resources', 'budget_data.csv')

with open(csvpath, 'r') as csv_file:
    
    csv_data = csv.reader(csv_file)
    csv_header = next(csv_data)
    

    
    for row in csv_data:
        months.append(f"{row[0]}")
        profitandloss.append(f"{row[1]}") 

total_months += {len(months)}

print(total_months)
    