student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80 and score <= 90:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
for k in student_grades:
   print(f"{k}: {student_grades[k]}")
 