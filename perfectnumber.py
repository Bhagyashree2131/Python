def perfectnum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    return sum==num
    #     return sum,"is a perfect number"
    # else:
    #     return "not a perfect number"
print(perfectnum(5))
print(perfectnum(26))
print(perfectnum(28))
print(perfectnum(6))