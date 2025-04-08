import csv

data = [
    ["Actual", "Predicted"],
    [1, 1],
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [1, 1],
    [0, 0],
    [1, 1],
    [0, 0],
    [1, 0],
]

with open("newcsv.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully")
