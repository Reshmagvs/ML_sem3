try:
 result = 10 / 0
 my_list = [1, 2, 3]
 print(my_list[10])
 except ZeroDivisionError:
 print("You can't divide by zero!")
  except IndexError:
 print("Index out of range!")

try:
 result = 10 / 2
 except ZeroDivisionError:
 print("You can't divide by zero!")
 else:
   print("No exceptions were raised!")
 finally:
   print("This block always executes!")

