class Dog():

    def __init__(self):
        print("Dog created")

    def speak(self):
        print("WOOF!")


class Cat():

    def __init__(self):
        print("Cat created")

    #polimorphism
    def speak(self):
        print("MEOW!")



my_cat = Cat()
my_cat.speak()
