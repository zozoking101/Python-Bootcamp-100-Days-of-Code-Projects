# Love Letters

fdigit = 0
ldigit = 0
true = ['T', 'R', 'U', 'E']
love = ['L', 'O', 'V', 'E']
p1name = input("Enter the name of the first person: ").upper()
p2name = input("Enter the name of the second person: ").upper()
for i in p1name:
    if "T"or"R"or"U"or"E" == i:
        fdigit += 1
    if "L"or"O"or"V"or"E" == i:
        ldigit += 1
for j in p2name:
    if "T"or"R"or"U"or"E" == j:
        fdigit += 1
    if "L"or"O"or"V"or"E" == j:
        ldigit += 1
percent = str(fdigit) + str(ldigit)
print(f"You are {percent}% compatible!")