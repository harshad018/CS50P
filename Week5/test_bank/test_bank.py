from bank import value


def test_value_h():
  assert value("hii") == "$20"
  assert value("HII") == "$20"
  assert value("how are you?") == "$20"
  assert value("HOW ARE YOU?") == "$20"
  assert value("how's the josh?") == "$20"
  assert value("HOW'S THE JOSH?") == "$20"


def test_value_hello():
  assert value("hello") == "$0"
  assert value("HELLO") == "$0"


def test_value_general():
  assert value("good morning") == "$100"
  assert value("GOOD MORNING") == "$100"
  assert value("what's up?") == "$100"
  assert value("WHAT'S UP?") == "$100"
