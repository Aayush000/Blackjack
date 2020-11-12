# Use randint to generate random cards. 
# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint

# Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

counter = 0
hand = 0

while counter < 2:
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
    
    hand += card_value
    counter += 1

user_choice = ''

if hand < 21:
    user_choice = input('You have ' + str(hand) + '. Hit (y/n)? ')
else:
    if hand == 21:
        print('Final hand: 21.')
        print('BLACKJACK!')
    elif hand >21:
        print('Final hand: {}.'.format(hand))
        print('BUST.')
        
while user_choice == 'y' and hand < 21:
    
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
        
    hand += card_value
    
    if hand == 21:
        print('Final hand: 21.')
        print('BLACKJACK!')
    elif hand >21:
        print('Final hand: {}.'.format(hand))
        print('BUST.')
    else:
        user_choice = input('You have ' + str(hand) + '. Hit (y/n)? ')

if user_choice == 'n':
    print('Final hand: {}.'.format(hand))
