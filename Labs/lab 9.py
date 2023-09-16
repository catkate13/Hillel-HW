                                       # Lambda

#Написати лямбда функцію яка приймає один або 2 аргументи (другому задати значення за замовчуванням рівне 100, як у  #звичайних функціях) та друкує символ переданий як перший аргумент ту кількість раз яка вказана в другому аргументі, зробити можливим роботу фнкції не тільки з рядком а й з цифрами.

print_value = lambda value, times=100: print(value * times)

print_value('мої вихідні  наступні 2 місяці =))), ', 5)
print_value('дохла русня ')


#Написати лямбда функцію яка приймає 2 числа як аргументи та повертає більше з них (використовуйте тернарний if)
bigger_number = lambda val1, val2: val1 if val1 > val2 else val2


result = bigger_number(10, 5)
print(result)


#Написати лямбда функція яка нічого не приймає та завжди повертає 10.
return_ten_fun = lambda: 10


result = return_ten_fun()
print(result)



                                   # Decorators

def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def make_italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

def make_underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"
    return wrapper

@make_bold
@make_italic
@make_underline
def civil_war():
    return "dead russians"

formatted_text = civil_war()
print(formatted_text)



                               # List comprehension

#Використовуйте list comprehension, щоб створити новий список, але додайте 6 до кожного елемента.
lst1 = [44, 54, 64, 74, 104]

lst2 = [num + 6 for num in lst1]
print(lst2)

#Використовуючи list comprehension, побудуйте список із квадратів кожного елемента в списку.
lst3 = [2, 4, 6, 8, 10, 12, 14]

lst4 = [num**2 for num in lst3]
print(lst4)

#Дано словник який складається з транспортних засобів та їх маси в кілограмах. Складіть список назв транспортних засобів вагою до 5000 кілограмів. У тому самому list comprehension зробіть імена ключів великими регістром.
car_dict = {
    "Sedan": 1500,
    "SUV": 2000,
    "Pickup": 2500,
    "Minivan": 1600,
    "Van": 2400,
    "Semi": 13600,
    "Bicycle": 7,
    "Motorcycle": 110
}

list5 = [key.capitalize() for key, value in car_dict.items() if value <= 5000]
print(list5)
