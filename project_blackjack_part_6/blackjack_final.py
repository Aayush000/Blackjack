# DO NOT REMOVE
from deck import print_card, draw_card, print_header, draw_starting_hand, print_end_turn_status, print_end_game_status

print_header("YOUR TURN")

user_hand = 0
for index in range(2):
    user_hand += draw_card()

while user_hand < 21 and input('You have ' + str(user_hand) + '. Hit (y/n)? ') == 'y':
    user_hand += draw_card()

print_end_turn_status(user_hand)
print_header("DEALER TURN")

dealer_hand = 0
while dealer_hand <= 17:
    dealer_hand += draw_card()

print_end_turn_status(dealer_hand)
print_end_game_status(user_hand, dealer_hand)

