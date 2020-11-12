card = int(input())

if card == 1:
    print('Drew a Ace')
elif card == 2 or card ==3 or card == 4 or card == 5 or card == 6 or card == 7 or card == 8 or card == 9 or card == 10:
    print('Drew a ' + str(card))
elif card == 11:
    print('Drew a Jack')
elif card == 12:
    print('Drew a Queen')
elif card == 13:
    print('Drew a King')


