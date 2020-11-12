import io
import unittest
from unittest.mock import patch
import sys

def __run_function(func, func_input=None, func_input_more=None):
  """
  Runs given function with given inputs

  Args:
    func - function to run
    func_input - optional function input if provided function requires input
  """
  if func_input_more:
    return func(func_input, func_input_more)
  return func(func_input) if func_input else func()

def get_print(func, func_input=None, func_input_more=None):
  """
  Saves printed statements and returns

  Args:
    func - function to run
    func_input - optional function input if provided function requires input
  """
  old_stdout = sys.stdout
  new_stdout = io.StringIO()
  sys.stdout = new_stdout
  __run_function(func, func_input, func_input_more)
  output = new_stdout.getvalue()
  sys.stdout = old_stdout
  return(output)

def mock_random(mocked_ints, func, func_input=None):
  """
  Runs given function with mocked out random numbers

  Args:
    func - function to run
    func_input - optional function input if provided function requires input
  """
  with patch("random.randint") as randint_mock:
    randint_mock.side_effect = mocked_ints
    return __run_function(func, func_input)