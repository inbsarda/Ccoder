class Book():

    def __init__(self, name, auther, pages):
        self.name = name
        self.auther = auther
        self.pages = pages


    def __str__(self):
        return self.name+' by '+self.auther

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book has been deleted")
        



my_book = Book('Python rocks','Bhagyashri',30)
print(my_book)
print(len(my_book))
del my_book

