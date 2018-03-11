# Modules
import os
import csv

# Prompt user for dataset
dataset = input('What dataset would you like to test?  (budget_data_1.csv or budget_data_2.csv    ')

# Set path for file
csvpath = os.path.join('raw_data', dataset)

# Results storage
count = 0
total = 0
greatest_increase = 0
greatest_decrease = 0
monthly_revenue_1 = 0

# Initiate the .csv reader
csvfile = open(csvpath, newline='')
csvreader = csv.reader(csvfile, delimiter=',')

# Skip the header
next(csvreader, None)

for row in csvreader:

    monthly_revenue = int(row[1])

    # Count of total months
    count += 1

    # Summed total revenue
    total += monthly_revenue

    # Average change calculation
    if count == 1:
        opening_value = monthly_revenue
    else:
        closing_value = monthly_revenue
        avg_change_denominator = count - 1
        avg_change = (closing_value - opening_value) / (count - 1)

    # Finding greatest increase and decrease in revenue
    monthly_revenue_2 = monthly_revenue
    if count == 1:
        pass
    else:
        change_in_revenue = monthly_revenue_2 - monthly_revenue_1
        if change_in_revenue > greatest_increase:
            greatest_increase = change_in_revenue
            greatest_increase_month = row[0]
        elif change_in_revenue < greatest_decrease:
            greatest_decrease = change_in_revenue
            greatest_decrease_month = row[0]
    monthly_revenue_1 = monthly_revenue

# Print results
print('')
print('```')
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(count))
print('Total Revenue: $' + str(total))
print('Average Revenue Change: $' + str(round(avg_change, 2)))
print('Greatest Increase in Revenue: ' + greatest_increase_month + ' ($' + str(greatest_increase) + ')')
print('Greatest Decrease in Revenue: ' + greatest_decrease_month + ' ($' + str(greatest_decrease) + ')')
print('```')
print('')