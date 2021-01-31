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


class ApiResponseType(Enum):
    error = "Error"
    warning = "Warning"
    info = "Info"
    ok = "OK"
    too_busy = "Too busy"
