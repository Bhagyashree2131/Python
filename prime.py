def prime(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
    
print(prime(2))
print(prime(3))
print(prime(4))
print(prime(17))