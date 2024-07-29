names = []
names2 = []
while True:
    try:
        userinput = input("Input: ")

        names.append(userinput)

        
    except:
        print()
        break


for name in range(len(names)-1):
    names2.append(names[name])



if len(names2) == 0:
    print("Adieu, adieu, to ", ", ".join(names))
else:
    print("Adieu, adieu, to ", ", ".join(names2) , "and", names[len(names)-1])
