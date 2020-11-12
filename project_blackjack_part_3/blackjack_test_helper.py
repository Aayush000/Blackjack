from unittest import TestCase, main
from unittest.mock import patch
import io
import sys 
from contextlib import contextmanager

def printValue(question, answer):
  print(question + answer)
  return answer
  
def test(side_effect, randint_mock, input_mock, answers):
  """ Mocks randint and runs function with mock """
  answers.reverse()
  randint_mock.side_effect = side_effect
  input_mock.side_effect = lambda question: printValue(question, answers.pop())
  old_stdout = sys.stdout
  new_stdout = io.StringIO()
  sys.stdout = new_stdout
  import blackjack
  output = new_stdout.getvalue()
  sys.stdout = old_stdout
  return(output)

class BlackjackPart2Test(TestCase):
  def setUp(self):
    """ Takes I/O for arguments to function."""
    args = input().split('), (')
    self.cards = list(map(lambda x: int(x), (args[0] + ')').strip(')(').split(', ')))
    self.responses = list(map(lambda x: x.strip('\"'), ("(" + args[1]).strip(')(').split(', ')))

  @patch('random.randint')
  @patch('builtins.input')
  def test_blackjack(self, input_mock, randint_mock):
    """ Runs tests """
    print(test(self.cards, randint_mock, input_mock, self.responses).strip())

if __name__ == '__main__':
    main()
