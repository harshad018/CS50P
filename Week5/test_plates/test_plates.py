from plates import is_valid


def test_criteria1():
  assert is_valid("CS50") == True

  assert is_valid("C50XX") == False


def test_criteria2():
  assert is_valid("c") == False
  assert is_valid("CS50088") == False
  assert is_valid("CS5008") == True


def test_criteria3():
  assert is_valid("AAA222") == True
  assert is_valid("AAA22A") == False


def test_criteria4():
  assert is_valid("CS50 P") == False
  assert is_valid("CS50.P") == False
  assert is_valid("CS!50") == False
