# CIS245-T303 Introduction to Programming
# M2: Assignment 2 - Python Selection Program
# Author: Eric J Turman
# Date: 09-11-2025
# email: ejturman@my365.bellevue.edu

# In caps because these are named constants
TIER_0_COST_PER_FOOT = 0.87
TIER_1_THRESHOLD = 100.0
TIER_1_COST_PER_FOOT = 0.8
TIER_2_THRESHOLD = 250.0
TIER_2_COST_PER_FOOT = 0.7
TIER_3_THRESHOLD = 500.0
TIER_3_COST_PER_FOOT = 0.5

# Introduction: Escaping the quotes so they display when printed
# Using Implicit Line Continuation with Parentheses. Using this approach,
# instead of six print statements, the implicit concatenation feature
# that does not require the "+" operator will keep the code clean adn readable.
# THis approach is supported by Python and PEP8 newline "\n" and f-strings
print(
    "Welcome to \"Fiber by the Foot,\" your one-stop shop for cable costs.\n\n"
    "We offer superior fiber optic cable at the low, low cost of only "
    f"${TIER_0_COST_PER_FOOT:.2f} per foot.\n"
    "BUT WAIT! We offer bulk discounts: the more you buy, the more you save!\n"
    f"Purchase at least {TIER_1_THRESHOLD:.0f} feet, "
    f"and your cost drops to only ${TIER_1_COST_PER_FOOT:.2f} per foot.\n"
    f"Purchase at least {TIER_2_THRESHOLD:.0f} feet, "
    f"and it is a bargain at only ${TIER_2_COST_PER_FOOT:.2f} per foot.\n"
    f"Purchase at least {TIER_3_THRESHOLD:.0f} feet, "
    f"and we're giving it away at ${TIER_3_COST_PER_FOOT:.2f} per foot.\n"
)

# Input: Ideally, we should trap for non-numeric inputs to avoid errors
linear_feet = float(input("How many linear feet do you need?: "))

# Initialize the cost and discount_cost variables explicitly as a floats
cost = float(0.0)
discount_cost = float(0.0)

# Process: Calculate total cost to the customer with discount if applicable
if linear_feet >= TIER_3_THRESHOLD:
    discount_cost = TIER_3_COST_PER_FOOT
elif linear_feet >= TIER_2_THRESHOLD:
    discount_cost = TIER_2_COST_PER_FOOT
elif linear_feet >= TIER_1_THRESHOLD:
    discount_cost = TIER_1_COST_PER_FOOT
else:
    discount_cost = TIER_0_COST_PER_FOOT

# Calculate adjusted cost to customer
cost = linear_feet * discount_cost

# Output: f-string used to limit the float to two places like dollars and cents
# Let the customer know the unit cost that they qualified for and
# Calculate their savings if applicable
if discount_cost < TIER_0_COST_PER_FOOT:
    print(
        f"You qualified for ${discount_cost:.2f} per linear foot and saved "
        f"${((linear_feet * TIER_0_COST_PER_FOOT) - cost):.2F}\n"
    )
else:
    print(
        f"You did not qualify for a discount. Your cost is "
        f"${discount_cost:.2f} per linear foot\n"
    )

# Provide the customer the amount owed for the linear feet they entered
# Adjust the message for whole feet
if linear_feet == int(linear_feet):
    print(
        f"Your total cost for {linear_feet:.0f} feet of cable "
        f"is ${cost:.2f}.\n"
        f"Thank you! Please come again."
    )
else:
    print(
        f"Your total cost for {linear_feet} feet of cable is ${cost:.2f}.\n"
        f"Thank you! Please come again."
    )
