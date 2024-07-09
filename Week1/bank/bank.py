#take the user input

user = input("Greeting: ")


#format the user input

user = user.strip().lower()


#check the conditions

if user.find("hello") == 0:
    print("$0")
elif user.startswith("h") :
    print("$20")
else:
    print("$100")