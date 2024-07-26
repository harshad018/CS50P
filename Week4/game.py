import random
import sys

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue

    if level > 0:
        user_int = random.randint(1,level)
        while True:
            try:
                guess = int(input("Guess: "))
                
            except ValueError:
                continue
            if guess > 0:
                if user_int > guess:
                    print("Too large")

                elif user_int < guess:
                    print("Too small")

                elif user_int == guess:
                    print("Just Right!")
                    sys.exit()
            else:
                continue


    else:
        continue
