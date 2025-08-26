# vehicle_demo.py

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Car(Vehicle):
    def move(self):
        print(f"{self.name}: Driving on the road! 🚗")


class Plane(Vehicle):
    def move(self):
        print(f"{self.name}: Flying in the sky! ✈️")


class Boat(Vehicle):
    def move(self):
        print(f"{self.name}: Sailing on the water! 🛥️")


class Bike(Vehicle):
    def move(self):
        print(f"{self.name}: Pedaling down the street! 🚲")


class Train(Vehicle):
    def move(self):
        print(f"{self.name}: Running on tracks! 🚆")


# -----------------------------------
# Polymorphism in action
def main():
    vehicles = [
        Car("Toyota"),
        Plane("Boeing 747"),
        Boat("SailMaster 3000"),
        Bike("Mountain Bike"),
        Train("Express Line")
    ]

    print("🚦 Vehicles are now moving:\n")
    for v in vehicles:
        v.move()


if __name__ == "__main__":
    main()
