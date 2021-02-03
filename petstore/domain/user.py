from alchemize import Attr, JsonMappedModel, JsonTransmuter
from petstore.domain.base_api_class import BaseApiClass
from petstore.domain.domain_types import UserStatus


class User(BaseApiClass):
    __mapping__ = {
        "id": Attr("id", int),
        "name": Attr("user_name", str),
        "firstName": Attr("first_name", str),
        "lastName": Attr("last_name", str),
        "email": Attr("email", str),
        "password": Attr("password", str),
        "phone": Attr("phone", str),
        "userStatus": Attr("user_status", UserStatus),
    }

    db = None # database.Database()

    def __init__(self, user_id=None, user_name=None, first_name=None, last_name=None,
                 email=None, password=None, phone=None, user_status: UserStatus=None):
        self.id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.user_status = user_status

    def to_json(self):
        return {"id": self.id, "username": self.user_name,
                "firstName": self.first_name, "lastName": self.last_name,
                "email": self.email, "password": self.password,
                "phone": self.phone, "status": self.user_status.value}

    @staticmethod
    def from_json(json):
        if "id" in json and "username" in json \
                and "firstName" in json and "lastName" in json \
                and "email" in json and "password" in json \
                and "phone" in json and "status" in json:
            return User(json["id"], json["username"], json["firstName"],
                        json["lastName"], json["email"], json["password"],
                        json["phone"], UserStatus(json["status"]))
        else:
            return None

    # def __eq__(self, other):
    #     if isinstance(other, self.__class__):
    #         return JsonTransmuter.transmute_to(self) == JsonTransmuter.transmute_to(other)
    #     else:
    #         return False

    @staticmethod
    def create_with_list(user_list: []): User.db.user_create_with_list(user_list)

    @staticmethod
    def get_by_name(name): return User.db.user_find_by_name(name)

    def create(self): self.db.user_create(*(self.to_json().values()))

    def login(self): self.db.user_login(self.user_name, self.password)

    def logout(self): self.db.user_logout()

    def update(self, new_user): self.db.user_update(new_user, self)

    def delete(self): self.db.user_delete(self.user_name)
