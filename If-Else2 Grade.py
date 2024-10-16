# 3. **Grading System**
# **Description:**  
# Assign a grade based on the marks obtained.
# **Criteria:**  
# - 90-100: Grade `A`
# - 80-89: Grade `B`
# - 70-79: Grade `C`
# - 60-69: Grade `D`
# - Below 60: Grade `F`
# **Input:**  
# An integer `marks` (0 ≤ marks ≤ 100).
# **Output:**  
# Print the corresponding grade (`A`, `B`, `C`, `D`, or `F`).
# ---

mark=int(input("Enter Your Marks:"))

if mark>90 and mark<=100:
    print("Grade A")
elif mark<90 and mark>=80:
    print("Grade B")
elif mark<80 and mark>=70:
    print("Grade C")
elif mark<70 and mark>=60:
    print("Grade D")
elif mark<60:
    print("Grade F")