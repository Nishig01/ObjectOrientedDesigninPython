'''
# input--> package
# op--> locker, slot, otp
# Core objects
# Package n->1 Locker System 1 to n Locker 1 to n Slot
# Receipt-->manage relation bw package and slot

# use cases
1. system should allocate a locker that fits the item size  -> reserve
    ->serve
    2. generate a code/otp and send it to the user, also send the locker location
    3. validate if an otp opens a locker
    ->checkout
    4. empty the locker after use
    5. empty the locker after 3 days

followup-->give the closest locker to the user

Class diag
Locker System -->
-OtpGenerator
-OtpRepository
-SlotFilterStrategy
-SlotAssginmentStrategy
+Slot allocateSlot(Package package)
+List<Slot> getAvailableSlots
+void deallocateSlot(Receipt receipt)
+Slot createSlot(Locker locker, Size slotSize)
+string generateOtp(slot slot, string otp)
+bool validateOtp(slot slot, string otp)
+void notifyUser(Receipt receipt)

Locker -->
-string id
-List<slot> slots
+void addSlot(slow slot)
+List<slot> getAvailableSlots()

slot-->
-string slotId
-size size
-Locker locker
-Package package
-Date allocation Date
+void allocateSlot(Package package)
+void deallocateSlot()
+bool isAvailable()

Singleton
size
-double width
-double length
-double height
+bool canFit(size size)

Package
-size size
-string id

<<Interface>> User --> Buyer & DeliveryPerson
#Contact contact
+virtual contact getContact()


Receipt--
-Slot slot
-Package package
-String otp
-User user

Contact
-String email
-String address

LockerSystem (the whole Amazon Locker network)
    │
    ├── Locker (physical locker unit at a location, e.g., Whole Foods)
    │       │
    │       ├── Slot (individual compartment)
    │       ├── Slot
    │       └── Slot
    │
    ├── Locker (another location, e.g., 7-Eleven)
    │       │
    │       ├── Slot
    │       ├── Slot
    │       └── Slot
    │
    └── Locker (another location)
            │
            ├── Slot
            └── Slot
'''
from datetime import datetime, timedelta
from typing import List, Optional, Dict
import random
import string

class NoSlotAvailableException(Exception):
    pass
class InvalidOtpException(Exception):
    pass

# =========Size============

class Size:
    def __init__(self, width:float, length:float, height:float):
        self.width = width
        self.length = length
        self.height = height

    def can_fit(self, other:'Size')->bool:
        return (self.width >= other.width and self.length >= other.length and self.height >= other.height)

class Package:
    def __init__(self, package_id:str, size:Size):
        self.id = package_id
        self.size =size

class Slot:
    def __init__(self, slot_id:str, size:Size):
        self.slot_id = slot_id
        self.size = size
        self.package: Optional[Package] = None

    def is_available(self)->bool:
        return self.package is None

    def allocate(self, package:Package):
        self.package = package

    def deallocate(self):
        self.package = None

class Locker:
    def __init__(self, locker_id:str):
        self.id= locker_id
        self.slots: List[Slot] =[]

    def add_slot(self, slot:Slot):
        self.slots.append(slot)

    def get_available_slots(self)->List[Slot]:
        return [s for s in self.slots if s.is_available()]


class LockerSystem:
    def __init__(self):
        self._lockers: List[Locker] =[]
        self._otp_map: Dict[str,str] ={} #slot_id->otp

    def add_locker(self, locker:Locker):
        self._lockers.append(locker)

    def _generate_otp(self)->str:
        return ''.join(random.choices(string.digits, k=6))

    def _find_slot(self, package:Package)->Optional[Slot]:
        for locker in self._lockers:
            for slot in locker.get_available_slots():
                if slot.size.can_fit(package.size):
                    return slot
        return None

    def allocate(self, package:Package)->tuple[Slot, str]:
        slot = self._find_slot(package)
        if not slot:
            raise NoSlotAvailableException("No available slot")

        slot.allocate(package)
        otp = self._generate_otp()
        self._otp_map[slot.slot_id] = otp
        return slot, otp

    def pickup(self, slot_id:str, otp:str):
        if self._otp_map.get(slot_id) !=otp:
            return InvalidOtpException("Invalid OTP")

        for locker in self._lockers:
            for slot in locker.slots:
                if slot.slot_id == slot_id:
                    slot.deallocate()
                    del self._otp_map[slot_id]
                    return
