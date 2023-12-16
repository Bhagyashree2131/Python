def my_function(num):
    div=[]
    for num1 in range(1,num):
        if num1%3==0 or num1%7==0:
            div.append(num1)
    return div
print(my_function(10))
    
def my_function1(num):
    if num%3==0 or num%7==0:
      return True
  
print(my_function1(6))  
    