def month(month,year):
    if month==2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    if month==1 or month==3 or month==5 or month==7 or month==9 or month==11:
        return 31
    else:
        return 30
                    
print(month(2,2020))
print(month(1,2024))  
print(month(3,2023))      
print(month(4,2023))  
print(month(6,2021))  
print(month(8,2023))  
print(month(2,2021))  