from alchemize import Attr

from petstore.domain.base_api_class import BaseApiClass
from petstore.domain.category import Category
from petstore.domain.domain_types import PetStatus
from petstore.domain.tag import Tag


class Pet(BaseApiClass):
    __mapping__ = {
        "id": Attr("id", int),
        "name": Attr("name", str),
        "category": Attr("category", Category),
        "photoUrls": Attr("photo_urls", [str]),
        "tags": Attr("tags", [Tag]),
        "status": Attr("status", PetStatus),
    }

    db = None  # database.Database()

    def __init__(self, pet_id: int = None, name: str = None, category: Category = None,
                 photo_urls: [] = None, tags: [Tag] = None, status: PetStatus = None):
        self.id = pet_id
        self.name = name
        self.category = category
        self.photo_urls = photo_urls
        self.tags = tags
        self.status = status

    def to_json(self):
        return {"id": self.id, "name": self.name, "category": self.category.to_json(),
                "photoUrls": self.photo_urls, "tags": [*map(lambda x: x.to_json(), self.tags)],
                "status": self.status.value}

    @staticmethod
    def from_json(json: str):
        if "id" in json and "name" in json and "category" in json \
                and "photoUrls" in json and "tags" in json and "status" in json:
            return Pet(json["id"], json["name"], Category.from_json(json["category"]),
                       json["photoUrls"], [*map(lambda x: Tag.from_json(x), json["tags"])],
                       PetStatus(json["status"]))
        else:
            return None

    @staticmethod
    def find_by_status(status: PetStatus):
        return Pet.db.pet_find_by_status(status)

    @staticmethod
    def find_by_tags(tag_list: [Tag]):
        return Pet.db.pet_find_by_tags(tag_list)

    @staticmethod
    def find_by_id(pet_id: int):
        return Pet.db.pet_find_by_id(pet_id)

    def update(self):
        self.db.pet_update(self)

    def add(self):
        self.db.pet_add(self)

    def update_with_form_data(self, name, status: PetStatus):
        self.db.pet_update_by_form_data(self.id, name, status)

    def delete(self, api_key: str):
        self.db.pet_delete(self.id, api_key)

    def upload_image(self, file_name: str, metadata: str):
        with open(file_name, "rb") as f:
            self.db.pet_upload_image(self.id, metadata, f)
