
                                  #Polymorphism


class Car:
    def wheels(self):
        print("Number of wheels: 4")

    def mode_of_transport(self):
        print("Mode of transport: Private usage")


class Bus:
    def wheels(self):
        print("Number of wheels: 8")

    def mode_of_transport(self):
        print("Mode of transport: Public usage")


car_obj1 = Car()
car_obj2 = Car()
bus_obj1 = Bus()
bus_obj2 = Bus()

vehicles = [car_obj1, car_obj2, bus_obj1, bus_obj2]


for vehicle in vehicles:
    vehicle.wheels()
    vehicle.mode_of_transport()
    print()


#2

    class Vehicle:
        def desc(self):
            print("Такс тут мав би бути опис транспорту")

        def wheels(self):
            print("Кількість колес")


    class Car(Vehicle):
        def desc(self):
            print("Це автомобіль.")

        def wheels(self):
            print("Кількість колес: 4")


    class Moto(Vehicle):
        def desc(self):
            print("Це мотоцикл.")

        def wheels(self):
            print("Кількість колес: 2")


    vehicle_obj = Vehicle()
    car_obj = Car()
    moto_obj = Moto()

    vehicle_obj.desc()
    vehicle_obj.wheels()

    car_obj.desc()
    car_obj.wheels()

    moto_obj.desc()
    moto_obj.wheels()


#2

class MyClass:
    def __init__(self):
        self._a = 'доступна'
        self.__a = 'не для мене мама квіточку ростила'


obj = MyClass()


print(obj._a)

print(obj.__a)

print(obj._MyClass__a)
# Output: 20
