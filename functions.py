def say_hello():
 print("Hello, World!")

say_hello()

def add(a, b):
 return a + b
result = add(3, 4)
print(result) 

def greet(name="Guest"):
 print(f"Hello, {name}!")
greet("Alice") 
greet() 

def describe_pet(pet_name, animal_type="dog"):
 print(f"I have a {animal_type} named {pet_name}.")
describe_pet(animal_type="hamster", pet_name="Harry")
