from alchemize import Attr

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

    def __init__(self, user_id: int = None, user_name: str = None, first_name: str = None, last_name: str = None,
                 email: str = None, password: str = None, phone: str = None, user_status: UserStatus = None):
        self.id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.user_status = user_status
