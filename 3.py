class Vehicle:
    def move(self):
        return ("Vehicle is moving")



class Car(Vehicle):
    def move(self):
        return ("Car is driving")


class Bicycle(Vehicle):
    def move(self):
        return ("Bicycle is pedaling")

def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()
print(move(car))
# Вывод: Car is driving
print(move(bike))
# Вывод: Bicycle is pedal






