#Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#               They are automatically called by many of Python's built-in operations
#               They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self,other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in book1.title

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key =="num_pages":
            return self.num_pages
        else:
            return f"{key} was not found"



book1 = Book("The Hobbit", "J.R.R", 310) # when we call the class of Book and pass argument we will call the dunder
# init method its a magic method its automatically called behind the scenes
# within this magic method we can define and customize the behavior of objects
book2 = Book("Harry Potter", "J.K.Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S.Lewis", 178)
book4 = Book("Harry Potter", "J.K.Rowling", 923)

print(book1) #gives memory address without __str__
#  but now it prints 'The Hobbit' by J.R.R with __str__


print(book2 == book4) #returns false without #with __eq__ returns True

print(book3 < book4)

print(book3 > book4)

print(book3 + book4)

print("Lion" in book1)
print("Harry" in book1)

print(book3['author']) #C.S.Lewis
print(book2['audio']) #audio was not found

# Decorators
