""" 17. **Temperature Converter**
**Description:**  
Convert temperature from Celsius to Fahrenheit or vice versa based on user choice.
**Conversion Formulas:**  
- Celsius to Fahrenheit: `(C * 9/5) + 32`
- Fahrenheit to Celsius: `(F - 32) * 5/9`
**Input:**  
Two inputs:1. A character `unit` indicating the conversion direction (`'C'` for Celsius to Fahrenheit, `'F'` for Fahrenheit to Celsius).
2. A floating-point number representing the temperature.
**Output:**  
Print the converted temperature rounded to two decimal places. If the unit is invalid, print `"Invalid unit"`. """

print("Temperature Converter")

print("1.Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius")

check=input("Enter Choice: ")

if check=="1":
    cel=int(input("Enter the Celcius: "))
    print("Fahrenheit: ",cel*9/5+32)
elif check=="2":
    fahr=int(input("Enter the Fahrenhiet: "))
    print("Celcius: ",fahr-32*5/9)
""" else:
    print("Invalid Choice..!") """