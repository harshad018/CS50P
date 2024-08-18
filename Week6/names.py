# name = input("What's your name? ")



# with open("names.txt","a") as file:

#     file.write(f"{name}\n")

with open("names.txt", "r") as file:
#     lines = file.readlines()


# for line in lines:
#     # print(f"hello, {line}", end="")
#     print(f"hello, {line.rstrip()}")
#
     for line in file:
         print("hello, ", line.rstrip())
