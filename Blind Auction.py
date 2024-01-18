print("Welcome to the blind auction")
AppRunning = True
Bidders = dict()
while AppRunning:
    name = input("What is your name?: ")
    Bidders[name] = int(input("What is your bid?: $"))
    to_continue = input("Are there any other bidders? Type 'yes' or'no'. ").lower()
    if to_continue in ['yes', 'y']:
        AppRunning =True
        clear_terminal()
    else:
        AppRunning = False
    
winner_name = max(Bidders, key=Bidders.get)
winning_bid = Bidders[winner_name]

print(f"/nThe winner of the auction is {winner_name} with a bid of ${winning_bid}!")