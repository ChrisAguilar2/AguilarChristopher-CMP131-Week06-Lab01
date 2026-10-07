# Student name: Christopher Aguilar
# Course: CMP 131
# Week: 6
# Lab: 1
# Assignment: Mobile Phone Service Bill
# Date: 10/1/26

# Display all packages before asking the customer to select one.
print("====== Mobile Phone Service Packages ======")
print("A: $39.99 monthly; 450 minutes; $0.45 per additional minute")
print("B: $59.99 monthly; 900 minutes; $0.40 per additional minute")
print("C: $69.99 monthly; unlimited minutes; no additional charge")

# Collect and validate the package selection.
package = input("Choose a package (A, B, or C): ")
if package != "A" and package != "B" and package != "C":
    print("ERROR: Invalid package. Choose A, B, or C.")
else:
    # Collect integer minutes and reject invalid input before billing.
    try:
        minutes = int(input("Enter the number of minutes used this month: "))
    except ValueError:
        print("ERROR: Enter a whole number of minutes.")
    else:
        if minutes < 0:
            print("ERROR: Minutes used must be zero or greater.")
        else:
            # Determine the monthly charge and additional minutes.
            if package == "A":
                monthly_charge = 39.99
                additional_rate = 0.45
                if minutes > 450:
                    additional_minutes = minutes - 450
                else:
                    additional_minutes = 0
            elif package == "B":
                monthly_charge = 59.99
                additional_rate = 0.40
                if minutes > 900:
                    additional_minutes = minutes - 900
                else:
                    additional_minutes = 0
            else:
                monthly_charge = 69.99
                additional_rate = 0.00
                additional_minutes = 0

            # Calculate the additional charge and total bill.
            additional_charge = additional_minutes * additional_rate
            total = monthly_charge + additional_charge

            # Display all required bill details with two decimal places.
            print("============= Monthly Bill =============")
            print("Selected package:", package)
            print("Minutes used:", minutes)
            print(f"Monthly package charge: ${monthly_charge:.2f}")
            if package == "C":
                print("Included minutes: Unlimited")
            print("Additional minutes:", additional_minutes)
            print(f"Additional-minute charge: ${additional_charge:.2f}")
            print(f"Total amount due: ${total:.2f}")
