# Method definitions
def menu():
    print("Welcome to my program!")
    print("please enter a choice:")
    print("1. Tell me a funny joke")
    print("2. Tell me a riddle")
    print("3. Exit")
    print("Please enter your choice:")
    
    choice = int(input())
    return choice

# Main program

menuChoice = 0

while menuChoice != 3:
    
    menuChoice = menu()

    if menuChoice == 1:
        print("What do you call a cow with no legs?")
    
    elif menuChoice == 2:
        print("What has roots that nobody sees, taller than trees, up, up, up it goes, yet never grows")
    
