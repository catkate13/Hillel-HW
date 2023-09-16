#Створити клас з абстрактним методом. Створити об'єкт даного класу.

from abc import abstractmethod

class SomeClass:
    @abstractmethod
    def abstract_method(self):
        pass

new_object = SomeClass()

class NewClass(SomeClass):
    def abstract_method(self):
        print('Some Abstract Mom')

new_object = NewClass()
new_object.abstract_method()


#Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.

import abc

class MyMetaclass(abc.ABCMeta):
    pass

class MyClass(metaclass=MyMetaclass):
    def some_method(self):
        print("Lorem Ipsum")

new_object = MyClass()
new_object.some_method()


#Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від абстрактного класу і створіть об'єкт нового класу.

from abc import ABC, abstractmethod

class SomeAbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class SomeNewClass(SomeAbstractClass):
    def abstract_method(self):
        print("Абстрактий метод успадкований від абстрактного класу")

new_object = SomeNewClass()
new_object.abstract_method()