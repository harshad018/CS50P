from twttr import shorten


def test_shorten_lower():
    assert shorten("twitter") == "twttr"

    assert shorten("harshad") == "hrshd"

    assert shorten("shrikant") == "shrknt"


def test_shorten_capital():
    assert shorten("TWITTER") == "TWTTR"


def test_shorten_empty_input():
    assert shorten("") == ""
