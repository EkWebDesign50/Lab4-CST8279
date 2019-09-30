#Task 1 
#8
def FtoC(temp):
    """ This function takes the temperature in Farenheit and converts it into celsius. """
    temp = temp-32
    temp = temp*5/9
    return temp

#10
def mpg(miles,gallons):
    """ This function calculates takes distance traveled in miles and the amount of fuel used in 
    gallons and returns the milelage in miles per gallon. """
    return(miles/gallons)

#12
from math import pi, sqrt
def areaofcircle(r):
    """ This function takes a value for the radius of a circle and returns the area. """ 
    return(pi*r*r)

#Task 2
def DistanceBetweenPoints(x,y,x1,y1):
    """ This function calculates the distance between two points 
    with coordinates and returns the distance between the two points. """
    dx = x-x1 
    dy = y-y1
    dist = sqrt(dx**2 + dy**2) 
    return(dist)

print(mpg(1,1222))
print(areaofcircle(1))
print(FtoC(72))
print("distance: ", DistanceBetweenPoints(5,2,12,25))

    

