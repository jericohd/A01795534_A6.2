import json
import os
import unittest

"""
Reservation System Module
This module provides functionality to manage hotels, customers, and reservations.
"""

class Hotel:
    """Class representing a Hotel."""
    DATA_FILE = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """Convert hotel object to dictionary."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms
        }

    @staticmethod
    def save_hotels(hotels):
        """Save hotels list to JSON file."""
        with open(Hotel.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([hotel.to_dict() for hotel in hotels], file, indent=4)

    @staticmethod
    def load_hotels():
        """Load hotels from JSON file."""
        if not os.path.exists(Hotel.DATA_FILE):
            return []
        with open(Hotel.DATA_FILE, "r", encoding="utf-8") as file:
            return [Hotel(**data) for data in json.load(file)]

    @staticmethod
    def create_hotel(hotel_id, name, location, rooms):
        """Create and save a new hotel."""
        hotels = Hotel.load_hotels()
        hotels.append(Hotel(hotel_id, name, location, rooms))
        Hotel.save_hotels(hotels)

    @staticmethod
    def delete_hotel(hotel_id):
        """Delete a hotel by ID."""
        hotels = Hotel.load_hotels()
        hotels = [hotel for hotel in hotels if hotel.hotel_id != hotel_id]
        Hotel.save_hotels(hotels)

    @staticmethod
    def display_hotels():
        """Print the list of hotels."""
        hotels = Hotel.load_hotels()
        for hotel in hotels:
            print(f"{hotel.hotel_id}: {hotel.name} - {hotel.location} ({hotel.rooms} rooms)")

class Customer:
    """Class representing a Customer."""
    DATA_FILE = "customers.json"

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert customer object to dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    @staticmethod
    def save_customers(customers):
        """Save customers list to JSON file."""
        with open(Customer.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([customer.to_dict() for customer in customers], file, indent=4)

    @staticmethod
    def load_customers():
        """Load customers from JSON file."""
        if not os.path.exists(Customer.DATA_FILE):
            return []
        with open(Customer.DATA_FILE, "r", encoding="utf-8") as file:
            return [Customer(**data) for data in json.load(file)]

    @staticmethod
    def create_customer(customer_id, name, email):
        """Create and save a new customer."""
        customers = Customer.load_customers()
        customers.append(Customer(customer_id, name, email))
        Customer.save_customers(customers)

class Reservation:
    """Class representing a Reservation."""
    DATA_FILE = "reservations.json"

    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convert reservation object to dictionary."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id
        }

    @staticmethod
    def save_reservations(reservations):
        """Save reservations list to JSON file."""
        with open(Reservation.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([res.to_dict() for res in reservations], file, indent=4)

    @staticmethod
    def load_reservations():
        """Load reservations from JSON file."""
        if not os.path.exists(Reservation.DATA_FILE):
            return []
        with open(Reservation.DATA_FILE, "r", encoding="utf-8") as file:
            return [Reservation(**data) for data in json.load(file)]

    @staticmethod
    def create_reservation(reservation_id, customer_id, hotel_id):
        """Create and save a new reservation."""
        reservations = Reservation.load_reservations()
        reservations.append(Reservation(reservation_id, customer_id, hotel_id))
        Reservation.save_reservations(reservations)

# Unit tests
class TestReservationSystem(unittest.TestCase):
    """Unit tests for reservation system."""
    def setUp(self):
        self.test_hotel = Hotel(1, "Test Hotel", "Test City", 20)
        self.test_customer = Customer(1, "Test User", "test@example.com")
        self.test_reservation = Reservation(1, 1, 1)

    def test_hotel_creation(self):
        """Test creating a hotel."""
        Hotel.create_hotel(self.test_hotel.hotel_id, self.test_hotel.name, self.test_hotel.location, self.test_hotel.rooms)
        hotels = Hotel.load_hotels()
        self.assertTrue(any(hotel.hotel_id == 1 for hotel in hotels))

    def test_customer_creation(self):
        """Test creating a customer."""
        Customer.create_customer(self.test_customer.customer_id, self.test_customer.name, self.test_customer.email)
        customers = Customer.load_customers()
        self.assertTrue(any(customer.customer_id == 1 for customer in customers))

    def test_reservation_creation(self):
        """Test creating a reservation."""
        Reservation.create_reservation(self.test_reservation.reservation_id, self.test_reservation.customer_id, self.test_reservation.hotel_id)
        reservations = Reservation.load_reservations()
        self.assertTrue(any(res.reservation_id == 1 for res in reservations))

if __name__ == "__main__":
    unittest.main()
