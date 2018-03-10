# Modules
import os
import csv

# State abreviation dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Prompt user for dataset
dataset = input('What dataset would you like to test?  (employee_data1.csv or employee_data2.csv    ')

# Set path for file
input_path = os.path.join('raw_data', dataset)

# Specify the file to write to
output_path = os.path.join('Output', 'new.csv')

count = 0
error_count = 0
errors = False

# Initiate the .csv reader
csvinput = open(input_path, newline='')
csvreader = csv.reader(csvinput, delimiter=',')

# Initiate the .csv writer
csvoutput = open(output_path, 'w', newline='')
csvwriter = csv.writer(csvoutput, delimiter=',')

for row in csvreader:

    if count == 0:
        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
        count += 1
    else:

        Emp_Id = row[0]
    
        name = row[1].split()
        First_Name = name[0]
        Last_Name = name[1]

        date = row[2].split('-')
        if len(date) == 3:
            day = date[2]
            month = date[1]
            year = date[0]
            DOB = day + '/' + month + '/' + year
        else:
            DOB = "ERROR"
            error_count += 1
            errors = True

        SSN = '***-**-' + row[3][7:]

        Date = us_state_abbrev[row[4]]

        csvwriter.writerow([Emp_Id, First_Name, Last_Name, DOB, SSN, Date])

        count += 1

if errors == True:
    print(error_count)