from vehicle import *


class Truck(Vehicle):

    carry_limit = 0
    current_carriage_weight = None
    has_carriage = False

    def has_carriage(self):
        if self.current_carriage_weight != None:
            return True
        else:
            return False

    def attach_carriage(self, carriage_weigth):
        self.carriage_weigth = carriage_weigth
        if self.carry_limit >= carriage_weigth:
            return True
        else:
            return False

    def detach_carriage(self):
        if self.current_carriage_weight != None:
            self.current_carriage_weight = None
        else:
            pass
