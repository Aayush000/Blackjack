import re
from unittest import TestCase, main

below = "WRITE YOUR TESTS BELOW"
filename = 'deck_tests.py'

def function_count(func):
  count = 0

  with open(filename, 'r') as f:
    lines = f.readlines()
    student_code = False
    for line in lines:
      if student_code:
        if bool(re.search('assertEqual.*' + func, line)):
          count += 1
      elif below in line:
        student_code = True
  return count

class BlackjackPart5Test(TestCase):

    def setUp(self):
      self.function = input()
      self.required = input()

    def test_function_count(self):
        count = function_count(self.function)
        print("Function tested: {}".format(self.function))
        print("Required number of tests: {}".format(self.required))
        print("Found number of tests: {}".format(count if count else 0))
        print("OK" if count >= int(self.required) else "Not enough tests")

if __name__ == '__main__':
    main()
