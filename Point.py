import math



class Point:
    def __init__(self,x,y,_x,_y):
        ''' Initialize the point instance'''
        #your code goes he
        self.x = x
        self.y =y
        self._x =_x
        self._y=_y
        
    def get_x(self):
        ''''Getter for the x coordinate'''
        #your code goes here
        return self.x

    def get_y(self):
        '''Getter for the y coordinate'''
        return self.y
        #your code goes here
    def set_x(self,x):
        '''Setter for the x coordinate'''
        #your code goes here
        self._x=x
    def set_y(self,y):
        self._y=y
        '''Setter for the y coordinate'''
        #your code goes here
    def distance(self,other):
        '''Calculate the distance between two points'''
        #your code goes here
        if not isinstance(other, Point):
          raise ValueError("The argument must be a Point instance")
        return math.sqrt((self._x - other.get_x())**2 + (self._y - other.get_y())**2)

    def __eq__(self,other):
        '''Two points are equal if they have the same x and y coordinates'''
        #your code goes here
        if not isinstance(other, Point):
            return False
        return self._x == other.get_x() and self._y == other.get_y()
    def __str__(self):
        ''''Returns a string representation of the point as (x,y)'''
        #your code goes here
        return f"({self._x}, {self._y})"

class Circle: 
    def __init__(self,center,radius):
        ''' Initialize the circle instance raise a ValueError exception
        if the radius is not a positive number or center is not a point object'''
        #your code goes here
        if not isinstance(center, Point):
            raise ValueError("Center must be a Point instance")
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self._center = center
        self._radius = radius
    def get_center(self):
        '''Getter for the center of the circle'''
        #your code goes here
        return self._center

    def get_radius(self):
        '''Getter for the radius of the circle'''
        #your code goes here
        return self._radius
    def set_center(self,center):
        '''Setter for the center of the circle'''
        #your code goes here
        if not isinstance(center, Point):
            raise ValueError("Center must be a Point instance")
        self._center = center
        
    def set_radius(self,radius):
       
         '''Setter for the radius of the circle'''
        #your code goes here
         if radius <= 0:
            raise ValueError("Radius must be a positive number")
         self._radius = radius
    def area(self):
        '''Calculate the area of the circle'''
        #your code goes here
        return math.pi * (self._radius**2)
    def __str__(self):
        '''Returns a string representation of the circle as Center:(x,y), Radius: r'''
        #your code goes here  
        return f"Center: {self._center}, Radius: {self._radius}"
    def is_in(self,point):
        '''Check if a point is inside the circle'''
        #your code goes here
        if not isinstance(point, Point):
            raise ValueError("Argument must be a Point instance")
        return self._center.distance(point) <= self._radius
    def __eq__(self,other):
        '''Two circles are equal if they have exactly the same center and the same radius''' 
        #your code goes here
        if not isinstance(other, Circle):
            return False
        return self._center == other.get_center() and self._radius == other.get_radius()


origin=Point(0,0,0,0)
p1=Point(3,4,3,4)
p2=Point(2,3,3,4)
c1=Circle(origin,4)
c2=Circle(p1,3)
print(c1)
print(p1)
print(c1.area())
print(c1.is_in(p1))
print(c2.is_in)

