#Ask user for their name
name = input("What's your name? ")
"""

I think this is also a comment.

"""

#Say hello to user
print("Hello,",end=" ")
print(name)




print("Good Morning",name)
#the f here indicates that the string inside print should be handled specially,
#since we are using {} for variable printing inside string.
print( f"What do you have on your mind {name} ?")



#what we have to do in the case user don't cooperate for the input 
#e.g user enter multiple spaces when asked for input.

#remove whitespace from str
name = name.strip()


#capitalize user's name
name = name.capitalize()

#title based capitalization
name = name.title()


#two functions together
name = name.strip().capitalize()


#also we can to following
name = input('What is your name?').capitalize().strip()

print(f"name without whitespaces is {name}")


#Split user's name into first name and last name

first, last = name.split()


#say hello to user
print(f"hello {first}")