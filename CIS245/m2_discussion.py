# Instruct the user on the expected response format
print(
    f"24-hour time is written without \":\" and ranges from 0000 to 2359.\n"
    f"AM times are 0000 through 1159.\n"
    f"PM times are 1200 through 2359. Just add 12 to the hours of pm times\n"
    f"for example:\n"
    f"    6:30 am is 0630 in 24-hour time while\n"
    f"    6:30 pm is 1830 in 24-hour time.\n"
)

# Get the current time from the user
time_of_day = int(input("In 24-hour time format, what time is it? "))

# Respond with a quip based on the time they entered
if time_of_day > 2359:
    print("What dimension are you getting extra hours from?")
elif time_of_day >= 2200 or time_of_day < 600:
    print("Why are you answering questions on the computer? Go back to bed!")
elif time_of_day >= 1800:
    print(
        f"If your school work is done, you can relax a bit; otherwise "
        f"do your coursework!"
    )
elif time_of_day >= 1700:
    print("Get some dinner.")
elif time_of_day >= 1300:
    print("Study time.")
elif time_of_day >= 1200:
    print("Get some lunch.")
elif time_of_day >= 700:
    print("Time to start you studying.")
else:
    print("Time to wake up, shower and get breakfast.")
