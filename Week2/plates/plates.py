def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = []
    
    for i in s:
        valid.append(i)

    criteria1 = False
    if 2 <= len(valid) <= 6:
        criteria2 = True
        if valid[0].isalpha() and valid[1].isalpha():
            criteria1 = True
        else:
            criteria1 = False
    else:
        criteria2 = False
    
    #criteria 3
    for i in valid:
        if i.isalpha():
            criteria3 = True
        elif i.isnumeric():
            criteria3 = True
        else:
            criteria3 = False
            break


    #criteria 4
    criteria4 = True
    no = 0
    for i in valid:
        if i.isdigit():
            no = i
            break

    if no != 0:
        test = s.rfind(no)
  
  
        new = []
        t = test
        while(t < len(s)):
            new.append(valid[t])
            t = t+1
  
  
        
        if int(new[0]) == 0:
            criteria4 = False
        else:
            for i in new:
                if i.isalpha():
                 criteria4 = False
  
  
    if ( criteria1 == True and criteria2 == True and criteria3 == True and criteria4 == True):
        return True
    else:
        return False
main()
