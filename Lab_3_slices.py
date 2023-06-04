
# За допомогою даної конструкції перевернути рядок
text = 'Python programing makes me cry'[::-1]
print(text)

# За допомогою даної конструкції перевернути список
locations_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_locations_list = slice(15)
print(locations_list[sliced_locations_list])


# Повернути частину списку від 2 до 7 елементу з кроком 2
locations_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = slice(2, 7)
print(locations_list[x])

# Поварнути частину рядка (вважати рядок списком)


a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])