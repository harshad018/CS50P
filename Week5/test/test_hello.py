from hello import hello


def test_default():
    assert hello() == "hello, World"


def test_argument():
    assert hello("Harshad") == "hello, Harshad"