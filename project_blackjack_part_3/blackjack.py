from random import randint

print('-----------\nYOUR TURN\n-----------')

# Cards for user.
user_hand = 0
drawn_count = 0

while drawn_count < 2:
  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
    user_hand = user_hand + 11
  elif card_rank == 11:
    card_name = 'Jack'
    user_hand = user_hand + 10
  elif card_rank == 12:
    card_name = 'Queen'
    user_hand = user_hand + 10
  elif card_rank == 13:
    card_name = 'King'
    user_hand = user_hand + 10
  else:
    card_name = card_rank
    user_hand = user_hand + card_rank

  print('Drew a ' + str(card_name))

  drawn_count = drawn_count + 1

# Total sum of value of cards that the user have.
while user_hand < 21 and input('You have ' + str(user_hand) + '. Hit (y/n)? ') == 'y':
  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
    user_hand = user_hand + 11
  elif card_rank == 11:
    card_name = 'Jack'
    user_hand = user_hand + 10
  elif card_rank == 12:
    card_name = 'Queen'
    user_hand = user_hand + 10
  elif card_rank == 13:
    card_name = 'King'
    user_hand = user_hand + 10
  else:
    card_name = card_rank
    user_hand = user_hand + card_rank

  print('Drew a ' + str(card_name))

print('Final hand: ' + str(user_hand) + '.')
if user_hand == 21:
  print('BLACKJACK!')
elif user_hand > 21:
  print('BUST.')
    
print('-----------\nDEALER TURN\n-----------')

# Cards and their total sum for dealer.
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

print('-----------\nGAME RESULT\n-----------')

# Result of the game.
if user_hand == dealer_hand or (user_hand > 21 and dealer_hand > 21):
    print('Tie.')
elif (user_hand > dealer_hand and user_hand < 21 and dealer_hand < 21) or (user_hand == 21 and dealer_hand != 21) or (user_hand < 21 and dealer_hand > 21):
    print('You win!')
elif (user_hand < dealer_hand and user_hand < 21 and dealer_hand < 21) or (dealer_hand == 21 and user_hand != 21) or (dealer_hand < 21 and user_hand > 21):
    print('Dealer wins!')