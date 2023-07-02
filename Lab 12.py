#Створити файл та записати в нього рядок.

with open('myfile.txt', 'w+') as file:
    file.write('Lorem Ipsum')

#Прочитати створений файл та вивести на консоль вміст файлу
file = open('myfile.txt', 'r')
print(file.read())
file.close()


#Додати ще один рядок до створеного файлу.
file = open('myfile.txt', 'a')
file.write('Lorem Ipsum1')
file.close()


#Прочитати всі рядки з файлу та вивести на консоль.
file = open('myfile.txt', 'r')
print(file.readlines())
file.close()


#* Записати у файл все що користувач введе з консолі. (Якщо хочете більш ніж один рядок спробуйте використати while True і перевірку на введений рядок, типу якщо exit тоді це кінець.)

data = input('Your name: ')

with open('myfile.txt', 'a') as file:
    file.write(data + '\n')
