'''Locker system for AmazonLocker
Locker System
Locker
Package
Order
Customer-->details
OTP
NotificationService

lockersize-->small, medium, large
# Package = just the box
package = Package("PKG-001", LockerSize.MEDIUM)

# Order = who's getting what
order = Order("ORD-001", package, customer)
```

## Code Flow
```
┌─────────────────────────────────────────────────────────────────┐
│                        DELIVERY FLOW                            │
└─────────────────────────────────────────────────────────────────┘

1. CREATE OBJECTS
   │
   │  customer = Customer("C1", "John", "john@email.com", "555-1234")
   │  package = Package("PKG-001", LockerSize.MEDIUM)
   │  order = Order("ORD-001", package, customer)
   │
   ▼
2. DELIVER PACKAGE
   │
   │  locker = system.deliver_package(order)
   │           │
   │           ├──▶ strategy.assign_locker(lockers, package)
   │           │         │
   │           │         └──▶ Find locker where size >= package.size
   │           │
   │           ├──▶ code = Code("482910")  # Generate OTP
   │           │
   │           ├──▶ locker.assign(order, code)
   │           │         │
   │           │         └──▶ locker._state = OCCUPIED
   │           │
   │           └──▶ notification_service.notify(customer, message)
   │                     │
   │                     ├──▶ EmailNotification.send()
   │                     └──▶ SMSNotification.send()
   │
   ▼
3. CUSTOMER RECEIVES
   │
   │  [EMAIL] To: john@email.com
   │    Locker: L3
   │    Code: 482910
   │    Expires: 2026-03-24
   │
   ▼
┌─────────────────────────────────────────────────────────────────┐
│                        PICKUP FLOW                              │
└─────────────────────────────────────────────────────────────────┘

4. PICKUP PACKAGE
   │
   │  package = system.pickup_package("L3", "482910")
   │            │
   │            ├──▶ Find locker by id
   │            │
   │            ├──▶ Check state != AVAILABLE (not empty)
   │            │
   │            ├──▶ Check state != EXPIRED
   │            │
   │            ├──▶ code.is_valid("482910")  # Validate OTP
   │            │
   │            └──▶ locker.release()
   │                      │
   │                      └──▶ locker._state = AVAILABLE
   │
   ▼
5. DONE
   │
   │  Customer has package ✓
   │  Locker is free ✓
'''


from enum import Enum
from abc import ABC, abstractmethod
from typing import Optional, List, Dict
from datetime import datetime, timedelta
import string
import random

class LockerSize(Enum):
    small=1
    medium=2
    large=3

class LockerState(Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    EXPIRED = "expired"

    # ======Exceptions============
class NoLockerAvailableException(Exception):
    pass
class InvalidCodeException(Exception):
    pass
class LockerExpiredException(Exception):
    pass

    # ===============Code=================
class Code:
    def __init__(self, code:str, expiration_hours: int =72):
        self.code = code
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(hours=expiration_hours)

    def is_expired(self)->bool:
        return datetime.now() > self.expires_at

    def is_valid(self, input_code:str)->bool:
        if self.is_expired():
            return False
        return self.code == input_code

# =================Customer=================
class Customer:
    def __init(self, customer_id:str, name:str, email:str, phone_number:str):
        self.id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

# ================Package===============
class Package:
    def __init__(self, package_id: str, size:LockerSize):
        self.id = package_id
        self.size = size
# =================Order=================
class Order:
    def __init__(self, order_id:str, package:Package, customer:Customer ):
        self.id = order_id
        self.package = package
        self.customer = customer
        self.created_at = datetime.now()
#     =======Observer Pattern: Notification=========
class Notification(ABC):
    @abstractmethod
    def send(self, customer:Customer, message:str):
        pass

class EmailNotification(Notification):
    def send(self, customer:Customer, message:str):
        print(f"[EMAIL] To: {customer.email}")
        print(f" {message}")

class SMSNotification(Notification):
    def send(self, customer:Customer, message:str):
        print(f"[EMAIL] To: {customer.phone_number}")
        print(f" {message}")

class NotificationService:
    """Observer - manages multiple notification channels."""
    def __init__(self):
        self._channels = List[Notification] =[]

    def add_channel(self, channel:Notification):
        self._channels.append(channel)

    def remove_channel(self, channel:Notification):
        self._channels.remove(channel)

    def notify(self, customer:Customer, message:str):
        for channel in self._channels:
            channel.send(customer, message)

# =========Locker (state pattern)==================
class Locker:
    def __init__(self, locker_id:str, size:LockerSize):
        self.id = locker_id
        self.size = size
        self._state = LockerState.AVAILABLE
        self.package : Optional[Package] = None
        self.code :Optional[Code] = None
        self.order : Optional[Order] = None

    @property
    def state(self)->LockerState:
        if self._state == LockerState.OCCUPIED and self.code and self.code.is_expired():
            self._state = LockerState.EXPIRED
        return self._state

    def is_available(self)->bool:
        return self._state == LockerState.AVAILABLE

    def assign(self, order:Order, code:Code):
        if not self.is_available():
            raise Exception("Locker is not available")

        self.order = order
        self.package = order.package
        self.code = code
        self._state = LockerState.OCCUPIED

    def release(self):
        self.order = None
        self.package = None
        self.code = None
        self._state = LockerState.AVAILABLE


# =================Strategy Pattern: Locker Assignment=========
class LockerAssignmentStrategy(ABC):
    @abstractmethod
    def assign_locker(self, lockers:List[Locker], package:Package)->Optional[Locker]:
        pass

class ExactFitStrategy(LockerAssignmentStrategy):
    """Assign exact size match first, then larger."""
    def assign_locker(self, lockers: List[Locker], package:Package)->Optional[Locker]:
        available =[l for l in lockers if l.is_available() and l.size.value >= package.size.value]

        if not available:
            return None

#         Sort by size - prefer exact fit
        available.sort(key=lambda l:l.size.value)
        return available[0]

class LargestFirstStrategy(LockerAssignmentStrategy):
    """Always assign largest available locker."""
    def assign_locker(self, lockers:List[Locker], package:Package)->Optional[Locker]:
        available =[l for l in lockers if l.is_available() and l.size.value>=package.size.value]

        if not available:
            return None
        # # You use 'key' to tell it: "Compare them using their 'value' attribute"
        available.sort(key=lambda l : l.size.value, reverse=True)
        return available[0]

class LockerSystem:
    def __init__(self, assignment_strategy:LockerAssignmentStrategy):
        self._lockers: List[Locker]=[]
        self._assignment_strategy = assignment_strategy
        self._notification_service = NotificationService()
        self._orders: Dict[str, Locker] ={} #order_id -> locker

    def add_locker(self, locker:Locker):
        self._lockers.append(locker)

    def add_notification_channel(self, channel:Notification):
        self._notification_service.add_channel(channel)

    def set_assignment_strategy(self, strategy:LockerAssignmentStrategy):
        self._assignment_strategy = strategy

#   Code generation
    def _generate_code(self)->str:
        return ''.join(random.choices(string.digits, k=6))
#   Deliver package to locker
    def deliver_package(self, order:Order)->Locker:
        locker = self._assignment_strategy.assign_locker(self._lockers, order.package)

        if not locker:
            raise NoLockerAvailableException("No locker available for this package")

        # 2. Generate code
        code = Code(self._generate_code())

        # 3. Assign locker
        locker.assign(order, code)
        self._orders[order.id] = locker

        # 4. Notify customer
        message = (f"Your package {order.package.id} is read!\n"
                   f"Locker: {locker.id}\n"
                   f"Code: {code.code}\n"
                   f"Expires: {code.expires_at}")
        self._notification_service.notify(order.customer, message)
        return locker

    # Customer picks up package
    def pickup_package(self, locker_id:str, input_code: str)->Package:
        # Find locker
        locker = next((l for l in self._lockers if l.id == locker_id), None) #next() grabs the first one that matches your criteria and stops immediately.
        if not locker:
            raise NoLockerAvailableException("Code has expired. Contact customer service.")

        # Check state
        if locker.state == LockerState.AVAILABLE:
            raise Exception("Locker is empty")

        if locker.state == LockerState.EXPIRED:
            raise LockerExpiredException("Code has expired. Contact customer service.")

        # Validate code
        if not locker.code.is_valid(input_code):
            raise InvalidCodeException("Invalid code")

        # Release package
        package = locker.package
        order_id = locker.order.id
        locker.release()

        if order_id in self._orders:
            del self._orders[order_id]

        return package

#      Cleanup: Handle expired lockers
    def process_expired_lockers(self):
        for locker in self._lockers:
            if locker.state == LockerState.EXPIRED:
                customer = locker.order.customer

#                 Notify customer
                message = f"Your package {locker.package.id} was not picked up and has been returned"
                self._notification_service.notify(customer, message)

#                 Release locker
                print(f"Returning package {locker.package.id} to warehouse")
                locker.release()

    def get_available_lockers(self)->Dict[LockerSize, int]:
        counts ={size :0 for size in LockerSize}
        '''Small: 0, Medium: 0, Large: 0'''
        for locker in self._lockers:
            if locker.is_available():
                counts[locker.size] +=1
        return counts #{LockerSize.SMALL: 12, LockerSize.MEDIUM: 5, LockerSize.LARGE: 2}




