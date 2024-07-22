months =  [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# inputuser = "8/9/1636"

# month,date,year = inputuser.split("/")

# print(month,date,year)

# month = "8/9/2003"

# month,day,year = month.split("/")
while True:
    userinput = input("Enter the date: ")

    if userinput.find("/") == -1:
        month, day, year = userinput.split()
            
        
    else:
        month,day,year = userinput.split("/")
        
    
    if (month in months or int(month) in range(1,len(months))) and day in range(0,31):

        
        if day.isalpha():
            continue
        else:
            if month.isdigit():
                print(year,"-",0,month,"-",0,day,sep="")
                break
            else:
                day,comma = day.split(",")
                print(year,"-",0,months.index(month)+1,"-",0,day,sep="")
                break
    else:
        print("fuck")
        continue
# m = "January"



# print(month)

# if m in months:
#     print("present")
# else:
#     print("absent")
