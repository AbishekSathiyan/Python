""" 13. **Simple Interest Calculator**
**Description:**  
Calculate the simple interest based on principal, rate, and time.
**Formula:**  
Simple Interest = (Principal * Rate * Time) / 100
**Input:**  
Three floating-point numbers: `principal`, `rate`, and `time`.
**Output:**  
Print the simple interest rounded to two decimal places.
 """
 
 
principal=int(input("Enter Principal Amount: "))
rate=int(input("Enter Rate: "))
time=int(input("Enter Time: "))

principal=float(principal)
rate=float(rate)
time=float(time)

Simple_Interest=principal*rate*time/100
print("Simple_Interest:",Simple_Interest)
print("Total: ",principal+Simple_Interest)