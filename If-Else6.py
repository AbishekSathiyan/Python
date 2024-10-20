"""  12. **Month Days Calculator**
**Description:**  
Find the number of days in a given month of a specific year.
**Input:**  
Two integers:
1. `month` (1 for January, 2 for February, ..., 12 for December)
2. `year`
**Output:**  
Print the number of days in the specified month. Account for leap years when determining February's days. If the month is invalid, print `"Invalid month"`.
"""


month = int(input("Enter Month: "))

if month < 1 or month > 12:
    print("Invalid Month..! ")
else:
    year = int(input("Enter Year: "))
    
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("29 Days")
        else:
            print("28 Days")
    
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        print("31 Days")
    
    else:
        print("30 Days")
