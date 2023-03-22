
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date: str, end_date: str):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        visitor.add_trip(self)
        national_park.add_trip(self)
    
