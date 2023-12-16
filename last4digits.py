def digits(num):
    x=num%10000
    sum=0
    while(x!=0):
        sum=sum+(x%10)
        x //=10
    return sum
print(digits(12345))
print(digits(1234))
print(digits(54321))
