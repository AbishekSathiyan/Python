n = int(input("Enter How Many Numbers: "))  # Convert input to integer
numbers = []
prime = []
composite = []

for _ in range(n):  # Use underscore for unused loop variable
    number = int(input("Enter a Number: "))  # Convert input to integer
    numbers.append(number)

for number in numbers:
    if number < 2:  # Numbers less than 2 are neither prime nor composite
        continue
    elif number == 2:  # 2 is a prime number
        prime.append(number)
    else:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                composite.append(number)
                is_prime = False
                break
        if is_prime:
            prime.append(number)

# Print the results
print("Prime Numbers:", prime)
print("Composite Numbers:", composite)
