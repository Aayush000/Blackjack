from deck import print_card, draw_card, print_header, draw_starting_hand, print_end_turn_status, print_end_game_status
from unittest import TestCase, main
from unittest.mock import patch
import io
import sys

def __run_function(function, args=None):
  return function(args) if args else function()

def listify(given):
  return list(map(lambda x: int(x), (given.replace(' ', ', ')).strip(')(').split(', ')))

def run_test(randint_mock, function, args=None, mocked_ints=[]):
    randint_mock.side_effect = mocked_ints # set randint calls to provided mocked_ints
    
    # Save printed output into variable so can return it to compare in test
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    function_return = __run_function(function, args)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return(output, function_return) # return printed statements in student-run code

def run_test_multiple_params(function, args=None):
    # Save printed output into variable so can return it to compare in test
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    function_return = function(*args)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return(output, function_return) # return printed statements in student-run code

class BlackjackPart5Test(TestCase):
    num_to_fnc = {
      "1": print_card,
      "2": draw_card,
      "3": print_header,
      "4": draw_starting_hand,
      "5": print_end_turn_status,
      "6": print_end_game_status,
    }

    def setUp(self):
      """
      As input, the first argument is going to map to functions:
      1 - print_card(card_rank)
      2 - draw_card()
      3 - print_header(message)
      4 - draw_starting_hand(name)
      5 - print_end_turn_status(hand)
      6 - print_end_game_status(user_hand, dealer_hand)

      The second input is going to be any arguments if necessary

      Third input is going to be integers to randint
      """
      args = input().split(',') # ask for input, will type this input into Mimir
      self.input_function = int(args[0])
      self.function = self.num_to_fnc[args[0].strip()]
      self.args = args[1].strip() if len(args) > 1 else None
      self.args = int(self.args) if self.input_function == 1 or self.input_function == 5 else self.args
      self.randint_numbers = listify(args[2].strip()) if len(args) > 2 else []

      if self.input_function == 6:
        parameters = args[1].strip()
        self.args = list(map(lambda x: int(x), list(parameters.strip(')(').split(' '))))

    @patch('random.randint')
    def test_stand(self, randint_mock):
        response = run_test(randint_mock, self.function, self.args, self.randint_numbers) if self.input_function <= 5 else run_test_multiple_params(self.function, self.args)
        print(response[0].strip())

        if self.input_function == 2:
          print(response[1])

if __name__ == '__main__':
    main()
