#4=2*2 9=3*3
def perfectsq(num):
    for i in range (1,num):
        if i*i==num:
            return i
print(perfectsq(9))
print(perfectsq(25))
            
        