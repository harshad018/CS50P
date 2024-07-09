def main():
    #take the input
    
    convert(userinput())


def userinput():
    userin = input()
    return userin

def convert(userinput):
    userinput = userinput.replace(":)", "🙂")
    userinput = userinput.replace(":(", "🙁")

    print(userinput)

main()