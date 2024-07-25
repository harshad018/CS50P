def main():
    get_int("What's x? ")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            
        except ValueError:
            pass
       
    


main()