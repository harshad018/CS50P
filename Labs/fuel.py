def main():
    
    result(percent(take_input()))
    




def take_input():
    
    while True:
        try:
            
            
            

            userinput = input("Fraction: ")
            first,middle,last = userinput.strip()
            try:
                
                
                    output = float(int(first)/int(last))
                    if output <= 1.0:
                        return output
                    
                
            except ZeroDivisionError:
                pass
        except ValueError:
            pass
        
    

def percent(output):
    try:
        final  = float(output * 100)
        return final
    except TypeError:
        pass


def result(final):
    try:
        if final <= 1:
            print("E")
        elif final == 100:
            print("F")
        else:
            print(str(int(final))+"%")
    except TypeError:
        pass


main()
