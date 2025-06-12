import csv
from datetime import datetime

from matplotlib import pyplot as plt
#import sys to allow for 'break' when user selects to exit
import sys

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high/low temperatures from this file. *ADDED LOWS TO CODE*
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)
        except (ValueError, IndexError) as e:
            print(f'Error Processing row {row}: {e}')
            continue

#Display menu and get users choice
while True:
    print('\n Please enter the corresponding number for which data you would like to view or to exit.'
          '(ex. to view "Lows" input "2")')
    choice = input('1: Highs \n2: Lows \n3: Exit \nPlease enter your selection: ')

    if choice == '1':
        # Plot the high temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
         # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '2':
        # Plot the low temperatures
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        # Format plot
        plt.title('Daily low temperatures - 2018', fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel('Temperature (F)', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    #Add the option for user to exit
    elif choice == '3':
        print('Exiting the program.')
        break

   #Add error message if user does not select 1,2, or 3.
    else:
        print('Error: Invalid choice, Please enter "1" for highs, "2" for lows, or "3" to exit')



