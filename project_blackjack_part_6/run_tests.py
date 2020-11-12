import subprocess

def tests_pass():
  try:
    subprocess.check_output('python blackjack_final_tests.py', shell=True)
    return True
  except:
    return False

print("All tests pass" if tests_pass() else "Not all tests pass")
