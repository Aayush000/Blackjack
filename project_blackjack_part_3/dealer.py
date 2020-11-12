# Use randint to generate random cards. 
# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint

# Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
dealer_hand = 0 
drawn_count = 0 

while dealer_hand <= 17:
  if drawn_count >= 2:
    print('Dealer has ' + str(dealer_hand) + '.')

  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
    dealer_hand = dealer_hand + 11
  elif card_rank == 11:
    card_name = 'Jack'
    dealer_hand = dealer_hand + 10
  elif card_rank == 12:
    card_name = 'Queen'
    dealer_hand = dealer_hand + 10
  elif card_rank == 13:
    card_name = 'King'
    dealer_hand = dealer_hand + 10
  else:
    card_name = card_rank
    dealer_hand = dealer_hand + card_rank

  print('Drew a ' + str(card_name))

  drawn_count = drawn_count + 1

print('Final hand: ' + str(dealer_hand) + '.')
if dealer_hand == 21:
  print('BLACKJACK!')
elif dealer_hand > 21:
  print('BUST.')
