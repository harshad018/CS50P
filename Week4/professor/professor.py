import random


def main():
    generate_integer(get_level())


def get_level():
    while True:
        level = input("Level: ")

        if int(level) == 1 :
            return level
            
        else:
            continue


def generate_integer(level):
    problems = 0

    while problems < 10:
        if int(level) == 1:
            x = random.randint(1,9)
            y = random.randint(1,9)
            attempt = 0

            while attempt < 3:
                try:
                    u_ans = input(f"{x} + {y} = ")
                except ValueError:
                    continue

                if x + y == int(u_ans):
                    break
                    
                else:
                    print("EEE")
                    
                    attempt = attempt + 1
        if attempt == 3:
            print(f"{x} + {y} = {x+y}")

        problems = problems + 1




if __name__ == "__main__":
    main()
