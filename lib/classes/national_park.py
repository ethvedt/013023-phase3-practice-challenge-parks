from .trip import Trip

class NationalPark:

    def __init__(self, name):
        if type(name) == str:
            self._name = name
            self._trips = []

    def getname(self):
        return self._name
    
    def setname(self, name):
        if not hasattr(self, "_name"):
            self._name = name
    
    name = property(getname, setname)

    def add_trip(self, trip):
        if type(trip) == Trip:
            self._trips.append(trip)

    def trips(self):
        return self._trips
    
    def visitors(self):
        return list(set(map(lambda trip: trip.visitor, self.trips())))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = {}
        for trip in self.trips():
            if trip.visitor.name not in visitors:
                visitors[trip.visitor.name] = 1
            visitors[trip.visitor.name] += 1
        for visitor in self.visitors():
            if visitor.name == max(visitors, key=visitors.get):
                return visitor
        
    

