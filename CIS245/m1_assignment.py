# CIS245-T303 Introduction to Programming
# M1: Assignment 2 - Your First Python Program
# Author: Eric J Turman
# Date: 09-11-2025
# email: ejturman@my365.bellevue.edu

# In caps because this is a named constant
COST_PER_FOOT = 0.87

# Introduction: Escaping the quotes so they display when printed
print("Welcome to \"Fiber by the Foot,\" your one-stop shop for cable costs.")

# This print statement would exceed the eighty-character limit per line of the
# PEP8 styleguide. So, I am breaking it up using
# Implicit Line Continuation with Parentheses.
print(
    "We offer superior fiber optic cable at the low, low cost of only "
    f"${COST_PER_FOOT} per foot."
)

# Input: Ideally, we should trap for non-numeric inputs to avoid errors
linear_feet = float(input("How many linear feet do you need?: "))

# Process: Calculate total cost to the customer
cost = linear_feet * COST_PER_FOOT

# Output: using f-string to limit the float to two places like dollars and cents
print(f"That is going to cost you ${cost:.2f}. Thank you! Please come again.")
