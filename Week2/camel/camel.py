def main():
    snake_case(user_input())

def user_input():
    name = input("camelCase: ")
    return name

def snake_case(name):
    word = ""
    for i in name:
    
        if 65 <= ord(i) <= 90:
            i = i.lower()
            word = word + "_"
            word = word + i
        else:
            word = word + i
    print(word)




    
    

main()