import random


def main():
    generate_integer(get_level())


def get_level():
    while True:
        level = input("Level: ")

        if int(level) == 1 or int(level) ==2 or int(level) == 3:
            return level
            
        else:
            continue


def generate_integer(level):
    problems = 0

    while problems < 10:
        if int(level) == 1:
            x = random.randint(1,9)
            y = random.randint(1,9)
            
        elif int(level) == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)

        elif int(level) == 3:
            x = random.randint(100,999)
            y = random.randint(100,900)

        attempt = 0
        while attempt < 3:
            
            u_ans = input(f"{x} + {y} = ")
            try:
                if x + y == int(u_ans):
                    break
                    
                else:
                    print("EEE")
                    
                    attempt = attempt + 1
            except ValueError:
                print("EEE")
                attempt = attempt + 1
        if attempt == 3:
            print(f"{x} + {y} = {x+y}")

        problems = problems + 1




if __name__ == "__main__":
    main()
