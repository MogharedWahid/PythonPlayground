from art import logo

print(logo)
print("Welcome to the secret auction program.")

def find_winner_bidder(bidders):
    winner = ""
    max_bid = 0
    for key in bidders:
        if bidders[key] > max_bid:
            max_bid = bidders[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${max_bid}")

bidders = {}
other_bidders = 'yes'
while other_bidders == 'yes':
    name = input("What is your name?: ")
    bid  = int(input("What is your bid?: $"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type \'yes\' or \'no\'.\n")
    print("\n" * 30)
find_winner_bidder(bidders)

