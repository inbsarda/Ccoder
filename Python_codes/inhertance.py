class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    #function overwriting
    def who_am_i(self):
        print("I am a dog")
        



new_animal = Dog()
new_animal.who_am_i()
