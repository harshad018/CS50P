#prompt user for input

user = input(("What is the answer to the great question of life, the universe, and everything? ").title())


#format user input

user = user.strip().lower()


#check if the user input is correct




if user == "forty two" or user == "forty-two" or user == "42":
    print("Yes")
else:
    print("No")