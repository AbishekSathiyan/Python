""" **Letter Grade to Description**
**Description:**  
Provide a description based on the letter grade.
**Descriptions:**  
- `A`: Excellent
- `B`: Good
- `C`: Average
- `D`: Below Average
- `F`: Fail
**Input:**  
A single uppercase letter (`A`, `B`, `C`, `D`, `F`).
**Output:**  
Print the corresponding description. If the grade is invalid, print `"Invalid grade"`.
 """
 
print("Letter Grade")
grade=input("Enter Grade: ")

if grade=='A':
    print("Excellent")
elif grade=='B':
    print("Good")
elif grade=='C':
    print("Average")
elif grade=='D':
    print("Below Average")
elif grade=='F':
    print("Fail")
else:
    print("Invalid Grade")