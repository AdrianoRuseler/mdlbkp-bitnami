import csv

# Define the headers as a dictionary
headers = {
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

# Create the CSV file
with open('course_sessions.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.DictWriter(file, fieldnames=headers.keys())
    
    # Write the headers to the CSV file
    writer.writeheader()

print("CSV file 'course_sessions.csv' has been created successfully with the specified headers.")