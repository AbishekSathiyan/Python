""" ### 14. **Grade Pass/Fail Checker**
**Description:**  
Determine if a student has passed or failed based on their marks and attendance.
**Passing Criteria:**  
- Marks ≥ 40 **and**
- Attendance ≥ 75%
**Input:**  
Two integers:
1. `marks` (0-100)
2. `attendance` (0-100)
**Output:**   Print `"Pass"` if both criteria are met, otherwise print `"Fail"` """

mark=int(input("Enter Your Mark: "))
attendance=int(input("Enter Your Attendance Percentage: "))

if mark >= 40 and attendance >=75:
    print("You are Pass")
else:
    print("You are Fail")