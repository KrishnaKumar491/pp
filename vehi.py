class vehicle:
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("car started")

ob1=car()
ob1.start()