from importlib import reload
from unittest import TestCase, main
from unittest.mock import patch
import io
import sys

def print_value(question, answer):
    print(question + answer)
    return answer

def run_test(user_cards, answers, dealer_cards, randint_mock, input_mock, imported):
    """
    Mocks randint and runs function with mock

    Args:
      randint_mock - patched random.randint()
      cards - desired input for random.randint()
      input_mock - patched bultins.input()
      answers - desired input for builtins.input()
      imported - whether module was imported already; always pass in True for your tests
    """
    answers.reverse() # reverses answers so can pop off list
    randint_mock.side_effect = user_cards + dealer_cards # set randint calls to cards
    input_mock.side_effect = \
        lambda question: print_value(question, answers.pop()) # print input question along with given answer

    # Save printed output into variable so can return it to compare in test
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    import blackjack_final
    if imported:
        reload(blackjack_final)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output # return printed statements in student-run code

class BlackjackPart6Test(TestCase):

    @patch('random.randint')
    @patch('builtins.input')
    def test_0_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock, False)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    # Make sure all your test functions start with test_
    # Follow indentation of test_example
    @patch('random.randint')
    @patch('builtins.input')
    def test_dealer_win1(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([3, 7, 7], ['y', 'n'], [4, 5, 10], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 7\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_dealer_win2(self, input_mock, randint_mock):
        '''
        The user receive cards that end up with a hand more than 21 and dealer end up with a hand less than 21.
        The dealer wins as the user gets busted.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([5, 11, 9], ['y'], [1, 8], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a Jack\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 8\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_dealer_win3(self, input_mock, randint_mock):
        '''
        The dealer ends with the hand exactly equal to 21 and user ends with the hand less than 21.
        The dealer wins by having a blackjack.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([6, 10, 4], ['y', 'n'], [12, 1], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 10\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('random.randint')
    @patch('builtins.input')
    def test_dealer_win4(self, input_mock, randint_mock):
        '''
        The dealer ends with the hand exactly equal to 21 and user ends with the hand more than 21.
        The dealer wins by having a blackjack and as user is busted.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([6, 10, 6], ['y', 'n'], [12, 1], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 10\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('random.randint')
    @patch('builtins.input')
    def test_user_win1(self, input_mock, randint_mock):
        '''
        The user ends with the hand of exactly 21 and dealer ends with the hand less than 21.
        The user wins by having a blackjack.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([10, 1], [], [2, 11, 8], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a Jack\n" \
                   "Drew a 8\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_user_win2(self, input_mock, randint_mock):
        '''
        The user ends with the hand of exactly 21 and dealer ends with the hand more than 21.
        The user wins by having a blackjack and as dealer is busted too.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([10, 1], [], [2, 11, 10], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a Jack\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)


    @patch('random.randint')
    @patch('builtins.input')
    def test_user_win3(self, input_mock, randint_mock):
        '''
        The dealer ends with the hand more than 21 and user ends with the hand less than 21.
        The user wins as the dealer is busted.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([12, 5, 5], ['y', 'n'], [4, 8, 1], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 8\n" \
                   "Drew a Ace\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('random.randint')
    @patch('builtins.input')
    def test_user_win4(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([4, 5, 12], ['y', 'n'], [1, 5, 2], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 5\n" \
                   "You have 9. Hit (y/n)? y\n" \
                   "Drew a Queen\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 5\n" \
                   "Drew a 2\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('random.randint')
    @patch('builtins.input')
    def test_tie_example1(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand more than 21.
        There is a tie as both the user and dealer are busted.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([8, 13, 11], ['y'], [3, 2, 11, 13], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 8\n" \
                   "Drew a King\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a Jack\n" \
                   "Final hand: 28.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 2\n" \
                   "Drew a Jack\n" \
                   "Drew a King\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Tie.\n"
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_tie_example2(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        There is a tie as both the user and dealer has a hand which are equal to each other.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([8, 12], ['n'], [4, 3, 2, 9], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 8\n" \
                   "Drew a Queen\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 3\n" \
                   "Drew a 2\n" \
                   "Drew a 9\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Tie.\n"
        self.assertEqual(output, expected)

    @patch('random.randint')
    @patch('builtins.input')
    def test_tie_example3(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand equal to 21.
        There is a tie as both the user and dealer has a hand which are equal to each other.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([1, 12], [], [8, 7, 6], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a Queen\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 8\n" \
                   "Drew a 7\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Tie.\n"
        self.assertEqual(output, expected)


    # Write all your tests above this. Do not delete this line.
    

if __name__ == '__main__':
    main()