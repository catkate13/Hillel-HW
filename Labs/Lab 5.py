from typing import Set  # Tuple

 #1.Створити кортеж котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7
 #2. Вивести кортеж у консоль
thistuple = (1, 2, 3, 4, 5, 6, 7)
print( 'кортеж:', thistuple)

                                                    #Set

# Створити set котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7
set_one = {1, 2, 3, 4, 5, 6, 7}

#Створити set котрий приймає в себе наступний ряд: 5, 6, 7, 8, 9, 10, 11
set_two = {5, 6, 7, 8, 9, 10, 11}

#Розширити перший сет за допомогою коменди .add(0)
set_one.add(5)

#Виконати команду .intersection() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
set_one = {1, 2, 3, 4, 5, 6, 7}
set_two = {5, 6, 7, 8, 9, 10, 11}

set_three = set_one.intersection(set_two)


#Виконати команду .difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
set_four = set_one.difference(set_two)

#Виконати команду .symmetric_difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
set_five = set_one.symmetric_difference(set_two)

#Вивести всі змінні у консоль.
print('set_one:',set_one)
print('set_two:',set_two)
print('set_three:',set_three)
print('set_four:',set_four)
print('set_five:', set_five)