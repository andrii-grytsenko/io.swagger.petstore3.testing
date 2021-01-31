from pytest import *

import config as cfg
from api.pet_store3_api import *


@fixture(scope="class")
def api():
    ps3api = PetStoreApi(cfg.API_BASE_URL)
    yield ps3api
    del ps3api
