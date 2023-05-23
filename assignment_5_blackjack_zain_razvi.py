import random

def main():
    cards_of_player = []
    cards_of_dealer = []
    print("\nWelcome to Blackjack.\n")
    print(f'{"":-^50}')
    new_game = input("\n\nDo you wish to start a new game? (y/n): ")

    #If the player chooses yes, then a new game is started
    if new_game == "y" or new_game == "Y":

        #Dealer and player are given 2 random cards
        cards_of_dealer.append(random.randint(1, 10))
        cards_of_dealer.append(random.randint(1, 10))
        cards_of_player.append(random.randint(1, 10))
        cards_of_player.append(random.randint(1, 10))

        #Both of the player's cards are visible, but only one of the dealer's cards are visible (the other one is hidden)
        print(f'\n\nYou draw a {cards_of_player[0]} and a {cards_of_player[1]}. Your total is {sum(cards_of_player)}.')
        print(f'\n\nThe dealer draws a {cards_of_dealer[0]} and a hidden card.')

        #While the player's total is less than 21
        while sum(cards_of_player) < 21:
            
            hit_or_stand = input("\n\nHit or stand? (h/s): ")

            #If the player chooses to hit
            if hit_or_stand == "h" or hit_or_stand == "H":
                cards_of_player.append(random.randint(1, 10))
                print(f'\n\nHit! You draw a {cards_of_player[-1]}. Your total is {sum(cards_of_player)}.')

            #If the player chooses to stand
            elif hit_or_stand == "s" or hit_or_stand == "S":
                
                print(f'\n\nYou stand.\n\n\nThe dealer\'s hidden card is {cards_of_dealer[1]} and has a total of {sum(cards_of_dealer)}.')

                #while the dealer's total is 16 or less
                while sum(cards_of_dealer) <= 16:
                    cards_of_dealer.append(random.randint(1, 10))
                    print(f'\n\nHit! The dealer draws a {cards_of_dealer[-1]}. The dealer\'s total is {sum(cards_of_dealer)}.')
                
                #If the dealer's total is 17 or more
                else:
                    #Player wins if their total is greater than the dealer's
                    if sum(cards_of_player) > sum(cards_of_dealer):
                        print(f'\n\nThe dealer stands. \n\n\nYou have a total of {sum(cards_of_player)} and the dealer has {sum(cards_of_dealer)}.')
                        print('\n\nYou win!\n')
                        break  
                    #If the player's total is not greater than the dealer's
                    else:
                        #The dealer wins if there's a tie
                        if sum(cards_of_player) == sum(cards_of_dealer):
                            print(f'\n\nThe dealer stands. \n\n\nYou have a total of {sum(cards_of_player)} and the dealer has {sum(cards_of_dealer)}.')
                            print('\n\nThe dealer wins!\n')
                            break
                        #The dealer busts if their total is over 21
                        elif sum(cards_of_dealer) > 21:
                            print('\n\nDealer\'s busted. You win!\n')
                            break
                        #The dealer wins if their total is greater than the player's
                        elif sum(cards_of_dealer) > sum(cards_of_player):
                            print(f'\n\nThe dealer stands. \n\n\nYou have a total of {sum(cards_of_player)} and the dealer has {sum(cards_of_dealer)}.')
                            print('\n\nThe dealer wins!\n')
                            break
                        break
            
            #If the player types invalid input
            else:
                print('\n\nYou did not choose hit or stand, please enter a proper value ("h" for hit or "s" for stand).')
        
        #If the player's total is 21 or more
        else:

            #The player busts if their total is greater than 21
            if sum(cards_of_player) > 21:
                print(f'\n\nYou\'re busted. The dealer wins.\n')

            #If the player's total equals 21
            elif sum(cards_of_player) == 21:
                
                print(f'\n\nYou stand. The dealer reveals the hidden card of {cards_of_dealer[1]} and has a total of {sum(cards_of_dealer)}.')
                
                #while dealer's total is 16 or less
                while sum(cards_of_dealer) <= 16:
                    cards_of_dealer.append(random.randint(1, 10))
                    print(f'\n\nHit! The dealer draws a {cards_of_dealer[-1]}. The dealer\'s total is {sum(cards_of_dealer)}.')
                
                #If the dealer's total is 17 or more
                else:
                    #The player wins if their total is greater than the dealer's
                    if sum(cards_of_player) > sum(cards_of_dealer):
                        print(f'\n\nThe dealer stands. \n\n\nYou have a total of {sum(cards_of_player)} and the dealer has {sum(cards_of_dealer)}.')
                        print('\n\nYou win!\n')
                    #If the player's total is less than the dealer's
                    else:
                        #The dealer wins if there's a tie
                        if sum(cards_of_player) == sum(cards_of_dealer):
                            print(f'\n\nThe dealer stands. \n\n\nYou have a total of {sum(cards_of_player)} and the dealer has {sum(cards_of_dealer)}.')
                            print('\n\nThe dealer wins!\n')
                        #The dealer busts if their total is over 21
                        elif sum(cards_of_dealer) > 21:
                            print('\n\nDealer\'s busted. You win!\n')
    
    #If the player chooses no (anything besides "y" or "Y", such as "n", "N", or something else), then the program exits the game
    else:
        exit

if __name__ == '__main__':
    main()