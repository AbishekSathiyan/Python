""" # 6. **BMI Calculator**
**Description:**  
Calculate the Body Mass Index (BMI) and categorize it.
**BMI Formula:**  
BMI = weight (kg) / (height (m))²
**Categories:**  
- BMI < 18.5: `"Underweight"`
- 18.5 ≤ BMI < 24.9: `"Normal weight"`
- 25 ≤ BMI < 29.9: `"Overweight"`
- BMI ≥ 30: `"Obesity"`
**Input:**  
Two floating-point numbers: `weight` (in kilograms) and `height` (in meters).
**Output:**  
Print the BMI category."""

print("BMI Calculator")
weight=int(input("Enter Your Weight in (KG): "))
height=float(input("Enter Your Height in (CM): "))
bmi=0

height=height/100 # Height Convert Centimeter to Meter
print(height," meter(s)")

bmi=weight/(height ** 2) # Calculate BMI using height squared

if bmi<18.5:
    print("You are Under Weight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal Weight")
elif bmi>=25 and bmi < 29.9:
    print("Over Weight")
elif bmi >=30:
    print("Obesity")
    
