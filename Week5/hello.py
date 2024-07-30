def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="World"):
    #print("hello", to)
    return f"hello, {to}"


if __name__ == "__main__":
    main()