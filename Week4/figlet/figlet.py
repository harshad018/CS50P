from pyfiglet import Figlet

import sys

if len(sys.argv) > 1:

    
    
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and Figlet(font=sys.argv[2]):
        
        try:
            f = Figlet(font=sys.argv[2])
            userinput = input("Input: ")
            print("Output: ",f.renderText(userinput),sep="\n")
        except:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid usage")        
    
elif len(sys.argv) == 1:
    userinput = input("Input: ")
    f = Figlet(font="slant")
    print("Output: ",f.renderText(userinput),sep="\n")

else:
    sys.exit()