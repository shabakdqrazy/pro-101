import random

response = "y"

while response == "y":
    # Roll the dice
    dice_value = random.randint(1, 6)

    # Print the dice representation
    print("---------")
    print("|       |")
    
    if dice_value == 1:
        print("|   o   |")
    elif dice_value == 2:
        print("| o   o |")
    elif dice_value == 3:
        print("| o o o |")
    elif dice_value == 4:
        print("| o o o |")
        print("|   o   |")
    elif dice_value == 5:
        print("| o o o |")
        print("| o   o |")
    else:
        print("| o o o |")
        print("| o o o |")
    
    print("|       |")
    print("---------")
    
    # Ask the user to continue or exit
    response = input("Roll the dice again? (y/n): ")

# End of the program
