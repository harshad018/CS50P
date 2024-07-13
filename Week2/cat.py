#print using for loop
for _ in range(3):
	print("meow")

#print using printing without loop
print("meow \n" * 3, end = "" )


while True:
	n = int(input("What's n? "))
	if n > 0:
		break


for _ in range(n):
	print("meow")