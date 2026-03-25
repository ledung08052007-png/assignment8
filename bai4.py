import random


class Car:
    def __init__(self, reg, max_speed):
        self.registration_number = reg
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def accelerate(self, change):
        self.current_speed = self.current_speed + change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance_travelled = self.distance_travelled + self.current_speed * hours


class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.distance = kilometers
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print("\nRace:", self.name)
        print("-------------------------------------------------")
        print("Car        Max speed   Current speed   Distance")
        print("-------------------------------------------------")

        for car in self.cars:
            print(
                f"{car.registration_number:<10} "
                f"{car.max_speed:<11} "
                f"{car.current_speed:<15} "
                f"{car.distance_travelled:.1f}"
            )

    def race_finished(self):
        for car in self.cars:
            if car.distance_travelled >= self.distance:
                return True
        return False


# main program
cars = []

for i in range(10):
    reg_number = "ABC-" + str(i + 1)
    max_speed = random.randint(150, 200)
    car = Car(reg_number, max_speed)
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while race.race_finished() == False:
    hours = hours + 1
    race.hour_passes()

    if hours % 10 == 0:
        print("\nAfter", hours, "hours")
        race.print_status()

print("\nRace finished!")
print("It took", hours, "hours.")
race.print_status()