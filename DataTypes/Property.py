# property --> Decorator used to define a method as a property (it can be accessed like an attribute)
#               Benefit: Add additional logic when read, write, or delete attributes
#               Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, widt, height):
        self._width = widt
        self._height = height

    #     getter --> provides controlled access to the data/attributes in class
    @property
    def width(self):
        return f"{self._width: .1f}cm"

    @property
    def height(self):
        return f"{self._height: .1f}cm"

    # setter
    @width.setter
    def width(self, new_width):
        if new_width>0:
            self._width = new_width
        else:
            print("width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height>0:
            self._height = new_height
        else:
            print("height must be greater than 0")#doesn't print

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")
rectangle = Rectangle(100, 200)

rectangle.width = 5
rectangle.height = -1#doesn't print height must be greater than 0 instead prints 200

del rectangle.height
print(rectangle.width)#technically we can
# print(rectangle.height)
