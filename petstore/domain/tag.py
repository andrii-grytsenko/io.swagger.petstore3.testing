from alchemize import Attr

from petstore.domain.base_api_class import BaseApiClass


class Tag(BaseApiClass):
    __mapping__ = {
        "id": Attr("id", int),
        "name": Attr("name", str)
    }

    def __init__(self, tag_id=None, tag_name=None):
        self.id = tag_id
        self.name = tag_name

    def to_json(self):
        return {"id": self.id, "name": self.name}

    @staticmethod
    def from_json(json):
        if "id" in json and "name" in json:
            return Tag(json["id"], json["name"])
        else:
            return None
