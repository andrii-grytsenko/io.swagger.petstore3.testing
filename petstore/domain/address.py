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
