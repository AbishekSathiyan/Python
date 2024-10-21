""" Grade Point Average (GPA) Calculator**
**Description:**  
Calculate GPA based on the number of subjects and their respective marks.
**Grading Scale:**  
- 90-100: 4.0
- 80-89: 3.0
- 70-79: 2.0
- 60-69: 1.0
- Below 60: 0.0
**Input:**  
First, an integer `n` representing the number of subjects.  
Then, `n` integers representing the marks for each subject.
**Output:**  
Calculate and print the average GPA, rounded to two decimal places.
---
 """
 
subjects = int(input("Enter Number of Subjects: "))
marks = []

print("Enter the Marks Subjectwise:")
for i in range(subjects):
    mark = int(input(f"Mark for subject {i + 1}: "))
    marks.append(mark)

total_points = 0

# Calculate total GPA points based on marks
for mark in marks:
    if 90 <= mark <= 100:
        total_points += 4.0
    elif 80 <= mark < 90:
        total_points += 3.0
    elif 70 <= mark < 80:
        total_points += 2.0
    elif 60 <= mark < 70:
        total_points += 1.0
    else:
        total_points += 0.0

# Calculate and print the average GPA
average_gpa = total_points / subjects
print("Average GPA: {:.2f}".format(average_gpa))
