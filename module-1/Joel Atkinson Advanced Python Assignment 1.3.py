#Joel Atkinson May 29,2025
#CSD325 Advanced Python Assignment 1.2
#The purpose of this assignment is to count down from 100 to 0 according to the "Bottles of Beer on the Wall" Song

def beer_countdown():
    count = int(input("Please enter the number of beer bottles currently on the wall: ",))
    print()

    while count > 0:
        if count ==1:
            print('One bottle of beer on the wall, 1 bottle of beer.')
            print('Take one down, pass it around, 0 bottles of beer on the wall.', end="\n\n\n")

        else:
            print(f'{count} bottles of beer on the wall, {count} bottles of beer')
            print(f'You take one down, pass it around, {count-1} bottles of beer on the wall.', end="\n\n")

        count -= 1

    print('Time to buy more bottles of beer!')




if __name__ == "__main__":
    beer_countdown()