
with open("note.txt", "r") as file:
 content = file.read()
print(content)

with open("note.txt", "r") as file:
 for line in file:
  print(line.strip())

with open("note.txt", "w") as file:
 file.write("Hello, World!\n")
 file.write("This is a file handling example.")

with open("note.txt", "a") as file:
 file.write("\nAppending a new line.")

 file = open("note.txt", "r")

file.close()
