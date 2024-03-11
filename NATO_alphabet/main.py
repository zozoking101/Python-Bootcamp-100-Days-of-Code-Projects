import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)

# Keyword Method with iterrows()
nato = {j.letter:j.code for (i, j) in df.iterrows()}
# print(nato)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    try:
        word = input("Enter a word: ")
        for i in word:
            if not i.isalpha():
                raise ValueError
    except ValueError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        name_list = [nato[i.upper()] for i in word if i.upper() in nato.keys()]
        print(name_list)
    


generate_phonetic()
