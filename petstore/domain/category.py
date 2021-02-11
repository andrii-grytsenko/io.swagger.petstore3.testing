from alchemize import Attr

from petstore.domain.base_api_class import BaseApiClass


class Category(BaseApiClass):
    __mapping__ = {
        "id": Attr("id", int),
        "name": Attr("name", str),
    }

    def __init__(self, category_id: int = None, category_name: str = None):
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
