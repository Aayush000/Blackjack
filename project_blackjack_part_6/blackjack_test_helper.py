from unittest import TestCase, main
from unittest.mock import patch
import io
import sys

def print_value(question, answer):
    print(question + answer)
    return answer

def run_test(randint_mock, cards, input_mock, answers):
    """
    Mocks randint and runs function with mock

    Args:
      randint_mock - patched random.randint()
      cards - desired input for random.randint()
      input_mock - patched bultins.input()
      answers - desired input for builtins.input()
    """
    answers.reverse() # reverses answers so can pop off list
    randint_mock.side_effect = cards # set randint calls to cards
    input_mock.side_effect = \
        lambda question: print_value(question, answers.pop()) # print input question along with given answer

    import blackjack_final # run code with mocked randint and input


class BlackjackPart6Test(TestCase):

    def setUp(self):
      args = input().split('), (') # ask for input, will type this input into Mimir
      self.cards = list(map(lambda x: int(x), (args[0] + ')').strip(')(').split(', ')))
      self.responses = list(map(lambda x: x.strip('\"'), ("(" + args[1]).strip(')(').split(', ')))

    @patch('random.randint')
    @patch('builtins.input')
    def test_stand(self, input_mock, randint_mock):
        run_test(randint_mock, self.cards, input_mock, self.responses)

if __name__ == '__main__':
    main()
