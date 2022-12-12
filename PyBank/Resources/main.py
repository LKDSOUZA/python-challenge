import os
import csv

months = []
pnl = []
total_months = []


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csv_file:
    
    csv_data = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_data)
    

    
    for row in csv_data:
        months.append(f"{row[0]}")
        pnl.append(int(row[1])) 
    
total_months += {len(months)}

total = []
total = 0

for i in range(0,len(pnl)):
    total = total + pnl[i]

results = {
    "Total Months" :total_months,
    "Total $":total
}

print(results)
print("Financial Analysis")
print("--------------------------------")
for i in results:
    print(f"{i}: {results[i]}")





outpath = os.path.join("Resources/analysis", "financial_analysis.txt")

with open(outpath, 'w') as output:
    
    writer = csv.writer(output)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------------"])

    writer.writerow([results])







