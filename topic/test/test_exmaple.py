# https://www.tutorialspoint.com/pytest/pytest_file_execution.htm


def test_greater():  # failed
  num = 100
  assert num > 100


def test_greater_equal():
  num = 100
  assert num >= 100


def test_less():
  num = 100
  assert num < 200
