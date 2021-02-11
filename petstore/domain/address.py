from alchemize import Attr

from petstore.domain.base_api_class import BaseApiClass


class Address(BaseApiClass):
    __mapping__ = {
        "street": Attr("street", str),
        "city": Attr("city", str),
        "state": Attr("state", str),
        "zip": Attr("zip", str),
    }

    def __init__(self, street: str = None, city: str = None, state: str = None, zip_code: str = None):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip_code

    def to_json(self):
        return {"street": self.street, "city": self.city, "state": self.state, "zip": self.zip}

    @staticmethod
    def from_json(json):
        if "street" in json and "city" in json and "state" in json and "zip" in json:
            return Address(json["street"], json["city"], json["state"], json["zip"])
        else:
            return None
