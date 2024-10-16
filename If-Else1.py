# Control Structures
# Conditionals: if, else if, else statements

# # 2. **Leap Year Determination**
# **Description:**  
# Determine whether a given year is a leap year.
# **Rules for Leap Year:**  
# - A year is a leap year if it is divisible by 4 **and** not divisible by 100, **or** it is divisible by 400.
# **Input:**  
# An integer `year`.
# **Output:**  
# Print `"Leap Year"` if the year is a leap year, otherwise print `"Not a Leap Year"`.
# ---


year=int(input("Enter Year: "))

if year%4==0 and year%100 or year%400:
    print(year,"is Leap Year")
else:
    print(year,"is Not a Leap Year")