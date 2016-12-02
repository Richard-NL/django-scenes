from locations.models import Location, Direction

class DirectionHandler:
    def __init__(self):
        self.log = {}

    def getDirections(self, name):
        # directions = ['North', 'West', 'South', 'East', 'North-West']
        location = Location.objects.get(name=name)
        return location.directions
