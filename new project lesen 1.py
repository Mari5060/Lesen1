import json

with open("bd.json", 'r', encoding = 'utf-8') as f:
    data = json.load(f)

lich = 0
for element in data:
    if element['імя'] == 'Маргарита':
        lich += 1

print(lich)
#'''''''''
