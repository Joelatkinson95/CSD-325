#Joel Atkinson July 2,2025 Assignment 9.2 Advanced Python
#The purpose of this assignment is to test the connection to a simple API and output results

import json
import requests

response = requests.get('https://anapioficeandfire.com/api/houses/1')

print(response.status_code)
if response.status_code == 200:
    print('Connection Successful!')
else:
    print(f'Failed to connect. Status code:{response.status_code}')

print('\nNon Formatted Response:', response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print('\nFormatted Response:')
jprint(response.json())