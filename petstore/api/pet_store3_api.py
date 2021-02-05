from alchemize import JsonTransmuter
from requests import *

from petstore.api.api_response import *
from petstore.domain.order import Order
from petstore.domain.pet import Pet
from petstore.domain.tag import Tag
from petstore.domain.user import User
from petstore.domain.domain_types import *


class PetStoreApi:
    def __init__(self, base_url):
        self.base_url = base_url + ("/" if base_url[-1] != "/" else "")
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def pet_update(self, pet_obj: Pet):
        response = put(f"{self.base_url}pet",
                       headers=self.headers,
                       data=JsonTransmuter.transmute_to(pet_obj))
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, Pet) if response.ok else response.text
        )

    def pet_add(self, pet_obj: Pet):
        response = post(f"{self.base_url}pet",
                        headers=self.headers,
                        data=JsonTransmuter.transmute_to(pet_obj))
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, Pet) if response.ok else response.text
        )

    def pet_find_by_status(self, status: PetStatus):
        response = get(f"{self.base_url}pet/findByStatus",
                       headers=self.headers,
                       params={"status": status.value})
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            list(map(lambda x: JsonTransmuter.transmute_from(x, Pet), response.json()))
            if response.ok else response.text
        )

    def pet_find_by_tags(self, tags: [Tag]):
        tag_list = "" if len(tags) == 0 else "&tags=".join(list(map(lambda x: x.name, tags)))
        response = get(f"{self.base_url}pet/findByTags?tags={tag_list}",
                       headers=self.headers,
                       # params={"tags": list(map(JsonTransmuter.transmute_to, tags))}
                       )
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            list(map(lambda x: JsonTransmuter.transmute_from(x, Pet), response.json()))
            if response.ok else response.text
        )

    def pet_find_by_id(self, pet_id):
        response = get(f"{self.base_url}pet/{pet_id}",
                       headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, Pet)
            if response.ok else response.text
        )

    def pet_update_by_form_data(self, pet_id, name, status: PetStatus):
        response = post(f"{self.base_url}pet/{pet_id}",
                        headers=self.headers,
                        params={"name": name, "status": status.value})
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, Pet) if response.ok else response.text
        )

    def pet_delete(self, pet_id, api_key):
        headers_ = self.headers.copy()
        headers_["api_key"] = str(api_key)
        response = delete(f"{self.base_url}pet/{pet_id}",
                          headers=headers_)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            response.text
        )

    def pet_upload_image(self, pet_id, metadata, image):
        headers_ = self.headers.copy()
        headers_["Content-Type"] = "application/octet-stream"
        response = post(f"{self.base_url}pet/{pet_id}/uploadImage",
                        headers=headers_,
                        params={"additionalMetadata": metadata},
                        data=image)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, Pet) if response.ok else response.text
        )

    def store_inventory(self):
        response = get(f"{self.base_url}store/inventory",
                       headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            response.json() if response.ok else response.text
        )

    def store_place_order(self, order: Order):
        response = post(f"{self.base_url}store/order",
                        headers=self.headers,
                        data=JsonTransmuter.transmute_to(order))
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, Order) if response.ok else response.text
        )

    def store_find_order_by_id(self, order_id):
        response = get(f"{self.base_url}store/order/{order_id}",
                       headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, Order) if response.ok else response.text
        )

    def store_delete_order(self, order_id):
        response = delete(f"{self.base_url}store/order/{order_id}",
                          headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            response.text
        )

    def user_create(self, user: User):
        response = post(f"{self.base_url}user",
                        headers=self.headers,
                        data=JsonTransmuter.transmute_to(user))
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, User) if response.ok else response.text
        )

    def user_create_with_list(self, user_list: [User]):
        response = post(f"{self.base_url}createWithList",
                        headers=self.headers,
                        data=str(list(map(JsonTransmuter.transmute_to, user_list))))
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            list(map(
                lambda x: JsonTransmuter.transmute_from(response.text, User), response.json()
            )) if response.ok else response.text
        )

    def user_login(self, user_name, password):
        response = get(f"{self.base_url}user/login",
                       headers=self.headers,
                       params={"username": user_name, "password": password})
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            response.text
        )

    def user_logout(self):
        response = get(f"{self.base_url}user/logout",
                       headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            response.text
        )

    def user_find_by_name(self, user_name):
        response = get(f"{self.base_url}user/{user_name}",
                       headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, User) if response.ok else response.text
        )

    def user_update(self, user_name, user: User):
        response = put(f"{self.base_url}user/{user_name}",
                       headers=self.headers,
                       data=JsonTransmuter.transmute_to(user))
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.text, User) if response.ok else response.text
        )

    def user_delete(self, user_name):
        response = delete(f"{self.base_url}user/{user_name}",
                          headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            response.text
        )
