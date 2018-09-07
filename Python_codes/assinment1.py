from math import sqrt


class Line():

    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def slope(self):
        #calculate slope
        return (self.cord2[1] - self.cord1[1]) / (self.cord2[0] - self.cord1[0])

    def distence(self):
        #calculate distence
        return sqrt(((self.cord1[0] - self.cord2[0])**2) + ((self.cord2[1] - self.cord1[1])**2))


#Create instance of a class
my_cord = Line((1,1), (3,3))
print(my_cord.slope())
print(my_cord.distence())
