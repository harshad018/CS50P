

def main():
    name = input("Enter you name: ")
    hello(name)
    hello()


def hello(to = "World!"):
    print(f"Hello {to}")



main()