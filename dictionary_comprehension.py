import random
import pandas as pd
# names = ['zoe', 'zion', '123']
# positions = [1, 7, 3]

# new_dict = {names:positions for (names, positions) in zip(names, positions)}

# print(new_dict)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {name:random.randint(20, 100) for name in names} 

numbers = range(1, 101)
cubes = {number: number ** 3 for number in numbers}

students = {i:item for (i,item) in enumerate(student_score.items())}

passed_students = {i:j for (i, j) in student_score.items() if j >= 60}

# Ex 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow"
result = {i:len(i) for i in sentence.split()}

# Ex 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def f(c):
    return ((c * 9/5) + 32)


weather_f = {day: f(c) for (day, c) in weather_c.items()}

student_dict = {
    "student": ["Anglea", "James", "Lily"],
    "score": [56, 76, 98],
}

data = pd.DataFrame(student_dict)

# for (i, j) in data.items():
#     print(j)
    
for (i, j) in data.iterrows():
    print(j.student, j.score)