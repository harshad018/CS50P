#take the user input
user = input("File Name: ")


#format the user input
user = user.lower().strip()


#check the conditions

if user.endswith(".gif"):
    print("image/gif")

elif user.endswith(".jpeg") or user.endswith(".jpg"):
    print("image/jpeg")
elif user.endswith(".png"):
    print("image/png")
elif user.endswith(".pdf"):
    print("application/pdf")
elif user.endswith(".txt"):
    print("text/plain")
elif user.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")

