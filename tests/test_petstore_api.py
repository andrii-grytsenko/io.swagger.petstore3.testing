from pytest import *

from domain.category import Category
from domain.order import Order
from domain.pet import Pet
from domain.tag import Tag
from domain.types import *
from domain.user import User


class TestPetStoreApi:

    #@mark.skip
    def test_pet_add(self, api):
        pet = Pet(1, "Dog", Category(1, "Dogs"), [], [Tag(1, "tag1")], PetStatus.available)
        response = api.pet_add(pet)
        assert response.id == pet.id, f"Error in ID {response.id}"
        assert response.name == pet.name, f"Error in ID {response.name}"

    #@mark.skip
    def test_pet_update(self, api):
        pet = Pet(1, "Dog", Category(1, "Dogs"), [], [Tag(1, "tag1")], PetStatus.available)
        response = api.pet_update(pet)
        assert response.id == pet.id, f"Error in ID {response.id}"
        assert response.name == pet.name, f"Error in ID {response.name}"

    #@mark.skip
    def test_pet_find_by_id(self, api):
        response = api.pet_find_by_id(1)
        assert response.id == 1, f"Error in ID {response.id}"
        assert response.name == "Dog", f"Error in ID {response.name}"

    #@mark.skip
    def test_pet_find_by_status(self, api):
        response = api.pet_find_by_status(PetStatus.sold)
        assert all(lambda x: x.status == PetStatus.sold for x in response), \
            f"Status code {response.status_code}\nResponse {response.text}\n"

    #@mark.skip
    def test_pet_find_by_tags(self, api):
        response = api.pet_find_by_tags([Tag(1, "tag1")])
        assert all(lambda x: x.tag.name == "tag1" and x.tag.id == 1 for x in response), \
            f"Status code {response.status_code}\nResponse {response.text}\n"

    #@mark.skip
    def test_pet_update_by_form_data(self, api):
        response = api.pet_update_by_form_data(1, "name", PetStatus.pending)
        assert response.id == 1, f"Error in ID {response.id}"
        assert response.name == "name", f"Error in ID {response.name}"
        assert response.status == PetStatus.pending, f"Error in ID {response.name}"

    #@mark.skip
    def test_pet_upload_image(self, api):
        response = api.pet_upload_image(10, "metadata", b"binary-data")
        assert response.id == 10, f"Error in ID {response.id}"

    #@mark.skip
    def test_pet_delete(self, api):
        response = api.pet_delete(1, 123456)
        assert response, f"Error id=n response {response}\n"

    #@mark.skip
    def test_store_inventory(self, api):
        response = api.store_inventory()
        assert response.ok, f"Status code {response.status_code}\nResponse {response.text}\n"

    #@mark.skip
    def test_store_place_order(self, api):
        order = Order(10, 198772, 7, "2021-01-14T18:47:45.870+00:00", OrderStatus.approved, True)
        response = api.store_place_order(order)
        assert response.id == order.id, f"Error in ID {response.id}\n"
        assert response.pet_id == order.pet_id, f"Error in PetID {response.pet_id}\n"
        assert response.quantity == order.quantity, f"Error in quantity {response.quantity}\n"

    #@mark.skip
    def test_store_find_order_by_id(self, api):
        response = api.store_find_order_by_id(1)
        assert response.id == 1, f"Error in ID {response.id}\n"

    #@mark.skip
    def test_store_delete_order(self, api):
        response = api.store_delete_order(999999)
        assert response, f"Status code {response.status_code}\nResponse {response.text}\n"

    #@mark.skip
    def test_user_create(self, api):
        data = User(125, "userName", "firstName", "lastName", "e@ma.il", "password", "phone", UserStatus.registered)
        response = api.user_create(data)
        assert response.id == data.id, f"Error in ID {response.id}\n"
        assert response.name == data.name, f"Error in ID {response.name}\n"
        assert response.first_name == data.first_name, f"Error in ID {response.first_name}\n"
        assert response.last_name == data.last_name, f"Error in ID {response.last_name}\n"
        assert response.email == data.email, f"Error in ID {response.email}\n"

    #@mark.skip
    def test_user_create_with_list(self, api):
        data1 = User(1251, "userName1", "firstName1", "lastName1", "e@ma.il", "password", "phone",
                     UserStatus.registered)
        data2 = User(1252, "userName2", "firstName2", "lastName2", "e@ma.il", "password", "phone",
                     UserStatus.registered)
        response = api.user_create_with_list([data1, data2])
        assert len(response) == 2, f"Error adding users"

    #@mark.skip
    def test_user_login(self, api):
        data = User(125, "userName", "firstName", "lastName", "e@ma.il", "password", "phone", UserStatus.registered)
        response = api.user_login(data.user_name, data.password)
        assert response.startswith("Logged in user session"), f"Something wrong {response}"

    #@mark.skip
    def test_user_logout(self, api):
        response = api.user_logout()
        assert response, f"Something wrong {response}\n"

    #@mark.skip
    def test_user_find_by_name(self, api):
        data = User(10, "theUser", "John", "James", "john@email.com", "12345", "12345", UserStatus.registered)
        response = api.user_find_by_name(data.user_name)
        assert response.user_name == data.user_name, f"Error in user name {response.user_name}\n"

    #@mark.skip
    def test_user_update(self, api):
        data = User(10, "theUser", "John", "James", "john@email.com", "12345", "12345", UserStatus.registered)
        data2 = User(10, "theUser", "User", "User", "john@email.com", "12345", "12345", UserStatus.registered)
        response = api.user_update(data.user_name, data2)
        assert response.first_name == data2.first_name, f"Error in First name {response.first_name}\n"

    #@mark.skip
    def test_user_delete(self, api):
        data = User(10, "theUser", "John", "James", "john@email.com", "12345", "12345", UserStatus.registered)
        response = api.user_delete(data.user_name)
        assert response, f"Something wrong {response}\n"


if __name__ == "__main__":
    pass
