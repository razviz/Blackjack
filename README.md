# Blackjack
This is a terminal based python game for "Blackjack", and I created it in my previous "Intro to Python Programming" course for the final assignment.

How the game works (instructions):
* The possible card values range from 1 to 10 and, unlike a real deck, the probability of drawing a card is equal
* The game begins by dealing two visible cards to the player, and two cards to the dealer. However, in the case of the dealer, one card is visible to other player while the other is hidden.
* The player decides whether to "hit" (draw another card), or "stand" which ends their turn.
* The player may hit any number of times. Should the total of the cards exceed 21, the player "busts" and loses the game to the dealer. The round then ends and the dealer does not have to draw/show any additional cards.
* If the player reaches 21, the player stands
* The dealer's turn begins by revealing the hidden card
* The dealer must continue to hit if the total is 16 or less, and must stand if the value is 17 or more
* The dealer busts if their total is over 21 and the player wins.
* The dealer wins all ties (i.e. if both the dealer and the player reach 21, the dealer wins)
