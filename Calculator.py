#Calculator 

#Add

def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

Calculator_running = True
reoperate = False

while Calculator_running:
    if reoperate:
        num1 = result
        reoperate = False
    else:
        num1 = float(input("What's the first number?: "))
        
    operation = input("Which operation (+ - * /):  ")
    num2 = float(input("What's the next number?: "))
   
    function = operations[operation]
    result = function(num1, num2)
    print(f"\n{num1} {operation} {num2} = {result}\n")
    
    to_continue = int(input(f"Do you want to: \n1. Operate on {result}\n2. Start again \n3. Exit\nChoose(1 - 3)\n: "))
    
    if to_continue == 1:
        reoperate = True
    elif to_continue == 2:
        pass
    elif to_continue == 3:
        Calculator_running = False
    else:
        print("Invalid choice")
        break