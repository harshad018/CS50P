def main():
    
    userinput()
    

counters = []

Items =  {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }



def userinput():
    while True:
        try:
            userinput = input("Item: ")
            
            counter(userinput)
        except EOFError:
            break


def counter(userinput):
    sum = 0
    for Item in Items:
        if Item.lower() == userinput.lower():
            
            counters.append(Items[Item])
            for i in counters:
                sum = sum + i
            print("Total: $", f"{sum:.2f}", sep="")
        else:
            continue
            

    



main()