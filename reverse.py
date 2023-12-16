def reverse(num):
    reverse1=0
    while(num!=0):
        rem=num%10
        reverse1=reverse1*10+rem
        num //=10
    return reverse1
print(reverse(124))
print(reverse(1234))
print(reverse(54321))