import csv
from datetime import datetime, timedelta

# Define all possible headers
all_headers = {
    'courseshortname': '',
    'groups': '',
    'sessiondate': '',
    'from': '',
    'to': '',
    'description': '',
    'repeaton': '',
    'repeatevery': '',
    'repeatuntil': '',
    'studentscanmark': '',
    'allowupdatestatus': '',
    'passwordgrp': '',
    'randompassword': '',
    'subnet': '',
    'automark': '',
    'autoassignstatus': '',
    'absenteereport': '',
    'preventsharedip': '',
    'preventsharediptime': '',
    'calendarevent': '',
    'includeqrcode': '',
    'rotateqrcode': '',
    'studentsearlyopentime': ''
}

# Sample data for 3 course sessions
course_data = [
    {
        'courseshortname': 'CS101',
        'groups': 'Group A',
        'sessiondate': datetime.now().strftime('%Y-%m-%d'),
        'from': '09:00',
        'to': '11:00',
        'description': 'Introduction to Programming',
        'repeaton': 'Monday',
        'repeatevery': '1',
        'repeatuntil': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
        'studentscanmark': 'yes',
        'allowupdatestatus': 'yes',
        'passwordgrp': 'CS101A',
        'randompassword': 'no',
        'subnet': '192.168.1.0/24',
        'automark': 'yes',
        'autoassignstatus': 'present',
        'absenteereport': 'yes',
        'preventsharedip': 'yes',
        'preventsharediptime': '30',
        'calendarevent': 'yes',
        'includeqrcode': 'yes',
        'rotateqrcode': 'no',
        'studentsearlyopentime': '15'
    },
    {
        'courseshortname': 'MATH201',
        'groups': 'Group B',
        'sessiondate': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
        'from': '13:00',
        'to': '15:00',
        'description': 'Calculus II',
        'repeaton': 'Tuesday',
        'repeatevery': '1',
        'repeatuntil': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
        'studentscanmark': 'yes',
        'allowupdatestatus': 'yes',
        'passwordgrp': 'MATH201B',
        'randompassword': 'yes',
        'subnet': '192.168.2.0/24',
        'automark': 'no',
        'autoassignstatus': 'pending',
        'absenteereport': 'yes',
        'preventsharedip': 'no',
        'preventsharediptime': '0',
        'calendarevent': 'yes',
        'includeqrcode': 'no',
        'rotateqrcode': 'no',
        'studentsearlyopentime': '10'
    },
    {
        'courseshortname': 'PHYS101',
        'groups': 'Group C',
        'sessiondate': (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d'),
        'from': '10:00',
        'to': '12:00',
        'description': 'Basic Physics',
        'repeaton': 'Wednesday',
        'repeatevery': '2',
        'repeatuntil': (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d'),
        'studentscanmark': 'no',
        'allowupdatestatus': 'no',
        'passwordgrp': '',
        'randompassword': 'yes',
        'subnet': '',
        'automark': 'yes',
        'autoassignstatus': 'present',
        'absenteereport': 'no',
        'preventsharedip': 'yes',
        'preventsharediptime': '45',
        'calendarevent': 'no',
        'includeqrcode': 'yes',
        'rotateqrcode': 'yes',
        'studentsearlyopentime': '20'
    }
]

# Predefined list of selected headers to populate with data
selected_headers = [
    'courseshortname',
    'sessiondate',
    'from',
    'to',
    'description',
    'studentscanmark',
    'passwordgrp'
]

# Validate selected headers
valid_headers = [h for h in selected_headers if h in all_headers]
if not valid_headers:
    print("No valid headers selected! Populating all headers instead.")
    valid_headers = list(all_headers.keys())

# Create filtered data with all headers, but only populate selected ones
filtered_course_data = []
for session in course_data:
    row = {header: '' for header in all_headers}  # Start with all headers empty
    for header in valid_headers:  # Populate only selected headers
        row[header] = session.get(header, '')
    filtered_course_data.append(row)

# Create the CSV file with all headers
with open('course_sessions2.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=all_headers.keys())
    writer.writeheader()
    writer.writerows(filtered_course_data)

print(f"CSV file 'course_sessions2.csv' has been created successfully with all {len(all_headers)} headers, "
      f"populating data for {len(valid_headers)} selected headers: {', '.join(valid_headers)}")