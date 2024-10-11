import math
from abc import ABC, abstractmethod

class Shape: 
    @abstractmethod
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    
    def area(self):
        return self.length * self.width
        
class Circle(Shape): 
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
         return math.pi * self.radius ** 2


#carton = Rectangle(3, 6)
#ball = Circle(7)

#print(f"Area of carton is {carton.area()} & area of ball is {ball.area()}")
