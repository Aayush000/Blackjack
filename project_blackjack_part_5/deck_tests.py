from deck import print_card, draw_card, print_header, draw_starting_hand, print_end_turn_status, print_end_game_status
from deck_test_helper import get_print, mock_random
import unittest
from unittest.mock import patch


class TestBlackjack(unittest.TestCase):
  """
  Class for testing Blackjack.

  There are two helper functions, get_print and mock_random, that can help you.

  get_print: returns the printed statements from running a provided function with provided arguments
  mock_random: use this if code calls randint. mock_random takes in a list of numbers that randint should
               be using and runs the provided function with provided arguments accordingly

  Example of calling print_card, which takes an argument and prints out card rank:
    get_print(print_card, 2) - returns string that gets printed out when print_card function gets called with 2
    To check whether the above printed correctly - self.assertEqual(get_print(print_card, 3), "Drew a 2\n")
    
  Example of calling draw_card(), which takes no arguments but uses randint:
    mock_random([3], draw_card)) - runs draw_card with 3 as the randint
    To check whether the above returned correctly - self.assertEqual(mock_random([3], draw_card)), 3)

    If the function takes in an argument, pass that as the last argument into mock_random()
    mock_random([3, 5], draw_starting_hand), "DEALER") - runs draw_starting_hand with 3 as first randint, 5 as secnd
    To check whether the above returned correctly - self.assertEqual(mock_random([3, 5], draw_starting_hand), "DEALER")
  """
  def test_print_card(self):
    """
    Example of a test to compare printed statements with expected
 
    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card, 2), "Drew a 2\n")  
 
  def test_mock_randint(self):
    """
    Example of a test to compare output for a function that calls randint
 
    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)
 
 
  # WRITE YOUR TESTS BELOW
  
  def test_print_card(self):
      self.assertEqual(get_print(print_card, 3), "Drew a 3\n")
      self.assertEqual(get_print(print_card, 7), "Drew a 7\n")
      self.assertEqual(get_print(print_card, 10), "Drew a 10\n")
      self.assertEqual(get_print(print_card, 1), "Drew a Ace\n")
      self.assertEqual(get_print(print_card, 11), "Drew a Jack\n")
      self.assertEqual(get_print(print_card, 12), "Drew a Queen\n")
      self.assertEqual(get_print(print_card, 13), "Drew a King\n")

  def test_print_header(self):
      self.assertEqual(get_print(print_header, "YOUR TURN"), "-----------\nYOUR TURN\n-----------\n")
      self.assertEqual(get_print(print_header, "DEALER TURN"), "-----------\nDEALER TURN\n-----------\n")
      self.assertEqual(get_print(print_header, "GAME RESULT"), "-----------\nGAME RESULT\n-----------\n")
      self.assertEqual(get_print(print_header, "DEALER"), "-----------\nDEALER\n-----------\n")
      self.assertEqual(get_print(print_header, "USER"), "-----------\nUSER\n-----------\n")
   
  def test_print_end_turn_status(self):
      self.assertEqual(get_print(print_end_turn_status, 11), "Final hand: 11.\n")
      self.assertEqual(get_print(print_end_turn_status, 19), "Final hand: 19.\n")
      self.assertEqual(get_print(print_end_turn_status, 20), "Final hand: 20.\n")
      self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
      self.assertEqual(get_print(print_end_turn_status, 25), "Final hand: 25.\nBUST.\n")
      self.assertEqual(get_print(print_end_turn_status, 28), "Final hand: 28.\nBUST.\n")

  def test_print_end_game_status(self):
      self.assertEqual(get_print(print_end_game_status, 19, 20), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
      self.assertEqual(get_print(print_end_game_status, 18, 21), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
      self.assertEqual(get_print(print_end_game_status, 26, 21), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
      self.assertEqual(get_print(print_end_game_status, 24, 19), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
      self.assertEqual(get_print(print_end_game_status, 19, 18), "-----------\nGAME RESULT\n-----------\nYou win!\n")
      self.assertEqual(get_print(print_end_game_status, 21, 20), "-----------\nGAME RESULT\n-----------\nYou win!\n")
      self.assertEqual(get_print(print_end_game_status, 21, 23), "-----------\nGAME RESULT\n-----------\nYou win!\n")
      self.assertEqual(get_print(print_end_game_status, 15, 25), "-----------\nGAME RESULT\n-----------\nYou win!\n")
      self.assertEqual(get_print(print_end_game_status, 19, 19), "-----------\nGAME RESULT\n-----------\nTie.\n")
      self.assertEqual(get_print(print_end_game_status, 21, 21), "-----------\nGAME RESULT\n-----------\nTie.\n")
      self.assertEqual(get_print(print_end_game_status, 23, 23), "-----------\nGAME RESULT\n-----------\nTie.\n")
      self.assertEqual(get_print(print_end_game_status, 22, 25), "-----------\nGAME RESULT\n-----------\nTie.\n")
    
  def test_draw_card(self):
      self.assertEqual(mock_random([3], draw_card), 3)
      self.assertEqual(mock_random([8], draw_card), 8)
      self.assertEqual(mock_random([1], draw_card), 11)
      self.assertEqual(mock_random([11], draw_card), 10)
      self.assertEqual(mock_random([12], draw_card), 10)
      self.assertEqual(mock_random([13], draw_card), 10)
    
  def test_draw_starting_hand(self):
      self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)
      self.assertEqual(mock_random([4, 5], draw_starting_hand, "DEALER"), 9)
      self.assertEqual(mock_random([1, 5], draw_starting_hand, "DEALER"), 16)
      self.assertEqual(mock_random([11, 12], draw_starting_hand, "DEALER"), 20)
      self.assertEqual(mock_random([13, 1], draw_starting_hand, "DEALER"), 21)
      self.assertEqual(mock_random([12, 5], draw_starting_hand, "DEALER"), 15)
      self.assertEqual(mock_random([3, 4], draw_starting_hand, "USER"), 7)
      self.assertEqual(mock_random([9, 10], draw_starting_hand, "USER"), 19)
      self.assertEqual(mock_random([13, 11], draw_starting_hand, "USER"), 20)
      self.assertEqual(mock_random([12, 11], draw_starting_hand, "USER"), 20)
      self.assertEqual(mock_random([13, 1], draw_starting_hand, "USER"), 21)
      self.assertEqual(mock_random([12, 5], draw_starting_hand, "USER"), 15)

if __name__ == '__main__':
    unittest.main()
