#Christopher Aguilar
#CMP 131
#Week 6
#Lab 1
#software discord
#10/1/26

software_purchase = int(input("Enter the amount of software units purchased:"))
original_cost = software_purchase * 99

if (software_purchase <= 0):
    print("ERROR")
elif (10 > software_purchase and software_purchase > 0):
    print("No Discount")
    discount_rate = 0.0
elif (10< software_purchase and software_purchase <19):
    discount_rate = .20
elif (20< software_purchase and software_purchase <49):
    discount_rate = .30
elif (50< software_purchase and software_purchase <99):
    discount_rate = .40
else:
    discount_rate = .50

discount_amount = original_cost * discount_rate
final_cost = original_cost - discount_amount

print("==============================")
print("-----------Outcome------------")
print("Amount of software purchased:",software_purchase)
print("Price per Unit is $99.00")
print("Original Cost:$", original_cost)
print("Rate of discount:", discount_rate,'%')
print("Amount of money discounted:$", discount_amount)
print("Final cost:$", final_cost)
print("===============================")