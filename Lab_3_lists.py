#створити список

fruit_list = ["apple", "banana", "cherry"]
print(fruit_list)

#копіювати через .copy()

vegetable_list = ["tomato", "potato", "cucumber"]
mylist = vegetable_list.copy()
print(mylist)

#додати елемент до списку.
locations_list = ["Atlanta", "San Antonio", "San Francisco"]
locations_list.append("Alaska")
print(locations_list)

#вставити елемент а певне місце.
locations_list = ["Atlanta", "San Antonio", "San Francisco"]
locations_list.insert(1, "Alaska")
print(locations_list)
#додати один список до іншого 2 способами *

#1
list1 = ["here", "we", "go"]
list2 = [10, 20, 30]
list3 = list1 + list2
print(list3)


#2
list1 = ["and", "again", "here", "we", "go"]
list2 = [10, 20, 30]
list1.extend(list2)
print(list1)

#команда .pop()
meat_list = ['pork', 'chicken', 'beef']
meat_list.pop(1)

#видалити елемент за значенням
meat_list = ['pork', 'chicken', 'beef']
meat_list.remove('pork')

#видалити елемент за індексом
meat_list = ['pork', 'chicken', 'beef']
meat_list.pop(1)

#показати як дістати значення елемента за його індексом
meat_list = ['pork', 'chicken', 'beef']
meat_list.pop(1)