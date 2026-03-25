class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def floor_up(self):
        if self.floor < self.top:
            self.floor = self.floor + 1
            print("Elevator is now at floor", self.floor)

    def floor_down(self):
        if self.floor > self.bottom:
            self.floor = self.floor - 1
            print("Elevator is now at floor", self.floor)

    def go_to_floor(self, target):
        while self.floor < target:
            self.floor_up()

        while self.floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, number):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for i in range(number):
            e = Elevator(bottom, top)
            self.elevators.append(e)

    def run_elevator(self, elevator_number, destination):
        print("Running elevator", elevator_number, "to floor", destination)
        self.elevators[elevator_number - 1].go_to_floor(destination)

    def fire_alarm(self):
        print("Fire alarm! All elevators go to the bottom floor.")
        for i in range(len(self.elevators)):
            print("Elevator", i + 1)
            self.elevators[i].go_to_floor(self.bottom)



house = Building(1, 10, 3)
house.run_elevator(1, 7)
house.run_elevator(2, 5)
house.run_elevator(3, 9)

house.fire_alarm()