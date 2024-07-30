from hello import hello


def test_default():
    
    assert hello() == "hello, World"

def test_arguments():
    for name in ["Hermione", "Ron", "Harry"]:

        assert hello(name) == f"hello, {name}"