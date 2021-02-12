from alchemize import Attr

from petstore.domain.base_api_class import BaseApiClass
from petstore.domain.domain_types import OrderStatus


class Order(BaseApiClass):
    __mapping__ = {
        "id": Attr("id", int),
        "petId": Attr("pet_id", int),
        "quantity": Attr("quantity", int),
        "shipDate": Attr("ship_date", str),
        "status": Attr("status", OrderStatus),
        "complete": Attr("complete", bool),
    }

    def __init__(self, order_id: int = None, pet_id: int = None, quantity: int = None, ship_date: str = None,
                 status: OrderStatus = None, complete: bool = None):
        self.id = order_id
        self.pet_id = pet_id
        self.quantity = quantity
        self.ship_date = ship_date
        self.status = status
        self.complete = complete
