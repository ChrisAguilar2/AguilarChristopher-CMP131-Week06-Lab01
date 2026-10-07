#Christopher Aguilar
#CMP 131
#Week 6
#Lab 1
#mobile phone bill
#10/1/26

package = input("Which package would you like to choose? ")
minutes = int(input("Enter the number of minutes used during the month"))


print("======Phone Bill Packages=========")
print("====Package A====")
print("Monthly charge: $39.99")
print("Included minutes: 450")
print("Additional minutes: $0.45 per minute")

print("======Phone Bill Packages=========")
print("====Package B====")
print("Monthly charge: $59.99")
print("Included minutes: 900")
print("Additional minutes: $0.40 per minute")

print("======Phone Bill Packages=========")
print("====Package C====")
print("Monthly charge: $69.99")
print("Included minutes: Unlimited")
print("Additional minutes: No additional-minute charge")

if package == "A":
    print("You chose package A")

    if minutes > 450:
        additional_minutes = minutes - 450
    else:
        additional_minutes = 0

    additional_charge = additional_minutes * 0.45
    total = 39.99 + additional_charge

    print("Additional minutes:", additional_minutes)
    print(f"Total amount due: ${total:.2f}")

elif package == "B":
    print("You chose package B")

    if minutes > 900:
        additional_minutes = minutes - 900
    else:
        additional_minutes = 0

    additional_charge = additional_minutes * 0.40
    total = 59.99 + additional_charge

    print("Additional minutes:", additional_minutes)
    print(f"Total amount due: ${total:.2f}")
elif package == "C":
    print("You chose package C")
    total = 59.99
    print(f"Total amount due: ${total:.2f}")

else:
    print("Invalid-Package")    
        