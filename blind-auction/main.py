import art
print(art.logo)

print("Welcome to the secret auction program.")

auction_dictionary = {}

while True:

    name = input("Please enter your name: \n")
    bid = int(input("Please enter your bid: \n$" ))

    auction_dictionary[name] = bid

    other_bid = input("is there other bidders as well? y/n: \n" )

    if other_bid == "y":
        print("\n"*100)
    elif other_bid == "n":
        break

highest_bid = 0
winner = ""

for name in auction_dictionary:
    if auction_dictionary[name] > highest_bid:
        highest_bid = auction_dictionary[name]
        winner = name
print(f"Highest bid is {highest_bid} and the winner is {winner}")