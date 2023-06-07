                                          #Рядки:
# a.Навести приклад простого рядка
a = "Simple string"

print('a. Звичайний рядок:', a)


# b. Навести приклад багаторядкового рядка (Вірш, хоку - щоб показати форматування)
multiline_string = '''
Ах, не топчи траву !
Там світлячки сяяли
Вчора нічний часом'''

print('b. Приклад багаторядкового рядка:', multiline_string)


# c. Навести приклад рядка з ігноруванням екрануючих символів (Raw)

txt = 'Цілий день мучуся з цими лабками \"Десять заплаканих жабеняток Пепе із десяти\".'
print('c. Приклад рядка з ігноруванням екрануючих символів', txt)


# d. Навести приклад форматування довгих рядків

multiline_string2 = 'In python there is also the shorthand ternary\n  tag which is a shorter version of the normal ternary\n operator you have seen above'


print('d. Приклад форматування довгих рядків:', multiline_string2)

                                     #Списки:

import copy

# Створити простий список
first_list = ['apple', 'banana', 'cherry', 'pear']

# Створити змінну з посиланням на перший список
reference_list = first_list

# Створити поверхову (Shallow copy) копію першого списка
shallow_copy = first_list.copy()

# Створити глибоку (повну) (Deep copy) першого списка
deep_copy = copy.deepcopy(first_list)

# Вивести значення всіх списків
print("Original List:", first_list)
print("Reference List:", reference_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

# Змінити перший список і ще раз вивести значення всіх списків
first_list.append('truskavka')

print("\nAfter modifying the Original List:")
print("Original List:", first_list)
print("Reference List:", reference_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)



                            # Словники:
#Створити пустий словник одним з наведених в лекції способів
empty_dictionary = {}



#Створити новий словник з 2-3 парами ключ:значення
new_dictionary = {
    'cat' : 'Murka',
    'dog' : 'Tuzik',
    'destination' : 'My heart =)'
}

print(new_dictionary)

#Додати одну пару ключ:значення до першого словника
empty_dictionary ['hamster'] = 'bulka'

#Додати до першого словника другий словник використовуючи .update()
empty_dictionary.update(new_dictionary)

#видалити один елемент словника за допомогою .pop()
empty_dictionary.pop('hamster')

#Видалити один елемент за допомогою .popitem()
empty_dictionary.popitem()

#Зробити глибоку копію першого словника в нову змінну
new_dictionary = empty_dictionary.copy()

#Додати до нового словника новий ключ, а як значення передати перший словник
new_dictionary['pig'] = empty_dictionary

#Вивести список ключів
print("List of Keys:", new_dictionary.keys)

list_of_keys = new_dictionary.keys()
print(list_of_keys)

#Вивести список значень
list_of_values = new_dictionary.values()
print(list_of_values)

                     #4. Тернарний if - 2 приклади.

bad = True
hw_result = ('good', 'bad')[bad]
print('HW result is', hw_result)


x = 4
ternary_var = True if x + 5 == 10 else False

print('The value {} is even:{}'.format(x, ternary_var))

#5 Вкладені структури:

# 1. Створити 3 вимірний список (список 3х списків)
three_dim_list = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# 2. Змінити, будь який, елемент, будь якого, спику.
three_dim_list[1][2] = 990

# 3. Вивести значення до та після
print('Значення до модифікації:')
print(three_dim_list)

print('\nЗначення після модифікаці:')
print(three_dim_list)

# 4. Створити список зі вкладеним словником
attached_dict = [
    {"тварина": "котичка", "кількість": 3},
    {"тварина": "собаня", "кількість": 1}
]

# 5. Створити словник зі вкладеним списком
nested_dict = {
    "numbers": [23, 42, 35, 46],
    "animals": ["lama", "cow", "chicken"]
}

# 6. Зберегти вкладений список зі словника у нову змінну
new_list = nested_dict["numbers"]

# Вивести новий список
print("\nNew List from Dictionary:")
print(new_list)

                   #6. Побітові операції:
#a. побітове AND:
#Порівняти два різних цілих і два однакових числа і вивести результат

num1 = 10   # binary: 1010
num2 = 6    # binary: 0110

result1 = num1 & num2
print(f"The bitwise AND of {num1} and {num2} is {result1}")  # Output: The bitwise AND of 10 and 6 is 2


# Two identical numbers
num3 = 15   # binary: 1111
num4 = 15   # binary: 1111

result2 = num3 & num4
print(f"The bitwise AND of {num3} and {num4} is {result2}")  # Output: The bitwise AND of 15 and 15 is 15

#Порівняти два різних рядка і два однакових рядка і вивести результат
# Two different strings
str1 = 'Майте Бога в серці'
str2 = 'Ця домашка витянула всі соки'

if str1 == str2:
    print('The strings are equal')
else:
    print('The strings are not equal')

# Two identical strings
str3 = 'Дай Боже сил'
str4 = 'Дай Боже сил'

if str3 == str4:
    print('The strings are equal')
else:
    print('The strings are not equal')