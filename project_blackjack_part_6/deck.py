import random

# 1)
# 
# Function: print_card
# 
# Prints the given card's official name.
# 
# Args:
#   card_rank: The numeric representation of a card.
# 
# Example:
#   print_card(2) prints out
#   Drew a 2
# 
#   print_card(11) prints out
#   Drew a Jack
def print_card(card_rank):
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    # All other cards are named by their rank.
    card_name = card_rank

  print('Drew a ' + str(card_name))

# 2)
# 
# Function: draw_card
# 
# Draws a new random card, prints its name, and returns its face value.
# 
# Returns:
#   Face value of chosen card. Face value of a card is the same as numeric value,
#   except for Ace, Jack, Queen, and King.
# 
# Examples:
#   draw_card() prints "Drew a Jack" and returns 11 (if card drawn is Ace)
#   draw_card() prints "Drew a 4" and returns 4  (if card drawn is 4)
#   draw_card() prints "Drew a 10" and returns 10 (if card drawn is Jack, Queen, King)
def draw_card():
  card_rank = random.randint(1, 13)
  print_card(card_rank)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
    card_value = 10
  elif card_rank == 1:
    # Aces are worth 11.
    card_value = 11
  else:
    # All other cards are worth the same as
    # their rank.
    card_value = card_rank

  return card_value

# 3)
# 
# Function: print_header
# 
# Prints the given message formatted as a header.
# 
# Args:
#   message: The message to be printed.
# 
# Example:
#   print_header("YOUR TURN") prints out
#   -----------
#   YOUR TURN
#   ----------- 
def print_header(message):
  """Prints the given message formatted as a header.
  
  Args:
    message: The message to be printed.

  Example:
    print_header("YOUR TURN") prints out
    -----------
    YOUR TURN
    ----------- 
  """
  print('-----------')
  print(message)
  print('-----------')

# 4)
# 
# Function: draw_starting_hand
# 
# Prints turn header and draws a starting hand, which is two cards.
# 
# Args:
#   name: The name of the player whose turn it is.
# 
# Returns:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
  print_header(name + ' TURN')
  return draw_card() + draw_card()

# 5)
# 
# Function: print_end_turn_status
# 
# Prints the hand total and status at the end of a player's turn.
# 
# Args:
#   hand: The sum of of all the cards in the hand.
# 
# Examples:
#   print_end_turn_status(15) prints out
#   Final hand: 15.
# 
#   print_end_turn_status(21) prints out
#   Final hand: 21.
#   BLACKJACK!
# 
#   print_end_turn_status(25) prints out
#   Final hand: 25.
#   BUST.
def print_end_turn_status(hand):
  print('Final hand: ' + str(hand) + '.')

  if hand == 21:
    print('BLACKJACK!')
  elif hand > 21:
    print('BUST.')

# 6)
# 
# Function: print_end_game_status
# 
# Prints the end game banner and the winner based on the final hands.
# 
# Args:
#   user_hand: The sum of all the cards in the user's hand.
#   dealer_hand: The sum of all the cards in the dealer's hand.
# 
# Examples:
#   print_end_game_status(21, 18) prints out
#   -----------
#   GAME RESULT
#   -----------
#   You win!
# 
#   print_end_game_status(18, 21) prints out
#   -----------
#   GAME RESULT
#   -----------
#   Dealer wins!
# 
#   print_end_game_status(24, 22) prints out
#   -----------
#   GAME RESULT
#   -----------
#   Tie.
def print_end_game_status(user_hand, dealer_hand):
  print_header('GAME RESULT')

  if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
    print('You win!')
  elif dealer_hand <= 21 and (dealer_hand > user_hand or user_hand > 21):
    print('Dealer wins!')
  else:
    print('Tie.')
