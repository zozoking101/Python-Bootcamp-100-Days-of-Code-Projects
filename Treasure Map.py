# Treasure Map

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

position = input("Where do you want to put the treasure? (x, y)")
col = int(position[0])-1
row = int(position[1])-1

#if row == 1:
#    row1[col] = 'X'
#elif row == 2:
#    row2[col] = 'X'
#elif row == 3:
#    row3[col] = 'X'
#else:
#    print("Error!")

#sel_row = map[row - 1]
#sel_row[col] = 'X'

map[row][col] = 'X'
print(f'{row1}\n{row2}\n{row3}')