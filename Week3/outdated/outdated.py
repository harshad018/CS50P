months = [
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

while True:
    
    
    userinput = input("Enter the Date: ")
    
    if '/' in userinput:
        try:
            
            
            month, day, year = userinput.split('/')
            
            
            month = int(month)
            day = int(day)
            year = int(year)
            
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
        
        
        except ValueError:
            pass
    else:
        
        
        
        
        try:
            
            
            month, day, year = userinput.split()
            month = month.capitalize()
            year = int(year) 
            
            
            if ',' in day:
                day = day.strip(',')
                try:
                    day = int(day)
                    if 1 <= day <= 31 and month in months:
                        
                        
                        
                        month_index = months.index(month) + 1
                       
                       
                        print(f"{year}-{month_index:02}-{day:02}")
                        break
                
                
                
                except ValueError:
                    pass
        
        
        
        
        except ValueError:
            pass
