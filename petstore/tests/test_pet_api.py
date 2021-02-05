from alchemize import JsonTransmuter
from pytest import mark

from petstore.api.api_response import ApiResponseType
from petstore.domain.pet import Pet
from petstore.domain.tag import Tag


class TestPetApi:

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

    @mark.order(5)
    def test_pet_find_by_tags(self, api, logger, dp_pet_tag):
        logger.info("Test case for finding pet by tags list")
        tag_list = list(map(lambda x: JsonTransmuter.transmute_from(x, Tag), dp_pet_tag[0]))
        response = api.pet_find_by_tags(tag_list)
        assert response.code == dp_pet_tag[1]
        assert response.type == ApiResponseType.ok
        # assert all(lambda x: x.tag.name == "tag1" and x.tag.id == 1 for x in response)
        logger.info("PASSED")

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


if __name__ == "__main__":
    pass
