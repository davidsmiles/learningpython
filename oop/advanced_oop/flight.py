from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        """
        :return: a string in the format of GLA -> LHR -> CAN
        """
        stops = [self.departure_point, self.destination_point]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return ' -> '.join(stops)

    @property
    def departure_point(self):
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)

    @property
    def destination_point(self):
        return self.segments[0].destination

    @destination_point.setter
    def destination_point(self, val):
        dept = self.segments[0].departure
        self.segments[0] = Segment(departure=dept, destination=val)


segment = Segment('Ughelli', 'Lagos')
flight = Flight([segment])
print(flight)

flight.departure_point = 'Benin'
flight.destination_point = 'Kano'
print(flight)

lists = ['cat', 'dog', 'cow', 'goat', 'rat']
print(lists[1:])
