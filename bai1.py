
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



e = Elevator(1, 10)
e.go_to_floor(5)
e.go_to_floor(1)

