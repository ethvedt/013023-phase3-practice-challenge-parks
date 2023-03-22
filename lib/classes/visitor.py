from .trip import Trip

class Visitor:

    def __init__(self, name):
        if type(name) == str:
            self._name = name
            self._trips = []
    
    def getname(self):
        return self._name
    
    def setname(self, name):
        if type(name) == str and (1 <= len(name) <= 15):
            self._name = name
    
    name = property(getname, setname)

    def trips(self):
        return self._trips
    
    def add_trip(self, trip):
        if type(trip) == Trip:
            self._trips.append(trip)

    def nationalparks(self):
        return list(set(map(lambda trip: trip.national_park, self.trips())))
    
    def create_trip(self, national_park, start_date, end_date):
        return Trip(self, national_park, start_date, end_date)
