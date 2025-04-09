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
    },
    {
        'groups': 'Turma B',
        'sessiondate': (datetime.now() + timedelta(days=1)).strftime('%d-%m-%Y'),
        'from': '13:00',
        'to': '15:00',
        'description': 'Calculus II',
        'repeaton': 'Tuesday',
        'repeatevery': '1',
        'repeatuntil': (datetime.now() + timedelta(days=30)).strftime('%d-%m-%Y'),
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
        'groups': 'Turma C',
        'sessiondate': (datetime.now() + timedelta(days=2)).strftime('%d-%m-%Y'),
        'from': '10:00',
        'to': '12:00',
        'description': 'Basic Physics',
        'repeaton': 'Wednesday',
        'repeatevery': '2',
        'repeatuntil': (datetime.now() + timedelta(days=60)).strftime('%d-%m-%Y'),
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

# Create the CSV file
with open('course_sessions2.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.DictWriter(file, fieldnames=headers.keys())
    
    # Write the headers to the CSV file
    writer.writeheader()
    
    # Write the sample data
    writer.writerows(course_data)

print("CSV file 'course_sessions.csv' has been created successfully with headers and sample data.")