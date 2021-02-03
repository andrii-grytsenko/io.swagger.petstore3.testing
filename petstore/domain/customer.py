from alchemize import Attr, JsonMappedModel, JsonTransmuter
from petstore.domain.base_api_class import BaseApiClass
from petstore.domain.address import Address


class Customer(BaseApiClass):
    __mapping__ = {
        "id": Attr("id", int),
        "username": Attr("user_name", str),
        "address": Attr("address", Address)
    }

    def __init__(self, customer_id, user_name, address: Address):
        self.id = customer_id
        self.user_name = user_name
        self.address = address

    def to_json(self):
        return {"id": self.id, "username": self.user_name, "address": self.address.to_json()}

    @staticmethod
    def from_json(json):
        if "id" in json and "username" in json and "address" in json:
            return Customer(json["id"], json["username"], Address.from_json(json["address"]))
        else:
            return None

    # def __eq__(self, other):
    #     if isinstance(other, self.__class__):
    #         return JsonTransmuter.transmute_to(self) == JsonTransmuter.transmute_to(other)
    #     else:
    #         return False
