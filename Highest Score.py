student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] =int(student_scores[n])
print(student_scores)
a = -1
for student in student_scores:
    if student > a:
        a = student
print(f"The highest score in the class is: {a}")