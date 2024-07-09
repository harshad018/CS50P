#take the expression from user
exp = input("Expression: ")

#extract x,y and z from the expression
x,y,z = exp.split()
x = float(x)
y = str(y)
z= float(z)

#match
match y:
    case "+":
        print(round(x+z,1))
    case "-":
        print(round(x-z,1))
    case "*":
        print(round(x*z,1))
    case "/":
        if z == 0:
            print("y can't be zero")
        else:
            print(round(x/z,1))
    case _:
        print("Invalid expression")