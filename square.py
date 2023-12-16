import math
def square(x1,y1,x2,y2):
    diagonal=math.sqrt((x2-x1)**2+(y2-y1)**2)
    #area=0.5*diagonal**2
    return 0.5*diagonal**2
    #return area
print(square(12,12,23,23))