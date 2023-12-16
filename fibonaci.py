def fibinaci(num):
    fibo=[0,1]
    a=0
    b=1
    #print(a,"\n",b)
    for i in range (10):
        c=a+b
        fibo.append(c)
        a=b
        b=c
    return fibo
print(fibinaci(10))