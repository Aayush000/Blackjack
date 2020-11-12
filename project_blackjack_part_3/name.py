card_rank = int(input())

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
