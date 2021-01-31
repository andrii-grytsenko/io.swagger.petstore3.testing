from alchemize import Attr, JsonMappedModel
from domain.types import OrderStatus


class Order(JsonMappedModel):
    __mapping__ = {
        "id": Attr("id", int),
        "petId": Attr("pet_id", int),
        "quantity": Attr("quantity", int),
        "shipDate": Attr("ship_date", str),
        "status": Attr("status", OrderStatus),
        "complete": Attr("complete", bool),
    }

    db = None # database.Database()

    def __init__(self, order_id=None, pet_id=None, quantity=None, ship_date=None, status: OrderStatus=None, complete=None):
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

    @staticmethod
    def from_json(json):
        if "id" in json and "petId" in json \
                and "quantity" in json and "shipDate" in json \
                and "status" in json and "complete" in json:
            return Order(json["id"], json["petId"], json["quantity"],
                         json["shipDate"], OrderStatus(json["status"]),
                         json["complete"])
        else:
            return None

    @staticmethod
    def store_inventory(): return Order.db.store_inventory()

    @staticmethod
    def find_by_id(order_id): return Order.db.store_find_order_by_id(order_id)

    def place(self): self.db.store_place_order(self)

    def delete(self): self.db.store_delete_order(self)
