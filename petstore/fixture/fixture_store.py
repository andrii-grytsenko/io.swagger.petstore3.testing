from pytest import *

from petstore.test_datasets.store_data import *


@fixture(params=order_place, ids=order_place_ids)
def dp_order_place(request):
    return request.param


@fixture(params=order_find, ids=order_find_ids)
def dp_order_find(request):
    return request.param


@fixture(params=order_delete, ids=order_delete_ids)
def dp_order_delete(request):
    return request.param
