day = int(input("Enter day : "))
month = int(input("Enter month : "))
year = int(input("Enter year : "))
if (year % 4 != 0) :  # not a leap year
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) :  # for december new condition
        if(day <= 30) :
            day = day + 1
        elif(day == 31) :
            month = month + 1
            day = 1
    elif(month == 4 or month == 6 or month == 9 or month == 11) :
        if(day <= 29) :
            day = day + 1
        elif(day == 30) :
            month = month + 1
            day = 1  
    elif(month == 2) :
        if(day <= 27) :
            day = day + 1
        elif(day == 28) :
            month = month + 1
            day = 1
    elif(month == 12) :
        if(day <= 30) :
            day = day + 1
        elif(day <= 31) :
            day = 1
            month = 1
            year = year + 1
else : # leap year
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) :  # for december new condition
        if(day <= 30) :
            day = day + 1
        elif(day == 31) :
            month = month + 1
            day = 1
    elif(month == 4 or month == 6 or month == 9 or month == 11) :
        if(day <= 29) :
            day = day + 1
        elif(day == 30) :
            month = month + 1
            day = 1  
    elif(month == 2) :
        if(day <= 28) :
            day = day + 1
        elif(day == 29) :
            month = month + 1
            day = 1
    elif(month == 12) :
        if(day <= 30) :
            day = day + 1
        elif(day <= 31) :
            day = 1
            month = 1
            year = year + 1
print("nexy date : ",day,"/",month,"/",year)