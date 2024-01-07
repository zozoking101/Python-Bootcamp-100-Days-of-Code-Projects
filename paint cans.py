import math
def paint_calc(height, width, cover):
    no_of_cans = math.ceil((height * width) / coverage)
    print(f"You'll need {no_of_cans:.0f} cans of paint")
    
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
no_of_cans = (test_h * test_w) / coverage    
paint_calc(height=test_h, width=test_w, cover=coverage)