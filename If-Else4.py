""" 10. **Age Category**
**Description:**  
Categorize a person's age group.
**Categories:**  
- 0-12: `"Child"`
- 13-19: `"Teenager"`
- 20-59: `"Adult"`
- 60 and above: `"Senior"`
**Input:**  
An integer `age`.
**Output:**  
Print the corresponding age category. If the age is negative, print `"Invalid age"`.
 """


print("Divide Age Category")
age=int(input("Enter Your Age: "))
if age>0 and age<=12:
    print("You are Child...")
elif age>=13 and age<20:
    print("You are Teenager")
elif age>=20 and age<=59:
    print("You are Adult")
elif age>59:
    print("You are Senior")