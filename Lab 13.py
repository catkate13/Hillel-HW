#Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.
import csv

with open('Sample.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
#Використайте прикріплений файл json та прочитайте його за допомогою модулю json.

import json

with open('sample2.json', mode='r') as json_file:
    json_data = json.load(json_file)

for key, value in json_data.items():
        print(key, ":", value)

#Створити конструкції try-except для арифметичної операції, роботи з колекціями.

try:
    value1 = 1
    value2 = 0
    result = value1 / value2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Value devided by zero!")

    try:
        my_list = [1, 2, 3, 4, 5]
        print("Value at index 9:", my_list[7])
    except IndexError:
        print("Error: Value is out of range!")
