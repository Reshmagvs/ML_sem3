class Animal:
 def __init__(self, name):
  self.name = name
 def speak(self):
  raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
def speak(self):
return f"{self.name} says Woof!"
class Cat(Animal):
def speak(self):
return f"{self.name} says Meow!"
Using Inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak()) 


class Animal:
def __init__(self, name):
self.name = name
def speak(self):
return "Some generic sound"
class Dog(Animal):
def speak(self):
return f"{self.name} says Woof!"
dog = Dog("Buddy")
print(dog.speak()) 


class Animal:
def __init__(self, name):
self.name = name
def speak(self):
return "Some generic sound"
class Dog(Animal):
def __init__(self, name, breed):
super().__init__(name)
self.breed = breed
def speak(self):
return f"{self.name} the {self.breed} says Woof!"
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())
