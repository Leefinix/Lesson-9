medical_cause = input("Did u have a medical cause Y or N: ")
aten = int(input("Enter the attendance percentage of the student: "))

if medical_cause == "Y":
    print("You are allowed")
else:
    if aten >= 75:
        print("Allowed")
    else:
        print("Not Allowed")