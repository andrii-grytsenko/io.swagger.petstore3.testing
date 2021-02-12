from abc import ABC, abstractmethod

from alchemize import JsonMappedModel, JsonTransmuter


class BaseApiClass(JsonMappedModel, ABC):
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return JsonTransmuter.transmute_to(self) == JsonTransmuter.transmute_to(other)
        else:
            return False
