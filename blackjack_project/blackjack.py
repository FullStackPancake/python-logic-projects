import random


looping = True
while looping:

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    play = input("Do you wanna play the game of Black Jack, 'Y or N' \n").lower()
    random.shuffle(cards)

    if play == "y":

        dealer_hand = []
        player_hand = []


        # Player Cards Function
        def player_cards():
            player_hand.append(cards.pop())
            player_hand.append(cards.pop())
            print("Player hand: ", player_hand)


        player_cards()


        # Dealer Hand Function
        def dealer_hands():
            dealer_hand.append(cards.pop())
            dealer_hand.append(cards.pop())
            print(f"Dealer visible card: {dealer_hand[0]}")


        dealer_hands()


        # player_hand_total = 0
        # dealer_hand_total = 0

        # def calculate_score(player_hand, dealer_hand):
        #     player_hand_total = sum(player_hand)
        #     dealer_hand_total = sum(dealer_hand)
        #     return player_hand_total, dealer_hand_total
        # player_score, dealer_score = calculate_score(player_hand, dealer_hand)

        # Ace Adjusting Function
        def adjust_ace(hand):
            score = sum(hand)

            if score > 21 and 11 in hand:
                hand.remove(11)
                hand.append(1)
                score = sum(hand)

            return score


        player_score = adjust_ace(player_hand)
        dealer_score = adjust_ace(dealer_hand)

        print(f"Player score:  {player_score}")
        print(f"Dealer visible card: {dealer_hand[0]}")

        player_busted = False

        while True:
            hit_stand = input("Do you wish to 'hit or stand'? \n").lower()

            if hit_stand == "hit":
                player_hand.append(cards.pop())
                player_score = adjust_ace(player_hand)
                print(f"Player hand: {player_hand} and score: {player_score}")

                if player_score > 21:
                    print("You went over 21, Bust")
                    print(f"Dealer hand: {dealer_hand} and score: {dealer_score}")
                    player_busted = True
                    break

            elif hit_stand == "stand":
                print(f"Dealer hand : {dealer_hand} and score: {dealer_score}")
                print(f"Player hand: {player_hand} and score: {player_score}")
                break

            else:
                print("Please enter 'hit' or 'stand'.")

        # Dealer Turn
        if not player_busted:

            while dealer_score < 17:
                dealer_hand.append(cards.pop())
                dealer_score = adjust_ace(dealer_hand)
                print(f"Dealer hand: {dealer_hand} and score: {dealer_score}")

                player_score = adjust_ace(player_hand)
                dealer_score = adjust_ace(dealer_hand)

            # Compare Scores
            if dealer_score > 21:
                print("Player wins")
            elif player_score > dealer_score:
                print("player wins")
            elif dealer_score > player_score:
                print("dealer wins")
            else:
                print("draw")
        else:
            print("Dealer wins")

        # Play the game again
        go_again = input("Do you want to play again? 'y' or 'n'\n").lower()

        if go_again == "n":
            print("Thanks for playing")
            break
        elif go_again != "y":
            print("Please enter 'y' or 'n'.")

    elif play == "n":
        print("Have a great day/evening")
        break

    else:
        print("Please enter 'y' or 'n'.")