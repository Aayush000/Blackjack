# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint

# Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
print('-----------')
print('YOUR TURN')
print('-----------')

card_rank = randint(1, 13)
if card_rank == 1:
  card_name = 'Ace'
elif card_rank == 11:
  card_name = 'Jack'
elif card_rank == 12:
  card_name = 'Queen'
elif card_rank == 13:
  card_name = 'King'
else:
  card_name = card_rank

print('Drew a ' + str(card_name))

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  card1_value = 10
elif card_rank == 1:
  card1_value = 11
else:
  card1_value = card_rank

card_rank = randint(1, 13)
if card_rank == 1:
  card_name = 'Ace'
elif card_rank == 11:
  card_name = 'Jack'
elif card_rank == 12:
  card_name = 'Queen'
elif card_rank == 13:
  card_name = 'King'
else:
  card_name = card_rank

print('Drew a ' + str(card_name))

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  card2_value = 10
elif card_rank == 1:
  card2_value = 11
else:
  card2_value = card_rank

user_hand = card1_value + card2_value

response = input('You have ' + str(user_hand) + '. Hit (y/n)? ')
while user_hand < 21 and response == 'y':
  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  print('Drew a ' + str(card_name))

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank
  user_hand = user_hand + card_value
  if user_hand < 21:
    response = input('You have ' + str(user_hand) + '. Hit (y/n)? ')

print('Final hand: ' + str(user_hand) + '.')
if user_hand == 21:
  print('BLACKJACK!')
elif user_hand > 21:
  print('BUST.')

print('-----------')
print('DEALER TURN')
print('-----------')

card_rank = randint(1, 13)
if card_rank == 1:
  card_name = 'Ace'
elif card_rank == 11:
  card_name = 'Jack'
elif card_rank == 12:
  card_name = 'Queen'
elif card_rank == 13:
  card_name = 'King'
else:
  card_name = card_rank

print('Drew a ' + str(card_name))

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  card1_value = 10
elif card_rank == 1:
  card1_value = 11
else:
  card1_value = card_rank

card_rank = randint(1, 13)
if card_rank == 1:
  card_name = 'Ace'
elif card_rank == 11:
  card_name = 'Jack'
elif card_rank == 12:
  card_name = 'Queen'
elif card_rank == 13:
  card_name = 'King'
else:
  card_name = card_rank

print('Drew a ' + str(card_name))

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  card2_value = 10
elif card_rank == 1:
  card2_value = 11
else:
  card2_value = card_rank

dealer_hand = card1_value + card2_value

while dealer_hand <= 17:
  print('Dealer has ' + str(dealer_hand) + '.')

  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  print('Drew a ' + str(card_name))

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank

  dealer_hand = dealer_hand + card_value

print('Final hand: ' + str(dealer_hand) + '.')
if dealer_hand == 21:
  print('BLACKJACK!')
elif dealer_hand > 21:
  print('BUST.')

print('-----------')
print('GAME RESULT')
print('-----------')

if dealer_hand <= 21 and (dealer_hand > user_hand or user_hand > 21):
  print('Dealer wins!')
elif user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
  print('You win!')
else:
  print('Tie.')
