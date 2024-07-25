def main():
    
    userinput()
    

grocery_list = []

def count(item):
  repeat = []
  for i in grocery_list:
    if i == item:
      repeat.append(i)
      

  return  len(repeat)

def userinput():
    userinput = ""
    while True:
        try:
            userinput = input()
            grocery_list.append(userinput.upper())
            
        except EOFError:
            break
    counter(userinput)

def counter(userinput):
    
    unique_grocery_list = sorted(list(set(grocery_list)))
    for grocery in unique_grocery_list:
        
        print(count(grocery),grocery)
        
            

    



main()