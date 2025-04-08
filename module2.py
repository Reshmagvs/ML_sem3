import modules
print(modules.greet("Alice"))
print(modules.add(2, 3)) 

from modules import greet, add
print(greet("Bob")) 
print(add(5, 7))
