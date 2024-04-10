import math

class Cone:
    def __init__(self,radius=20, height=30):
        if radius >0 and height>0:
            self.__r = radius
            self.__h = height
    def get_vol(self):
        return 1/3 * math.pi * (self.__r**2) * self.__h
    def get_surf(self):
        return math.pi * (self.__r ** 2) + math.pi * self.__r * self.__h
    def get_radius(self):
        return self.__r
    def set_radius(self, radius):
        if radius >0 :
            self.__r = radius

class Triangle:
    def __init__(self, width1, width2, angle):
        if(width1 >0 and width2 >0 and angle>0):
            self.__width1 = width1
            self.__width2 = width2
            self.__angle = math.radians(angle)
    def get_vol(self):
        return 1/2 * self.__width1 * self.__width2 * math.sin(self.__angle)


testTri = Triangle(10,20,60)
print(testTri.get_vol())