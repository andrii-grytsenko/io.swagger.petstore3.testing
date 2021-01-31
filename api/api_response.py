from domain.types import ApiResponseType


class ApiResponse:
    def __init__(self, code, response_type: ApiResponseType, message):
        self.code = code
        self.type = response_type
        self.message = message

    def to_json(self):
        return {"code": self.code, "type": self.type.value, "message": self.message}

    @staticmethod
    def from_json(json):
        if "code" in json and "type" in json and "message" in json:
            return ApiResponse(json["code"], json["type"], json["message"])
        else:
            return None


class ApiResponseError(Exception):
    def __init__(self, response: ApiResponse, message="Api exception"):
        self.response = response
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n{self.response.code}: [{self.response.type}] {self.response.message}"
