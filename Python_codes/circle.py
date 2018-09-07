class circle():

    #Attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = self.radius * self.radius * circle.pi

    def get_circumferance(self):
        return 2 * self.pi * self.radius



my_circle = circle()
print(my_circle.get_circumferance())
print(my_circle.area)
