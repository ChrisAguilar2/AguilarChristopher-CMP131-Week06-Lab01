# Student name: Christopher Aguilar
# Course: CMP 131
# Week: 6
# Lab: 1
# Assignment: Software Quantity Discount
# Date: 10/1/26

# Display the program title and collect an integer quantity.
print("====== Software Quantity Discount ======")
try:
    software_purchase = int(input("Enter the number of software units purchased: "))
except ValueError:
    print("ERROR: Enter a whole number of units.")
else:
    # Reject invalid quantities before calculating a purchase total.
    if software_purchase <= 0:
        print("ERROR: The number of units must be greater than zero.")
    else:
        # Select exactly one discount rate for every valid quantity.
        if software_purchase < 10:
            discount_rate = 0.0
        elif software_purchase < 20:
            discount_rate = 0.20
        elif software_purchase < 50:
            discount_rate = 0.30
        elif software_purchase < 100:
            discount_rate = 0.40
        else:
            discount_rate = 0.50

        # Calculate the original cost, discount, and final cost.
        price_per_unit = 99.00
        original_cost = software_purchase * price_per_unit
        discount_amount = original_cost * discount_rate
        final_cost = original_cost - discount_amount

        # Display the complete purchase report with monetary formatting.
        print("============= Purchase Report =============")
        print("Units purchased:", software_purchase)
        print(f"Price per unit: ${price_per_unit:.2f}")
        print(f"Original cost: ${original_cost:.2f}")
        print(f"Discount percentage: {discount_rate:.0%}")
        print(f"Discount amount: ${discount_amount:.2f}")
        print(f"Final purchase cost: ${final_cost:.2f}")
