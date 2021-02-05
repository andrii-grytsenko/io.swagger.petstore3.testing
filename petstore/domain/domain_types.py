from enum import Enum


class PetStatus(Enum):
    available = "available"
    pending = "pending"
    sold = "sold"


class OrderStatus(Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"


class UserStatus(Enum):
    registered = 1
    active = 2
    closed = 3
