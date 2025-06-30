# Joel Atkinson June 26,2025 Assignment 8.2 Advanced Python CSD-325
# The goal of this code is to use JSON load() to load the JSON file into a Python class list

#Import JSON module
import json

#Define function to load json data
def load_json_data(filename):
    #Create try-except block to error handle opening .json file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f'Error: The file "{filename}", was not found.')
        return []
    except json.JSONDecodeError:
        print(f'Error: The file "{filename}" contains invalid JSON.')
        return []


#Define function  to save the data in the .json file
def save_json_data(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'\nAttention: The {filename} file has been updated. Would you like to save? (yes/no)')
        choice = input().lower()
        #Offer user an input choice of whether they would like to save the updated file or not
        if choice == 'yes':
            print('File saved successfully.')
        else: print('Changes not saved.')
    #Add error handling when saving file
    except Exception as e:
        print(f'Error saving file: {e}')

#Define the function to print the student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['F_Name']}, {student['L_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

#Deefine the main() function that will run the program
def main():
    filename = 'student_list.json'
    #Load original data
    student_list = load_json_data(filename)

    #print original list
    print('\nAttention: This Is The Student List')
    print_students(student_list)

    #Add new student
    new_student = {
        "F_Name": "Joel",
        "L_Name": "Atkinson",
        "Student_ID": 324143,
        "Email": "Jatkinson@fake.com"
    }
    student_list.append(new_student)
    print('\nAttention: New Student Added to List')

    #Print updated list
    print('\nAttention: This Is The Updated Student List.')
    print_students(student_list)

    #Save updated data
    save_json_data(filename, student_list)

#Run the main() function
if __name__ == "__main__":
    main()