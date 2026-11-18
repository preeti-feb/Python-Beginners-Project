print('*' * 40)
print("Student Marks Calculator")
print('*' * 40)

student_name = input("\nEnter the student name: ")
obtained_marks = []
marks = 0


for m in range(1, 6):
    subject_marks = int(input("\nEnter your subject marks one by one: "))
    obtained_marks.append(subject_marks)
    marks += subject_marks

total_marks = 500
percentage = (marks / total_marks) * 100

if percentage >= 90 and percentage <= 100:
    grade = "A+"
elif percentage >= 80 and percentage < 90:
    grade = "A"
elif percentage >= 70 and percentage < 80:
    grade = "B"
elif percentage >= 60 and percentage < 70:
    grade = "C"
elif percentage >= 50 and percentage < 60:
    grade = "D"
elif percentage > 100 or percentage < 0:
    grade = "Invalid"
elif percentage >= 0 and percentage < 50:
    grade = "Fail"




print("\n`Final Report`")
print(f"Student name: {student_name}")
print(f"Obtinted marks: {obtained_marks}")
print(f"Total marks: {total_marks}")
print(f"Percentage {percentage}")
print(f"Your Grade: {grade}")
