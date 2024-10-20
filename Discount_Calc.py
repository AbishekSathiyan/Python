"""  16. **Discount Calculator**
**Description:**  
Calculate the final price after applying a discount based on the original price.
**Discount Rules:**  
- If price > $1000: 10% discount
- If price > $500 and ≤ $1000: 5% discount
- Otherwise: No discount
**Input:**  
A floating-point number `price`.

Discount Amount = Original Price – New Price After Discount

discount price=original_price-(original_price*discount/100)

**Output:**  
Print the final price after discount, rounded to two decimal places."""
 

print("Discount Calculator")

o_price = float(input("Enter Total Price: "))   

 
print("Original Price:", o_price)
 
if o_price > 1000:
    discount_price = o_price - (o_price * 10 / 100)  # 10% Discount
    print("Discounted Price: ", discount_price)
elif o_price > 500 and o_price <= 1000:
    discount_price = o_price - (o_price * 5 / 100)  # 5% Discount
    print("Discounted Price: ", discount_price)
else:
    print("No discount applicable. Original Price: ", o_price)

     