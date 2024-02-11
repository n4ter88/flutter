
class Pet:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def show(self):
         print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
        def speak(self):
            print("Meow")

class Dog(Pet):
        def speak(self):
            print("Bark")

p = Pet("Tim", 19)
p.show()
c = Cat("Billy", 34)
c.speak()
c.show()
d = Dog("Biatch", 25)
d.speak()
d.show()