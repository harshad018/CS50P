def main():
    twttr(user_input())

def user_input():
    word = input("Input: ")
    return word

def twttr(user_input):
    new_word = ""
    for j in user_input:
        
        if j.lower()== "a" or j.lower() =="e" or j.lower()=="i" or j.lower() =="o" or j.lower() == "u":
            new_word = new_word
        else:
            new_word = new_word + j
    print("Output:",new_word)


main()