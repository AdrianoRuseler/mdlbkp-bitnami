import csv
from datetime import datetime, timedelta

# Define the headers as a dictionary
headers = {
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
        'groups': 'Turma A',
        'sessiondate': datetime.now().strftime('%d-%m-%Y'),
        'from': '09:00',
        'to': '11:00',
        'description': 'Introduction to Programming',
        'repeaton': 'Monday',
        'repeatevery': '1',
        'repeatuntil': (datetime.now() + timedelta(days=30)).strftime('%d-%m-%Y'),
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
    }
]

# Create the CSV file
with open('course_sessions1.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.DictWriter(file, fieldnames=headers.keys())
    
    # Write the headers to the CSV file
    writer.writeheader()
    
    # Write the sample data
    writer.writerows(course_data)

print("CSV file 'course_sessions.csv' has been created successfully with headers and sample data.")