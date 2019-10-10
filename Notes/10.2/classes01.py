class Flight():

    def __init__(self, flight_number, origin, destination, duration):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.duration = duration

        #remember a list of passengers
        self.passengers = []

    def get_duration(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return (hours, minutes)

    def delay(self, minutes):
        self.duration += minutes;

    def add_passenger(self, p):
        self.passengers.append(p)

class Passenger():
    def __init__()
