""" 9. **Simple Calculator**
**Description:**  
Perform basic arithmetic operations based on user input.
**Input:**  
Three inputs:
1. An integer `a`.
2. An integer `b`.
3. A character `operation` representing the operation (`+`, `-`, `*`, `/`).

**Output:**  
Perform the operation `a op b` and print the result. Handle division by zero by printing `"Error: Division by zero"`.  and Check Valid Operator
or '"Error: Invalid Operator"' """

print("Simple Calculator Project")

a=float(input("Enter the First Number: "))
b=float(input("Enter the Second Number: "))
    
operation=input("Enter the Operation: ('+'-'*'/','%') : ")

if operation=='+':
    print("Addition = ",a+b)
elif operation=='-':
    print("Subtraction =",a-b)
elif operation=='*':
    print("Multiplication =",a*b)
elif operation=='/':
    if a==0 or b==0:
        print("Error ⚠ Division Operation not  by zero")
    else:
        print("Division =",a/b)

elif operation=='%':
    if a==0 or b==0:
        print("Error ⚠ Modulo Division Operation not  by zero")
    else:
        print("Modulo Division =",a%b)
else:
    print("Invalid Operation ⚠")
    