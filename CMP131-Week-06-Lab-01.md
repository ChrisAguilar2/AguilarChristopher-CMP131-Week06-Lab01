# CMP 131 – Python Programming


> **Required file location:** Keep every Python file directly in the repository root. Do not create a `src` folder.

## Week 6 – Lab 1: Quantity Discounts and Mobile Phone Service Bill

**Total Points: 100**

* Program 1: Software Quantity Discount — 50 points
* Program 2: Mobile Phone Service Bill — 50 points

### Learning Objectives

After completing this lab, students should be able to:

* Accept numeric and text input from the user.
* Convert user input to the appropriate data type.
* Use `if`, `elif`, and `else` statements.
* Evaluate numeric ranges using comparison operators.
* Use nested conditional statements when necessary.
* Calculate discounts and final purchase costs.
* Calculate additional service charges.
* Validate user input.
* Format monetary values to two decimal places.
* Test programs using boundary values.

## Assignment Overview

Create two separate Python programs using conditional statements.

The first program calculates the total cost of purchasing software packages after applying a quantity discount.

The second program calculates a customer’s monthly mobile phone bill based on the selected subscription package and the number of minutes used.

Create the following files:

* `software_discount.py`
* `mobile_phone_bill.py`

The instructor is not providing completed Python code or an exact output design. Students must design, write, and test their own programs.

# Program 1: Software Quantity Discount

**Points: 50**

## Program Description

A software company sells a software package for **$99.00 per unit**.

The company provides quantity discounts according to the number of units purchased.

| Quantity Purchased |    Discount |
| -----------------: | ----------: |
|          1–9 units | No discount |
|        10–19 units |         20% |
|        20–49 units |         30% |
|        50–99 units |         40% |
|  100 or more units |         50% |

Create a program that asks the user for the number of software units purchased. The program must determine the appropriate discount and calculate the final cost of the purchase.

## Required Python File

Create a Python file named:

`software_discount.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: User Input

Ask the user to enter the number of software units purchased.

The quantity must:

* Be converted to an integer.
* Be stored in a meaningfully named variable.
* Be greater than zero.

If the user enters zero or a negative number, display an error message and do not calculate a purchase total.

## Part 2: Calculate the Original Cost

Each software unit costs:

**$99.00**

Calculate the original cost before the discount:

**Original cost = Number of units × $99.00**

## Part 3: Determine the Discount

Use conditional statements to determine the correct discount rate.

Apply the following rules:

* Fewer than 10 units receive no discount.
* From 10 through 19 units receive a 20% discount.
* From 20 through 49 units receive a 30% discount.
* From 50 through 99 units receive a 40% discount.
* 100 or more units receive a 50% discount.

Every valid quantity must receive exactly one discount rate.

## Part 4: Calculate the Discount Amount

Calculate the amount of money deducted from the original cost:

**Discount amount = Original cost × Discount rate**

If the customer does not qualify for a discount, the discount amount is `$0.00`.

## Part 5: Calculate the Final Cost

Calculate the final purchase cost after the discount:

**Final cost = Original cost − Discount amount**

## Part 6: Display the Purchase Report

Display a clearly formatted purchase report containing:

* Number of units purchased
* Price per unit
* Original cost before the discount
* Discount percentage
* Discount amount
* Final purchase cost

All monetary values must:

* Include a dollar sign.
* Display exactly two digits after the decimal point.
* Include a clear label.

The discount rate should display as a percentage.

## Required Testing for Program 1

### Test 1: No Discount

* Units purchased: `5`
* Original cost: `$495.00`
* Discount: `0%`
* Final cost: `$495.00`

### Test 2: 20% Discount Boundary

* Units purchased: `10`
* Original cost: `$990.00`
* Discount amount: `$198.00`
* Final cost: `$792.00`

### Test 3: 30% Discount Boundary

* Units purchased: `20`
* Original cost: `$1,980.00`
* Discount amount: `$594.00`
* Final cost: `$1,386.00`

### Test 4: 40% Discount Boundary

* Units purchased: `50`
* Original cost: `$4,950.00`
* Discount amount: `$1,980.00`
* Final cost: `$2,970.00`

### Test 5: 50% Discount Boundary

* Units purchased: `100`
* Original cost: `$9,900.00`
* Discount amount: `$4,950.00`
* Final cost: `$4,950.00`

### Test 6: Invalid Quantity

* Units purchased: `0`

Confirm that:

* An error message is displayed.
* The program does not calculate a purchase cost.
* The program ends without an error.

## Program 1 Point Distribution

* User input and integer conversion: 5 points
* Quantity input validation: 5 points
* Correct discount conditions: 15 points
* Correct original-cost calculation: 5 points
* Correct discount calculation: 5 points
* Correct final-cost calculation: 5 points
* Clear monetary formatting and output: 5 points
* Comment header, code comments, and testing: 5 points

**Program 1 Total: 50 points**

# Program 2: Mobile Phone Service Bill

**Points: 50**

## Program Description

A mobile phone service provider offers three subscription packages.

### Package A

* Monthly charge: `$39.99`
* Included minutes: `450`
* Additional minutes: `$0.45` per minute

### Package B

* Monthly charge: `$59.99`
* Included minutes: `900`
* Additional minutes: `$0.40` per minute

### Package C

* Monthly charge: `$69.99`
* Included minutes: Unlimited
* No additional-minute charge

Create a program that asks the user to select a package and enter the number of minutes used during the month.

The program must calculate and display the total monthly bill.

## Required Python File

Create a Python file named:

`mobile_phone_bill.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Display the Available Packages

Display the three subscription packages before asking the user to make a selection.

The package information should clearly show:

* Package letter
* Monthly charge
* Included minutes
* Additional-minute rate

## Part 2: User Input

Ask the user to enter:

* The selected package: `A`, `B`, or `C`
* The number of minutes used during the month

The package selection must be stored as text.

The number of minutes must:

* Be converted to an integer.
* Be zero or greater.
* Be stored in a meaningfully named variable.

## Part 3: Validate the Package Selection

The program must accept only:

* `A`
* `B`
* `C`

If the user enters another letter or value:

* Display an invalid-package message.
* Do not calculate a monthly bill.
* Allow the program to end without an error.

## Part 4: Calculate the Package A Bill

If the customer selects Package A:

* Begin with the monthly charge of `$39.99`.
* Include the first 450 minutes without an additional charge.
* Charge `$0.45` for every minute above 450.

If the customer uses 450 minutes or fewer, the total bill remains `$39.99`.

If the customer uses more than 450 minutes, calculate:

**Additional minutes = Minutes used − 450**

**Additional charge = Additional minutes × $0.45**

**Total bill = $39.99 + Additional charge**

## Part 5: Calculate the Package B Bill

If the customer selects Package B:

* Begin with the monthly charge of `$59.99`.
* Include the first 900 minutes without an additional charge.
* Charge `$0.40` for every minute above 900.

If the customer uses 900 minutes or fewer, the total bill remains `$59.99`.

If the customer uses more than 900 minutes, calculate:

**Additional minutes = Minutes used − 900**

**Additional charge = Additional minutes × $0.40**

**Total bill = $59.99 + Additional charge**

## Part 6: Calculate the Package C Bill

If the customer selects Package C:

* Charge the monthly rate of `$69.99`.
* Do not calculate an additional-minute charge.
* The total bill remains `$69.99` regardless of the number of minutes used.

## Part 7: Display the Monthly Bill

Display a clearly formatted bill containing:

* Selected package
* Number of minutes used
* Monthly package charge
* Number of additional minutes
* Additional-minute charge
* Total amount due

For Package C, clearly indicate that the customer has unlimited minutes.

All monetary values must:

* Include a dollar sign.
* Display exactly two digits after the decimal point.
* Include a clear label.

## Required Testing for Program 2

### Test 1: Package A Without Additional Minutes

* Package: `A`
* Minutes used: `400`
* Total amount due: `$39.99`

### Test 2: Package A With Additional Minutes

* Package: `A`
* Minutes used: `500`
* Additional minutes: `50`
* Additional charge: `$22.50`
* Total amount due: `$62.49`

### Test 3: Package B Without Additional Minutes

* Package: `B`
* Minutes used: `850`
* Total amount due: `$59.99`

### Test 4: Package B With Additional Minutes

* Package: `B`
* Minutes used: `1000`
* Additional minutes: `100`
* Additional charge: `$40.00`
* Total amount due: `$99.99`

### Test 5: Package C

* Package: `C`
* Minutes used: `1500`
* Total amount due: `$69.99`

### Test 6: Invalid Package

* Package: `D`
* Minutes used: `500`

Confirm that:

* An invalid-package message is displayed.
* A monthly bill is not calculated.
* The program ends without an error.

## Program 2 Point Distribution

* Package menu and clear input prompts: 5 points
* Correct input conversion: 5 points
* Correct package validation: 5 points
* Correct Package A calculation: 10 points
* Correct Package B calculation: 10 points
* Correct Package C calculation: 5 points
* Clear monetary formatting and output: 5 points
* Comment header, code comments, and testing: 5 points

**Program 2 Total: 50 points**

# Code Comments

Use comments to identify and explain the major sections of both programs.

Include comments for:

* The program information header
* The program title
* The user-input section
* The conditional-statement section
* The calculation section
* The output section

Comments should explain the purpose of each major section. They do not need to repeat every Python statement.

# Functional Requirements

## Software Discount Program

When `software_discount.py` runs, it must:

* Ask the user for the number of units purchased.
* Convert the quantity to an integer.
* Verify that the quantity is greater than zero.
* Determine the correct discount rate.
* Calculate the original purchase cost.
* Calculate the discount amount.
* Calculate the final purchase cost.
* Display a complete purchase report.
* Format monetary values to two decimal places.
* Run without errors.

## Mobile Phone Bill Program

When `mobile_phone_bill.py` runs, it must:

* Display the three available packages.
* Ask the user to select Package A, B, or C.
* Ask the user for the number of minutes used.
* Validate the package selection.
* Determine whether additional minutes were used.
* Calculate the correct additional charge.
* Calculate the total amount due.
* Display a complete monthly bill.
* Format monetary values to two decimal places.
* Run without errors.

# General Requirements

* Use Python to complete both programs.
* Use `if`, `elif`, and `else` statements.
* Use meaningful and consistent variable names.
* Convert user input to the appropriate data type.
* Include a complete comment header in both files.
* Include comments explaining each major section.
* Format monetary values to two decimal places.
* Use clear prompts, headings, and labels.
* Test both programs using all required test values.
* Check spelling, capitalization, grammar, and punctuation.
* Make sure both programs run without errors.
* Follow the course AI-use policy.
* Record any AI assistance in `AI-Use-Report.md`.

# Required Organization

Organize the assignment as follows:

* `Week-06`

  * `Lab-01`

    * `CMP131-Week-06-Lab-0.md1.md`
    * `AI-Use-Report.md`
    * `src`

      * `software_discount.py`
      * `mobile_phone_bill.py`

# Submission Requirements

Submit or push the complete `Lab-01` folder.

The submission must include:

* `software_discount.py`
* `mobile_phone_bill.py`
* `AI-Use-Report.md`

Before submitting, verify that:

* Both required Python files are included.
* Both filenames are correct.
* Both programs contain a complete comment header.
* Both programs contain appropriate comments.
* The software program validates the quantity.
* All software discount ranges work correctly.
* The mobile phone program validates the package selection.
* All three mobile packages work correctly.
* Additional minutes are calculated correctly.
* Monetary values display two decimal places.
* Both programs were tested using the required values.
* Both programs run without errors.
* The AI-use report is complete.
* The latest work has been committed and pushed to GitHub.

# Suggested Git Commit Messages

* Create Week 6 Lab 1 Python files
* Add software quantity input and validation
* Add quantity discount conditions
* Complete software purchase calculations
* Add mobile phone package selection
* Add mobile phone billing conditions
* Test all discount and package boundaries
* Complete Week 6 Python lab

---

## GitHub Starter Repository

Use the following public starter repository:

[CMP131-Week-06-Lab-01](https://github.com/ahedhli12/CMP131-Week-06-Lab-01)

### Getting Started

1. Open the starter repository using the link above.
2. If **Use this template** is available, select **Use this template → Create a new repository**.
3. Choose your personal GitHub account as the owner.
4. Name your repository `LastName-FirstName-CMP131-Week-06-Lab-01`.
5. Set your repository to **Public**.
6. Clone your own newly created repository—not the instructor’s starter repository.
7. Open the entire cloned folder in Visual Studio Code.
8. Complete and test every required Python file.
9. Commit and push your work to GitHub.
10. Verify that your latest files appear on GitHub.
11. Complete `AI-Use-Report.md`.
12. Submit the required work through Blackboard Ultra and include your public repository link when requested.

### Required Repository Files

- `CMP131-Week-06-Lab-01.md`
- `AI-Use-Policy.md`
- `AI-Use-Report.md`
- `mobile_phone_bill.py`
- `software_discount.py`

### Before You Submit

- [ ] All required Python files are in the repository root.
- [ ] Every required filename is exact.
- [ ] Each program runs successfully.
- [ ] Required tests and screenshots are complete.
- [ ] `AI-Use-Report.md` is complete and accurate.
- [ ] The latest commit is visible on GitHub.
