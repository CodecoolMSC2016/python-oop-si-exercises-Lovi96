from vehicle import Vehicle


class Car(Vehicle):

    is_running = False

    def start_engine(self):
        if not self.is_running:
            self.is_running = True

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
