u = int(input(" Please enter the number of Units you consumed : "))

if (u < 50):
    amount = u * 2.60
    surcharge = 25

elif (u <= 100):
    amount = u * 3.60
    surcharge = 35

elif (u <= 200):
    amount = u * 4.60
    surcharge = 45

else:
    amount = u * 5.60
    surcharge = 55

total = amount + surcharge
print("\n Electricity Bill = %.2f" %total)