class Cone:
    def __init__(self,radius=20, height=30):
        if radius >0 and height>0:
            self.__r = radius
            self.__h = height
    def get_vol(self):
        return 1/3 * 3.14 * (self.__r**2) * self.__h
    def get_surf(self):
        return 3.14 * (self.__r ** 2) + 3.14 * self.__r * self.__h
    def get_radius(self):
        return self.__r
    def set_radius(self, radius):
        if radius >0 :
            self.__r = radius


class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
    def get_BMI(self):
        BMI = self.__weight / ((self.__height/100) ** 2)
        return BMI
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age>0:
            self.__age = age
    def get_status(self):
        BMI = self.get_BMI()
        if BMI > 25:
            return '비만'
        elif BMI > 23:
            return '과제중'
        elif BMI > 20:
            return '정상'
        else:
            return "저체중"


cone1 = Cone()
cone2 = Cone(50,60)
print(cone2.get_radius())

print(cone1.get_surf())
print(cone2.get_vol())




person1 = BMI('변기원',34,89,183)
print(person1.get_age())
person1.set_age(30)
print(person1.get_age())
# print(person1.name+'은',person1.get_status())


