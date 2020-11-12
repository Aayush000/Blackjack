card_rank = int(input())

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  card_value = 10
elif card_rank == 1:
  card_value = 11
else:
  card_value = card_rank

print('Your hand value is ' + str(card_value) + '.')
