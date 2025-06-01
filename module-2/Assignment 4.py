# Joel Atkinson April 2, 2025 Assignment 4.2
# The purpose of this project is to create a system that converts milage to kilometers

# Define function to convert miles to km
def miles_to_km(miles):
    return miles * 1.60934

# Setting up program with welcome message
print('Welcome to mileage converter calculator. This program converts miles to kilometers')
input('To start, press "Enter"')

# Create loop to bring user back to input if input creates error
while True:
    try:
        user_input = input('Please enter the mileage to be converted (up to two decimal places): ')

        if '.' in user_input:
            decimal_split = user_input.split('.')

            # Check if the number after the '.' is only two decimal places and throw error if > 2.
            # Otherwise, proceed as normal
            if len(decimal_split[1]) > 2:
                raise ValueError("Please enter a valid number up to two decimal places.")

            miles = float(user_input)
            kilometers = miles_to_km(miles)
            print(f'Miles Entered:{miles:.2f}')
            print(f'Converted to Kilometers:{kilometers:.2f}')
            break

        else:
            miles = float(user_input)
            kilometers = miles_to_km(miles)
            print(f'Miles Entered:{miles:.2f}')
            print(f'Converted to Kilometers:{kilometers:.2f}')
            break

    # Catch all errors raised in the loop
    except Exception as error:
        print(f"Something went wrong: {error}")
        print('Try Again')
        continue