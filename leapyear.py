def is_leap(year):

    
    if year%4==0 :
        
        if year%100==0 and year%400 == 0:
            return ("True")
        elif year%100 == 0 and year%400 != 0:
            return ("False")
        else : return("True")
        
    elif year%4!=0 :
            return ("False")

year = int(input())
print(is_leap(year))