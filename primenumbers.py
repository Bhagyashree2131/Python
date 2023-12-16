def isPrime(num1,num2):
    prime=[]
    for i in range(num1,num2):
        for j in range(num1,i):
            if i%j==0:
                break
        else:
            prime.append(i)
    return prime
            
print(isPrime(2,101))