"""
Character Case Converter
Description:
Convert a given alphabet character to its opposite case.
**Input:**  
A single English letter (uppercase or lowercase).
**Output:**  
If the input is uppercase, convert it to lowercase. If it's lowercase, convert it to uppercase. If it's not an alphabet, print `"Not an alphabet"`.
 """

print("Character Case Converter")
text = input("Enter some text: ")


for i in text:
    if i.islower(): 
        print(i.upper(), end="")  
    elif i.isupper(): 
        print(i.lower(), end="")
    else:
        print(i, end="")
        