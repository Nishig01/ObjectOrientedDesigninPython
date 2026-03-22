from abc import ABC, abstractmethod

from datetime import datetime, timedelta
from typing import List, Optional

# Exceptions
class ParkFullException(Exception):
    pass
class InvalidTicketException(Exception):
    pass

# Vehicle Hierarchy
class Vehicle(ABC):
    @abstractmethod
    def get_size(self)->int:
        pass

class Car(Vehicle):
    def get_size(self)->int:
        return 1

class Bus(Vehicle):
    def get_size(self)->int:
        return 3

class Motorcycle(Vehicle):
    def get_size(self)->int:
        return 1

# Spot
class Spot:
    def __init__(self, spot_id:int):
        self.spot_id = spot_id
        self._is_available = True

    def is_available(self)->bool:
        return self._is_available

    def take_spot(self):
        self._is_available = False

    def clear_spot(self):
        self._is_available = True

# Ticket
class Ticket:
    def __init__(self, vehicle:Vehicle, spots: List[Spot]):
        self.vehicle = vehicle
        self.start_time = datetime.now()
        self.spots = spots

# ParkingLot
class ParkingLot:
    def __init__(self, num_spots:int, hourly_rate: float = 2.0):
        self.spots : List[Spot] = [Spot(i) for i in range(num_spots)]
        self.hourly_rate = hourly_rate
        self._available_count = num_spots
        self._tickets = {} #dictionary

    def get_available_count(self)->int:
        return self._available_count

    def _find_spots(self, vehicle:Vehicle)->Optional[List[Spot]]: ## Either returns a list of spots, or None if no spots found
        """Find consecutive spots on the parking lot."""
        size_needed = vehicle.get_size()
        consecutive = []

        for spot in self.spots:
            if spot.is_available():
                consecutive.append(spot)
                if len(consecutive) == size_needed:
                    return consecutive
            else:
                consecutive =[]
        return None

    def park_vehicle(self, vehicle:Vehicle)->Ticket:
        """Park vehicle on the parking lot. and return a ticket"""
        spots = self._find_spots(vehicle)
        if spots is None:
            raise ParkFullException("No available spots for this vehicle")

        for spot in spots:
            spot.take_spot()

        self._available_count-=len(spots)

        ticket = Ticket(vehicle, spots)
        self._tickets[id(vehicle)] = ticket #id is built in fn in python assigns unique id
        return ticket

    def clear_spot(self, ticket:Ticket):
        """Remove a spot from the parking lot when vehicle leaves."""
        if id(ticket.vehicle) not in self._tickets:
            raise InvalidTicketException("No available spots for this vehicle")

        for spot in ticket.spots:
            spot.clear_spot()

        self._available_count += len(ticket.spots)
        del self._tickets[id(ticket.vehicle)]

    def calculate_fee(self, ticket:Ticket)->float:
        """Calculate parking fee based in duration"""
        duration = datetime.now() - ticket.start_time
        print(f"Duration: {datetime.now()}, {ticket.start_time}")
        hours = duration.total_seconds()/3600
        return round(max(1, hours)* self.hourly_rate, 3)

#   Demo
if __name__ =="__main__":
    lot = ParkingLot(num_spots=20)
    print(f"Available spots: {lot.get_available_count()}")

    car=Car()
    bus=Bus()
    motorcycle=Motorcycle()

    ticket1 = lot.park_vehicle(car)
    ticket2 = lot.park_vehicle(bus)

    # we can wait for a ticket1 for 2 hours using thread?
    ticket1.start_time = datetime.now()-timedelta(hours=6)
    ticket2.start_time = datetime.now()-timedelta(hours=2)

    print(f"Car parked. Available: {lot.get_available_count()} {lot.calculate_fee(ticket1):.2f}")
    lot.clear_spot(ticket1)
    print(f"Car left. Available: {lot.get_available_count()}")

    print(f"Car parked. Available: {lot.get_available_count()} {lot.calculate_fee(ticket2):.2f}")
    lot.clear_spot(ticket2)
    print(f"Car left. Available: {lot.get_available_count()}")
