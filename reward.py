def lotery(num):
    if num%4==0 and num%7==0:
        return 20
    elif num%7==0:
        return 10
    elif num%4==0:
        return 6
    else:
        return 0
print(lotery(8))
print(lotery(14))
print(lotery(28))
print(lotery(9))
