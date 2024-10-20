"""  11. **Triangle Type Identifier**
**Description:**  
Determine the type of a triangle based on the lengths of its sides.
**Types:**  
- Equilateral: All sides equal.
- Isosceles: Any two sides equal.
- Scalene: All sides different.
**Input:**  
Three positive integers `a`, `b`, and `c` representing the sides of a triangle.
**Output:**  
Print `"Equilateral"`, `"Isosceles"`, or `"Scalene"`. If the sides do not form a valid triangle, print `"Invalid triangle"`. """


side1=int(input("Enter Side 1:"))
side2=int(input("Enter Side 2:"))
side3=int(input("Enter Side 3:"))

print("Side 1: ",side1,"Side 2: ",side2,"Side 3:",side3)
    
if side1 == side2 and side2 == side3 and side3 ==side1 :
    print("Equilateral")
elif side1 == side2 or side1 ==side3 or side3 == side1:
    print("Isosceles")
else:
    print("Scalene")