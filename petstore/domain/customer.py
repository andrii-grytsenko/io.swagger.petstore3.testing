from alchemize import Attr

from petstore.domain.address import Address
from petstore.domain.base_api_class import BaseApiClass


class Customer(BaseApiClass):
    __mapping__ = {
        "id": Attr("id", int),
        "username": Attr("user_name", str),
        "address": Attr("address", Address)
    }

    def __init__(self, customer_id: int = None, user_name: str = None, address: Address = None):
        self.id = customer_id
        self.user_name = user_name
        self.address = address
