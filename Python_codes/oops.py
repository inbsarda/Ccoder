class Dog():

    #Class object attribute
    #same for any instance of a class
    spacies = 'mammel'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    #Operations/actions ---methodes
    def bark(self, number):
        print('WOOF my name is {} and the number is {}'.format(self.name, number))



my_dog = Dog(breed = 'lab', name = 'sammy')
print(my_dog.breed +' '+ my_dog.name)
print(my_dog.spacies)
my_dog.bark(5)

