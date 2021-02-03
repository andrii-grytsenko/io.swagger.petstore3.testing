from pytest import *

from petstore.test_datasets.pet_data import *


@fixture(params=pet_add, ids=pet_add_ids)
def dp_pet_add(request):
    return request.param


@fixture(params=pet_update, ids=pet_update_ids)
def dp_pet_update(request):
    return request.param


@fixture(params=pet_id, ids=pet_id_ids)
def dp_pet_id(request):
    return request.param


@fixture(params=pet_status, ids=pet_status_ids)
def dp_pet_status(request):
    return request.param


@fixture(params=pet_tag, ids=pet_tag_ids)
def dp_pet_tag(request):
    return request.param


@fixture(params=pet_update_by_form, ids=pet_update_by_form_ids)
def dp_pet_update_by_form(request):
    return request.param


@fixture(params=pet_upload, ids=pet_upload_ids)
def dp_pet_upload(request):
    return request.param


@fixture(params=pet_delete, ids=pet_delete_ids)
def dp_pet_delete(request):
    return request.param
