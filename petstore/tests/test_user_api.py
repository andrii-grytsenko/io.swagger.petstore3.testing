from pytest import mark
from petstore.domain.category import Category
from petstore.domain.order import Order
from petstore.domain.pet import Pet
from petstore.domain.tag import Tag
from petstore.domain.user import User
from petstore.domain.domain_types import *
from alchemize import JsonTransmuter


class TestUserApi:

    @mark.order(2)
    def test_pet_update(self, api, dp_pet_update, logger):
        _pet = JsonTransmuter.transmute_from(dp_pet_update[0], Pet)
        logger.info("Test case for updating pet to the store")
        response = api.pet_update(_pet)
        assert response.code == dp_pet_update[1]
        assert response.type == ApiResponseType.ok
        assert _pet == response.message
        logger.info(f"Pet with ID={_pet.id} was updated.")
        response = api.pet_find_by_id(_pet.id)
        assert response.type == ApiResponseType.ok
        assert response.message == _pet
        logger.info("Test PASSED")

    @mark.order(1)
    def test_pet_add(self, api, dp_pet_add, logger):
        _pet = JsonTransmuter.transmute_from(dp_pet_add[0], Pet)
        logger.info(f"Test case for adding pet with ID={_pet.id}")
        response = api.pet_add(_pet)
        assert response.code == dp_pet_add[1]
        assert response.type == ApiResponseType.ok
        assert _pet == response.message
        logger.info(f"Pet with ID={_pet.id} was added.")
        response = api.pet_find_by_id(_pet.id)
        assert response.type == ApiResponseType.ok
        assert response.message == _pet
        logger.info("Test PASSED")

    @mark.order(3)
    def test_pet_find_by_id(self, api, dp_pet_id, logger):
        _pet = JsonTransmuter.transmute_from(dp_pet_id[1], Pet) if dp_pet_id[2] == 200 else None
        logger.info(f"Test case for finding pet by ID={dp_pet_id[0]}")
        response = api.pet_find_by_id(dp_pet_id[0])
        assert response.code == dp_pet_id[2]
        if response.type == ApiResponseType.ok:
            assert _pet == response.message
        else:
            assert response.message == dp_pet_id[1]
        logger.info("Test PASSED")

    @mark.order(4)
    def test_pet_find_by_status(self, api, logger, dp_pet_status):
        logger.info(f"Test case for finding pet by status [{dp_pet_status[0].value}]")
        response = api.pet_find_by_status(dp_pet_status[0])
        assert response.code == dp_pet_status[1]
        assert response.type == ApiResponseType.ok
        assert all(lambda x: x.status == dp_pet_status[0] for x in response.message)
        logger.info("Test PASSED")

    #@mark.order(5)
    @mark.skip
    def test_pet_find_by_tags(self, api, logger, dp_pet_tag):
        logger.info("Test case for finding pet by tags list")
        tag_list = list(map(lambda x: JsonTransmuter.transmute_from(x, Pet), dp_pet_tag[0]))
        response = api.pet_find_by_tags(tag_list)
        assert response.code == dp_pet_tag[1]
        assert response.type == ApiResponseType.ok
        assert all(lambda x: x.tag.name == "tag1" and x.tag.id == 1 for x in response)
        logger.info("PASSED")

    #@mark.skip
    @mark.order(6)
    def test_pet_update_by_form_data(self, api, logger, dp_pet_update_by_form):
        _pet = JsonTransmuter.transmute_from(dp_pet_update_by_form[0], Pet)
        logger.info(f"Test case for updating pet by form data, ID={_pet.id}")
        response = api.pet_update_by_form_data(_pet.id, dp_pet_update_by_form[1], dp_pet_update_by_form[2])
        assert response.code == dp_pet_update_by_form[3]
        assert response.type == ApiResponseType.ok
        assert response.message == _pet
        logger.info(f"Pet with ID={_pet.id} was updated.")
        response = api.pet_find_by_id(_pet.id)
        assert response.type == ApiResponseType.ok
        assert response.message == _pet
        logger.info("Test PASSED")

    @mark.order(7)
    def test_pet_upload_image(self, api, logger, dp_pet_upload):
        logger.info(f"Test case for uploading image data, ID={dp_pet_upload[0]}")
        response = api.pet_upload_image(dp_pet_upload[0], dp_pet_upload[1], dp_pet_upload[2])
        assert response.code == dp_pet_upload[3]
        assert response.type == ApiResponseType.ok
        logger.info("Test PASSED")

    @mark.order(8)
    def test_pet_delete(self, api, logger, dp_pet_delete):
        logger.info(f"Test case for deleting pet ID={dp_pet_delete[0]}")
        response = api.pet_delete(dp_pet_delete[0], dp_pet_delete[1])
        assert response.code == dp_pet_delete[2]
        assert response.type == ApiResponseType.ok
        assert response.message == "Pet deleted"
        logger.info(f"Pet with ID={dp_pet_delete[0]} was deleted")
        response = api.pet_find_by_id(dp_pet_delete[0])
        assert response.type == ApiResponseType.error
        assert response.code == 404
        assert response.message == "Pet not found"
        logger.info("Test PASSED")

    @mark.skip
    def test_store_inventory(self, api, logger):
        response = api.store_inventory()
        assert response.code == 200
        assert response.type == ApiResponseType.ok

    @mark.skip
    def test_store_place_order(self, api, logger):
        order = Order(10, 198772, 7, "2021-01-14T18:47:45.870+00:00", OrderStatus.approved, True)
        response = api.store_place_order(order)
        assert response.code == 200
        assert response.type == ApiResponseType.ok

    @mark.skip
    def test_store_find_order_by_id(self, api, logger):
        response = api.store_find_order_by_id(1)
        assert response.code == 200
        assert response.type == ApiResponseType.ok

    @mark.skip
    def test_store_delete_order(self, api, logger):
        response = api.store_delete_order(999999)
        assert response.code == 200
        assert response.type == ApiResponseType.ok

    @mark.skip
    def test_user_create(self, api, logger):
        data = User(125, "userName", "firstName", "lastName", "e@ma.il", "password", "phone", UserStatus.registered)
        response = api.user_create(data)
        assert response.code == 200
        assert response.type == ApiResponseType.ok

    @mark.skip
    def test_user_create_with_list(self, api, logger):
        data1 = User(1251, "userName1", "firstName1", "lastName1", "e@ma.il", "password", "phone",
                     UserStatus.registered)
        data2 = User(1252, "userName2", "firstName2", "lastName2", "e@ma.il", "password", "phone",
                     UserStatus.registered)
        response = api.user_create_with_list([data1, data2])
        assert len(response) == 2, f"Error adding users"

    @mark.skip
    def test_user_login(self, api, logger):
        data = User(125, "userName", "firstName", "lastName", "e@ma.il", "password", "phone", UserStatus.registered)
        response = api.user_login(data.user_name, data.password)
        assert response.code == 200
        assert response.type == ApiResponseType.ok

    @mark.skip
    def test_user_logout(self, api, logger):
        response = api.user_logout()
        assert response.code == 200
        assert response.type == ApiResponseType.ok

    @mark.skip
    def test_user_find_by_name(self, api, logger):
        data = User(10, "theUser", "John", "James", "john@email.com", "12345", "12345", UserStatus.registered)
        response = api.user_find_by_name(data.user_name)
        assert response.user_name == data.user_name, f"Error in user name {response.user_name}\n"

    @mark.skip
    def test_user_update(self, api, logger):
        data = User(10, "theUser", "John", "James", "john@email.com", "12345", "12345", UserStatus.registered)
        data2 = User(10, "theUser", "User", "User", "john@email.com", "12345", "12345", UserStatus.registered)
        response = api.user_update(data.user_name, data2)
        assert response.code == 200
        assert response.type == ApiResponseType.ok
        assert response.first_name == data2.first_name, f"Error in First name {response.first_name}\n"

    @mark.skip
    def test_user_delete(self, api, logger):
        data = User(10, "theUser", "John", "James", "john@email.com", "12345", "12345", UserStatus.registered)
        response = api.user_delete(data.user_name)
        assert response.code == 200
        assert response.type == ApiResponseType.ok


if __name__ == "__main__":
    pass
