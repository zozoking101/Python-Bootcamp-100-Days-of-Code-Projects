student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
sum = 0
len = 0
for i in student_heights:
    sum += i
    len += 1
avg = sum / len
print(f"Average = {avg:.0f}")