from random import randint

print('-----------\nYOUR TURN\n-----------')

# Storing a random number from 1 to 13
card_rank = randint(1, 13)

# Assigning the name of a card according to the position of card
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

# Providing the hand value to the user according to their chosen card
if card_rank == 1:
    user_hand_value_1 = 11
elif card_rank == 11 or card_rank == 12 or card_rank == 13:
    user_hand_value_1 = 10
else:
    user_hand_value_1 = card_rank
    
# Storing a random number from 1 to 13
card_rank = randint(1, 13)

# Assigning the name of a card according to the position of card
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

# Providing the hand value to the user according to their chosen card
if card_rank == 1:
    user_hand_value_2 = 11
elif card_rank == 11 or card_rank == 12 or card_rank == 13:
    user_hand_value_2 = 10
else:
    user_hand_value_2 = card_rank

user_hand_value = user_hand_value_1 + user_hand_value_2

# Checking if the user wants to take more cards if their hand value is smaller than 21 and providing more cards if they want to
while user_hand_value < 21 and input('You have ' + str(user_hand_value) + '.Hit (y/n)? ') == 'y':
    # Storing a random number from 1 to 13
    card_rank = randint(1, 13)

    # Assigning the name of a card according to the position of card
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
    
    # Providing the hand value to the user according to their chosen card
    if card_rank == 1:
        new_user_hand_value = 11
    elif card_rank == 11 or card_rank == 12 or card_rank == 13:
        new_user_hand_value = 10
    else:
        new_user_hand_value = card_rank

    user_hand_value = user_hand_value + new_user_hand_value

# Deciding the user's final hand value with their result if they are out or win or still in the game
if user_hand_value == 21:
    print('Final hand: ' + str(user_hand_value) + '.')
    print('BLACKJACK!')
elif user_hand_value > 21:
    print('Final hand: ' + str(user_hand_value) + '.')
    print('BUST.')
else:
    print('Final hand: ' + str(user_hand_value) + '.')
    
print('-----------\nDEALER TURN\n-----------')

# Storing a random number from 1 to 13
card_rank = randint(1, 13)

# Assigning the name of a card according to the position of card
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

# Providing the hand value to the dealer according to their chosen card
if card_rank == 1:
    dealer_hand_value_1 = 11
elif card_rank == 11 or card_rank == 12 or card_rank == 13:
    dealer_hand_value_1 = 10
else:
    dealer_hand_value_1 = card_rank

# Storing a random number from 1 to 13
card_rank = randint(1, 13)

# Assigning the name of a card according to the position of card
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

# Providing the hand value to the dealer according to their chosen card
if card_rank == 1:
    dealer_hand_value_2 = 11
elif card_rank == 11 or card_rank == 12 or card_rank == 13:
    dealer_hand_value_2 = 10
else:
    dealer_hand_value_2 = card_rank

dealer_hand_value = dealer_hand_value_1 + dealer_hand_value_2

# Checking the dealer hand value and continue on providing other cards if their hand value is less than 18
while dealer_hand_value <= 17:
    print('Dealer has ' + str(dealer_hand_value) + '.')
    
    # Storing a random number from 1 to 13
    card_rank = randint(1, 13)

    # Assigning the name of a card according to the position of card
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
    
    # Providing the hand value to the dealer according to their chosen card
    if card_rank == 1:
        new_dealer_hand_value = 11
    elif card_rank == 11 or card_rank == 12 or card_rank == 13:
        new_dealer_hand_value = 10
    else:
        new_dealer_hand_value = card_rank
        
    dealer_hand_value = dealer_hand_value + new_dealer_hand_value
    
# Deciding the dealer's final hand value with their result if they are out or win or still in the game
if dealer_hand_value == 21:
    print('Final hand: ' + str(dealer_hand_value) + '.')
    print('BLACKJACK!')
elif dealer_hand_value > 21:
    print('Final hand: ' + str(dealer_hand_value) + '.')
    print('BUST.')
else:
    print('Final hand: ' + str(dealer_hand_value) + '.')
    
print('-----------\nGAME RESULT\n-----------')

# Comparing the hand value of user and dealer to determine who won the game or if there is a tie
if user_hand_value == 21 and dealer_hand_value == 21:
    print('Tie.')
elif user_hand_value < 21 and dealer_hand_value < 21 and user_hand_value == dealer_hand_value:
    print('Tie.')
elif user_hand_value >= 21 and dealer_hand_value >= 21:
    print('Tie.')
elif dealer_hand_value <= 21 and user_hand_value > 21:
    print('Dealer wins!')
elif dealer_hand_value <= 21 and user_hand_value <= 21 and dealer_hand_value > user_hand_value:
    print('Dealer wins!')
elif user_hand_value <= 21 and dealer_hand_value > 21:
    print('You win!')
elif user_hand_value <= 21 and dealer_hand_value <= 21 and user_hand_value > dealer_hand_value:
    print('You win!')







