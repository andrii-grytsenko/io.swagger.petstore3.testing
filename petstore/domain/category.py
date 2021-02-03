from alchemize import Attr, JsonMappedModel, JsonTransmuter
from petstore.domain.base_api_class import BaseApiClass


class Category(BaseApiClass):
    __mapping__ = {
        "id": Attr("id", int),
        "name": Attr("name", str),
    }

    def __init__(self, category_id=None, category_name=None):
        self.id = category_id
        self.name = category_name

    def to_json(self):
        return {"id": self.id, "name": self.name}

    @staticmethod
    def from_json(json):
        if "id" in json and "name" in json:
            return Category(json["id"], json["name"])
        else:
            return None

    # def __eq__(self, other):
    #     if isinstance(other, self.__class__):
    #         return JsonTransmuter.transmute_to(self) == JsonTransmuter.transmute_to(other)
    #     else:
    #         return False
