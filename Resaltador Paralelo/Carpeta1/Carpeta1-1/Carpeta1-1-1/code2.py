from abc import ABC, abstractmethod
from math import pi

class GeometricObject(ABC):
    def perimeter(self):
        pass
    def area(self):
        pass

class Circle(GeometricObject):
    def __init__(self,radius = 1.0):
        self._radius = radius
    
    def perimeter(self):
        return pi*2*self._radius
      
    def area(self):
        return pi*((self._radius)**2)
        
    def __str__(self):
        return f'Circle with radius = {self._radius}'
        
class Rectangle(GeometricObject):
    def __init__(self,width = 1.0,length = 1.0):
        self._width = width
        self._length = length
    
    def perimeter(self):
        return 2 * self._length + 2 * self._width
      
    def area(self):
        return self._width * self._length
    
    def __str__(self):
        return f'Rectangle with length = {self._length} and width = {self._width}'
    
class Resizable(ABC):
    def resize(percent):
        pass
      
class ResizableCircle(Circle,Resizable):
    def __init__(self,radius):
        Circle.__init__(self,radius)
    
    def resize(self,percent):
        self._radius = (percent / 100) * self._radius
    
class ResizableRectangle(Rectangle,Resizable):
    def __init__(self,width,length):
        Rectangle.__init__(self,width,length)
    
    def resize(self,percent):
        self._width = (percent / 100) * self._width
        self._length = (percent / 100) * self._length