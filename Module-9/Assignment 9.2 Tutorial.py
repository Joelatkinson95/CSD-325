#Joel Atkinson July 2,2025 Assignment 9.2 Tutorial Advanced Python CSD-325
#The purpose of this file is to set up and complete the API Tutorial for Astronaut JSON

import requests
response = requests.get('http://api.open-notify.org/astros.json')

#Check to see if connection was successful and print Status Code
print(response.status_code)
#Added an if/else in addition to what tutorial showed to add some more context to status code
if response.status_code == 200:
    print('Connection Successful!')
else:
    print(f'Failure to connect. Code: {response.status_code}')

import json

#create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Print imported JSON results
jprint(response.json())