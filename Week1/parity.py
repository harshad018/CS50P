def main():
    num = int(input("What's number: "))
    if isEven(num):
        print("Even")
    else:
        print("Odd")

def isEven(num):
   return num %2 == 0
    
main()