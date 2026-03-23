## Class Relationships
'''
Book (metadata)
  │
  └──1:n──▶ BookItem (physical copy)
                │
                ├── status: BookStatus
                ├── due_date
                └── borrowed_by: Member

Member
  │
  ├── checked_out_books: List[BookItem]
  ├── fines: List[Fine]
  └── reservations

Library
  │
  ├── Catalog (search)
  ├── FineStrategy (calculate fines)
  ├── NotificationService (notify members)
  └── reservations: Dict[isbn, deque[BookReservation]]
'''
from abc import abstractmethod
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional
from collections import deque
import uuid

class BookStatus(Enum):
    AVAILABLE= "available"
    LOANED= "loaned"
    RESERVED= "reserved"
    LOST= "lost"

class MemberStatus(Enum):
    ACTIVE="active"
    SUSPENDED="suspended"

# Exceptions
class BookNotAvailableException(Exception):
    pass
class MemberSuspendedException(Exception):
    pass
class BookNotFoundException(Exception):
    pass

# Author
class Author:
    def __init__ (self, name:str, book:str=""):
        self.name =name
        self.book = book

# Rack
class Rack:
    def __init__(self, rack_id:str, floor:int, section:str):
        self.rack_id = rack_id
        self.floor = floor
        self.section = section

    def __str__(self):
        return f"Floor: {self.floor}, Section: {self.section}, Rack ID: {self.rack_id}"
    
# Book(metadata)
class Book:
    def __init__(self, isbn:str, title:str, authors:List[Author], subject:str, publisher:str, pages:int):

        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.subject = subject
        self.publisher = publisher
        self.pages = pages

# BookItem(physical copy)
class BookItem:
    def __init__(self, barcode:str, book:Book, rack:Rack):
        self.barcode = barcode
        self.book = book
        self.rack = rack
        self._status = BookStatus.AVAILABLE
        self.due_date: Optional[datetime] = None
        self.borrowed_by:Optiona['Member'] = None 
        """By using a string literal 'Member', the type checker understands the type hint, but the Python interpreter does not attempt to resolve the name Member at that moment. This is a forward reference."""

    @property
    def status(self)->BookStatus:
        return self._status
    
    def checkout(self, member:'Member', loan_days:int =14):
        self._status = BookStatus.LOANED
        self.due_date = datetime.now() + timedelta(days=loan_days)
        self.borrowed_by = member
    
    def return_item(self):
        self._status = BookStatus.AVAILABLE
        self.due_date = None
        self.borrowed_by = None

    def is_overdue()->bool:
        if self.due_date is None:
            return False
        return datetime.now() > self.due_date
    
# Observer pattern for notifications
class NotificationObserver(ABC):
    @abstractmethod
    def notify(self, member:'Member', message:str):
        pass

class EmailNotification(NotificationObserver):
    def notify(self, member:'Member', message:str):
        print(f"Email to {member.name}, {member.email}: {message}")

class SMSNotification(NotificationObserver):
    def notify(self, member:'Member', message:str):
        print(f"SMS to {member.name}, {member.phone}: {message}")

class NotificationService:
    def __init__(self):
        self._observers: List[NotificationObserver] = []

    def add_observer(self, observer:NotificationObserver):
        self._observers.append(observer)
    
    def notify_all(self, member:'Member', message:str):
        for observer in self._observers:
            observer.notify(member, message)

# Strategy pattern for fine calculation
class FineStrategy(ABC):
    @abstractmethod
    def calculate_fine(self, days_overdue:int)->float:
        pass

class SimpleFineStrategy(FineStrategy):
    '''$0.5 per day'''
    def calculate_fine(self, days_overdue:int)->float:
        return max(0, days_overdue * 0.5)  

class ProgressiveFineStrategy(FineStrategy):
    '''$0.5 for first 5 days, then $1 per day'''
    def calculate_fine(self, days_overdue:int)->float:
        if days_overdue <= 5:
            return max(0, days_overdue *0.5)
        else:
            return 5*0.5 + (days_overdue -5)*1
        
# Fine
class Fine:
    def __init__(self, member: 'Member', amount:float, book_item: BookItem):
        self.id = str(uuid.uuid4())[:8]  # Short unique ID
        self.member = member
        self.book_item = book_item
        self.amount = amount
        self.paid = False
        self.created_at = datetime.now()

    def pay():
        self.paid = True

#BookLending
class BookLending:
    def __init__(self, book_item:BookItem, member:'Member'):
        self.id = str(uuid.uuid4())[:8]
        self.book_item = book_item
        self.member = member
        self.checkout_date = datetime.now()
        self.due_date = book_item.due_date
        self.return_date: Optional[datetime] = None 

    def complete_return(self):
        self.return_date = datetime.now()
    
    # BookReservation
class BookReservation:
    def __init__(self, book:Book, member:'Member'):
        self.id = str(uuid.uuid4())[:8]
        self.book = book
        self.member = member
        self.reserved_at = datetime.now()
        self.fulfilled = False

    def fulfill(self):
        self.fulfilled = True

# Member
class Member:
    MAX_BOOKS =5
    def __init__(self, member_id:str, name:str, email:str, phone:str):
        self.id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.check_out_books: List[BookItem] = []
        self.fines : List[Fine] =[]

    def can_checkout(self)->bool:
        if self.status == MemberStatus.SUSPENDED:
            return False
        if len(self.check_out_books) >= self.MAX_BOOKS:
            return False
        if any(not fine.paid for fine in self.fines):
            return False
        return True
    
    def add_book(self, book_item:BookItem):
        self.check_out_books.append(book_item)

    def remove_book(self, book_item:BookItem):
        self.check_out_books.remove(book_item)
    
    def add_fine(self, fine:Fine):
        self.fines.append(fine)

    # Librarian
class Librarian:
    def __init__(self, employee_id:str, name:str):
        self.id = employee_id
        self.name = name

    def add_book_item(self, library:'Library', book_item:BookItem):
        library.add_book_item(book_item)
    
    def block_member(self, member:Member):
        member.status = MemberStatus.SUSPENDED

# ===============Catalog (search)===============
class Catalog:
    def __init__(self):
        self._books: Dict[str, Book]={} #isbn-->Book
        self._book_items: Dict[str, List[BookItem]] = {} #isbn --> List[BookItem]

    def add_book(self, book:Book):
        self._books[book.isbn] = book
        if book.isbn not in self._book_items:
            self._book_items[book.isbn] = []
# # After add_book()
'''self._books = {
    "978-1984": Book("1984")      # Metadata stored
}
self._book_items = {
    "978-1984": []                 # Empty list, ready for copies
}'''

    def add_book_item(self, book_item:BookItem):
        isbn = book_item.book.isbn
        if isbn not in self._book_items:
            self._book_items[isbn] =[]
        self._book_items[isbn].append(book_item)
    
    def search_by_title(self, title:str)->List[Book]:
        return [b for b in self._books.values() if title.lower() in b.title.lower()]
    
    def search_by_author(self, author_name:str)->List[Book]:
        results =[]
        for book in self._books.values():
            if any(author_name.lower() in a.name.lower() for a in book.authors):
                results.append(book)
        return results
    
    def search_by_isbn(self, isbn:str)->Optional[Book]:
        return self._books.get(isbn)

    def search_by_subject(self, subject:str)-> List[Book]:
        return [b for b in self._books.values() if subject.lower() in b.subject.lower()]

    def get_available_copies(self, book:Book)->List[BookItem]:
        # dict.get(key, [])	Returns Value	Returns []
        items = self._book_items.get(boo.isbn, [])
        return [item for item in items if item.status==BookStatus.AVAILABLE]

    def get_all_copies(self, book:Book)->List[BookItem]:
        return self._book_items.get(book.isbn, [])

# ===========Library=======
class Library:
    def __init__(self, name:str, fine_strategy: FineStrategy):
        self.name = name
        self.catlog = Catalog()
        self._fine_strategy =fine_strategy
        self._notification_service = NotificationService()
        self._reservations: Dict[str, deque] = {} # isbn-> queue for BookReservation
        self._lendings :List[BookLending]=[]
    
    def add_notification_channel(self, observer:NotificationObserver):
        self._notification_service.add_observer(observer)

    def set_fine_strategy(self, strategy:FineStrategy):
        self._fine_strategy = strategy
    
    # Book Management
    def add_book(self, book:Book):
        self.catalog.add_book(book)
        self._reservations[book.isbn] = deque()

    def add_book_item(self, book_item:BookItem):
        self.catalog.add_book_item(book_item)

    def search_by_title(self, title:str)->List[Book]:
        return self.catalog.search_by_title(title)
    
    def search_by_isbn(self, isbn:str)->Optional[Book]:
        return self.catalog.search_by_isbn(isbn)

    def search_by_subject(self, subject:str)-> List[Book]:
        return self.catalog.search_by_subject(subject)
    
    def checkout_book(self, book_item:BookItem, member:Member)->BookLending:
        if not member.can_checkout():
            raise MemberSuspendedException("Member cannot checkout books")

        if book_item.status != BookStatus.AVAILABLE:
            raise BookNotAvailableException("Book is not available")

        # Checkout
        book_item.checkout(member)
        member.add_book(book_item)

        # Create lending record
        lending = BookLending(book_item, member)
        self._lendings.append(lending)

        print(f"Checkout: {book_item.book.title} to {member.name}")
        print(f"Due date: {book_item.due_date}")
        return lending

        # Return book
        def return_book(self, book_item:BookItem)->Optional[Fine]:
            member = book_item.borrowed_by
            fine = None

            if member is None:
                raise InvalidBookException("Book os not checked out")

            # Calculate fine if overdue
            if book-item.is_iverdue():
                days_overdue = (datetime.now() - book_item.due_date).days
                fine_amount = self._fine_strategy.calculate_fine(days_overdue)
                fine = Fine(member, fine_amount, book_item)
                member.add_fine(fine)
                print(f"Fine of ${fine_amount:.2f} for {days_overdue} days overdue")

            # Update lending record
            for lending in self._lendings:
                if lending.book_item == book_item and lending.return_date is None:
                    lending.complete_return()
                    break
            
            # Return the book
            member.remove_book(book_item)
            book_item.return_item()

            # Check reservation queue (Observer pattern)
            self._process_reservation_queue(book_item.book)

            print(f"Returned: {book_item.book.title}")

            return fine
        
    def reserve_book(self, book:Book, member: Member)-> BookReservation:
        reservation = BookReservation(book, member)
        
        if book.isbn not in. self._reservations:
            self._reservations[book.isbn] = deque()     
    
        self.-reservations[book,isbn].append(reservation)
        print(f"Reserved: {book.title} for {member.name}")
        print(f"Position in queue: {len(self._reservations[book.isbn])}")
        return reservation