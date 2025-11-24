# CIS245-T303 Introduction to Programming
# Instructor: Dr. Sasan Azazian
# M3: Assignment 2 - Python Repetition Program
# Author: Eric J Turman
# Date: 09-24-2025
# email: ejturman@my365.bellevue.edu

# Set named variables
GREETING = (
    "Welcome to \"DublinVestments\" the investment company that let's you "
    "know\nhow long it will take for you to at least double your initial "
    "investment\nfor a given interest percentage rate.\n"
    "'Let Dublin, Ireland help you find your pot of gold'\n"
)
INPUT_COMPLIANCE_MESSAGE = (
    "Enter a positive integer only: no letters, symbols, or "
    "punctuation, please."
)
INTEREST_MESSAGE = (
    "Example: for eight percent write 8 and not 0.08 or 8%.\n"
    "Enter the INTEREST PERCENTAGE RATE to the nearest percent: "
)
INVEST_MESSAGE = (
    "Example: for ten thousand dollars, write 10000 not $10,000.00.\n"
    "Enter your INITIAL INVESTMENT in whole dollars: "
)

# Greeting message
print(GREETING)
print("="*79)

# Input: Initialize valid_input Boolean and compound_rate
valid_input = False
interest_rate = ""

# Obtain the interest rate that is greater than 0
while not valid_input:
    print(INPUT_COMPLIANCE_MESSAGE)
    interest_rate = input(INTEREST_MESSAGE)
    valid_input = interest_rate.isdigit()
    if valid_input:
        interest_rate = float(interest_rate)
        if interest_rate < 1:
            valid_input = False

print("-"*79)

# Reset the valid_input boolean and initialize the initial_investment amount
valid_input = False
initial_investment = ""

# Obtain the initial investment that is greater than 0
# Code duplication here is not ideal, but within the parameters of what
# has been taught so far--Functions are next week
while not valid_input:
    print(INPUT_COMPLIANCE_MESSAGE)
    initial_investment = input(INVEST_MESSAGE)
    valid_input = initial_investment.isdigit()
    if valid_input:
        initial_investment = float(initial_investment)
        if initial_investment < 1:
            valid_input = False

print("="*79)

# Initialize compounding variables
years_to_double = 0
compounded_investment = initial_investment

# Process: Create a multiplier for compound interest based on the interest rate
compounding_factor = (100 + interest_rate) / 100

while compounded_investment < initial_investment * 2:
    compounded_investment = compounded_investment * compounding_factor
    years_to_double += 1

# determine if year needs to be plural
if years_to_double > 1:
    years = "years"
else:
    years = "year"

# Output: Present the result to the customer
print(
    f"\nTo at least double your initial investment of "
    f"${initial_investment:,.2f} at a\nyearly compound interest rate of "
    f"{interest_rate:.0f}% it will take {years_to_double} {years}.\n"
    f"At this time, you will have ${compounded_investment:,.2f}."
)
