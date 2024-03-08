with open("file1.txt") as f:
    with open("file2.txt") as g:
        a = f.readlines()
        b = g.readlines()
        c = [int(i.strip()) for i in a if i in b]
        print(c)
# Output: [3, 6, 5, 33, 12, 7, 42, 13]