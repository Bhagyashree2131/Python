def samelastdigit(num1,num2):
    x=num1%10
    y=num2%10
    return x==y
    #     return True
    # else:
    #     return False
print(samelastdigit(123,123))
print(samelastdigit(123,124))