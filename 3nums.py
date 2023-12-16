def add(num1,num2,num3):
    if num1+num2==num3 or num1+num3==num2 or num2+num3==num1:
        return True
    else:
        return False
print(add(1,2,3))
print(add(2,1,3))
print(add(4,2,2))
print(add(5,2,1))