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

    db = None  # database.Database()

    def __init__(self, order_id: int = None, pet_id: int = None, quantity: int = None, ship_date: str = None,
                 status: OrderStatus = None, complete: bool = None):
        self.id = order_id
        self.pet_id = pet_id
        self.quantity = quantity
        self.ship_date = ship_date
        self.status = status
        self.complete = complete

    def to_json(self):
        return {"id": self.id, "petId": self.pet_id,
                "quantity": self.quantity, "shipDate": self.ship_date,
                "status": self.status.value, "complete": self.complete}

    @classmethod
    def from_json(cls, json):
        if "id" in json and "petId" in json \
                and "quantity" in json and "shipDate" in json \
                and "status" in json and "complete" in json:
            return cls(json["id"], json["petId"], json["quantity"],
                       json["shipDate"], OrderStatus(json["status"]),
                       json["complete"])
        else:
            return None

    @classmethod
    def store_inventory(cls):
        return cls.db.store_inventory()

    @classmethod
    def find_by_id(cls, order_id: int):
        return cls.db.store_find_order_by_id(order_id)

    def place(self):
        self.db.store_place_order(self)

    def delete(self):
        self.db.store_delete_order(self)
