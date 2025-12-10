

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


# Creating an instance of the Point class
point = Point(10, 20)
print(point.x)  # Accessing the 'x' attribute of the point object
print(point.y)
point.move()
point.draw()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('talk')


# Creating an instance of the Person class
john = Person("John Smith")
print(john.name)  # Accessing the 'name' attribute of the person object
john.talk()  # Calling the talk method
