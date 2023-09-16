# 1. Створити простий, пустий клас без реалізації - PlaceHolder
class Empty:
    pass


x = Empty()

# 2. Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр

class Human:
    def __init__(self, name):
        self.name = name

    def print_name(self):
     print(self.name)

p1 = Human("Iryna")
p1.print_name()

# 3.Додати до класу з пункту 2 змінну класу та статичний метод.

class Human:
    def __init__(self, name,age): #тут друга змінна класу `age`
        self.name = name
        self.age = age

    def print_name(self):
     print(self.name)

    def print_age(self):
     print(self.age)

    @staticmethod
    def Live():
        print("Person is living.")

Human.Live()

# 4. Створити клас який успадковується від класу з пункта 2.
# Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.


class Employee(Human):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def print_employee_id(self):
        print("Employee ID:", self.employee_id)


employee = Employee('John', 30, 'E1234')
employee.print_name()
employee.print_age()
employee.print_employee_id()