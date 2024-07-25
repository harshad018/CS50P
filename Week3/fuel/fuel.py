import math

def main():
    
    result(percent(take_input()))
    




def take_input():
    
    while True:
        try:
            
            
            

            userinput = input("Fraction: ")
            first,last = userinput.split("/")
            try:
                
                
                    output = float(int(first)/int(last))
                    
                    if 0.0 <= output <= 1.0:
                        return output
                    
                
            except ZeroDivisionError:
                pass
        except ValueError:
            pass
        
    

def percent(output):
    try:
        final  = float(output * 100)
        final = round(final)
        return final
    except TypeError:
        pass


def result(final):
    try:
        if 0 <= final <= 1:
            print("E")
        elif final == 100 or final == 99:
            print("F")
        else:
            print(str(int(final))+"%")
    except TypeError:
        pass


main()
