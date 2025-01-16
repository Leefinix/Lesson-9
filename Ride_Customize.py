print("Select you're ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter you're choice: "))

if (choice == 1):
    print("What type of bike?")
    print("1. Scooter")
    print("2. Hoverboard")
   
    choice2 = int(input("Enter you're choice: "))
    if choice2 == 1:
        print("You have selected Scooter")
    else:
        print("You have selected Hoverboard")

elif (choice == 2):
    print("What type of car?")
    print("1. Honda")
    print("2. Toyota")

    choice3 = int(input("Enter you're choice: "))
    if choice3 == 1:
        print("You have selected Honda")
    else:
        print("You have selected Toyota")

else:
    print("Invalid choice!")