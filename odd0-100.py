def my_function(num):
    odd=[]
    for i in range(num):
        if i%2==1:
            odd.append(i)
    return odd
            
print(my_function(100))