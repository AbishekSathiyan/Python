# 5. **Vowel or Consonant**
# **Description:**  
# Check whether a given character is a vowel or a consonant.
# **Input:**  
# A single lowercase or uppercase English letter.
# **Output:**  
# Print `"Vowel"` if the character is a vowel (`a`, `e`, `i`, `o`, `u`), otherwise print `"Consonant"`.

vowels=['a','e','i','o','u','A','E','I','O','U']

i=input("Enter the Character to Check Vowel: ")
if i in vowels:
    print(i,"is Vowel")
else:
    print(i,"is Consonant")
    