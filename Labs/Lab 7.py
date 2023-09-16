#1. Функція яка виводить ряд Фібоначчі використовуючи рекурсію

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


n = 10
fibo = fibonacci(n)
print(fibo)


# 2.  Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
# Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.

def sum_range(start, end):
    if start > end:
        start, end = end, start

    total = 0
    for num in range(start, end + 1):
        total += num

    return total

result = sum_range(10, 100)
print(result)

result = sum_range(10, 5)
print(result)


# 3. Написати функцію season, що приймає 1 аргумент - номер місяця
# (від 1 до 12), і повертає пору року, якому цей місяць належить (зима, весна, літо чи осінь).

def season(month_number):
    if month_number in [12, 1, 2]:
        return 'зима'
    elif month_number in [3, 4, 5]:
        return 'весна'
    elif month_number in [6, 7, 8]:
        return 'літо'
    elif month_number in [9, 10, 11]:
        return 'осінь'
    else:
        return 'Неправильний номер місяця'


month = 1
result = season(month)
print(result)

month = 10
result = season(month)
print(result)

month = 15
result = season(month)
print(result)


# 4. Написати функцію get_filtered(), що приймає 1 аргумент - список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
# і виводить на консоль всі елементи які менші 5.

def get_filtered(a):
    filtered_list = [num for num in a if num < 5]
    for num in filtered_list:
        print(num)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
get_filtered(a)