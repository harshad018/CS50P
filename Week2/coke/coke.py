def main():
   
    insert_coin()
    



def insert_coin():
    amount = 0
    while( amount < 50):
        
        print("Amount Due:",50 - amount)
        insert = int(input("Insert coin: "))
        if insert == 25 or insert == 10 or insert == 5:
            amount= amount + insert
        else:
            amount = amount + 0
    if insert == 25 or insert == 10 or insert == 5:
        if amount >= 50:
            print("Change Owed:",amount - 50)


main()