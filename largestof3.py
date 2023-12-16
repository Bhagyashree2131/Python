def largest(num1,num2,num3):
    if num1 >num2 and num1 > num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(largest(9,8,7))
print(largest(7,10,6))
print(largest(9,8,11))