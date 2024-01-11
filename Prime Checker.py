def prime_checker(number):
    if number == 2 or number == 3:
        print("Prime number")
    elif number < 2:
        print("Not a prime number")
    else:
        is_prime = True
        for i in range(2, int(number/2)):
            check = number % i
            if check == 0:
                is_prime = False
                break
        if is_prime == True:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)