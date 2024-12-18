import math

class Point:
    def __init__(self,x,y):
        ''' Initialize the point instance'''
        #your code goes here
    def get_x(self):
        ''''Getter for the x coordinate'''
        #your code goes here
    def get_y(self):
        '''Getter for the y coordinate'''
        #your code goes here
    def set_x(self,x):
        '''Setter for the x coordinate'''
        #your code goes here
    def set_y(self,y):
        '''Setter for the y coordinate'''
        #your code goes here
    def distance(self,other):
        '''Calculate the distance between two points'''
        #your code goes here
    def __eq__(self,other):
        '''Two points are equal if they have the same x and y coordinates'''
        #your code goes here
    def __str__(self):
        ''''Returns a string representation of the point as (x,y)'''
        #your code goes here

class Circle: 
    def __init__(self,center,radius):
        ''' Initialize the circle instance raise a ValueError exception
        if the radius is not a positive number or center is not a point object'''
        #your code goes here
    def get_center(self):
        '''Getter for the center of the circle'''
        #your code goes here
    def get_radius(self):
        '''Getter for the radius of the circle'''
        #your code goes here
    def set_center(self,center):
        '''Setter for the center of the circle'''
        #your code goes here
    def set_radius(self,radius):
        '''Setter for the radius of the circle'''
        #your code goes here
    def area(self):
        '''Calculate the area of the circle'''
        #your code goes here
    def __str__(self):
        '''Returns a string representation of the circle as Center:(x,y), Radius: r'''
        #your code goes here  
    def is_in(self,point):
        '''Check if a point is inside the circle'''
        #your code goes here
    def __eq__(self,other):
        '''Two circles are equal if they have exactly the same center and the same radius''' 
        #your code goes here


origin=Point(0,0)
p1=Point(3,4)
p2=Point(2,3)
c1=Circle(origin,4)
c2=Circle(p1,3)
print(c1)
print(p1)
print(c1.area())
print(c1.is_in(p1))
print(c2.is_in(p2))

