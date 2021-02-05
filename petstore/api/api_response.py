from enum import Enum


class ApiResponseType(Enum):
    error = "Error"
    warning = "Warning"
    info = "Info"
    ok = "OK"
    too_busy = "Too busy"


class ApiResponse:
    def __init__(self, code, response_type: ApiResponseType, message):
        self.code = code
        self.type = response_type
        self.message = message


class ApiResponseError(Exception):
    def __init__(self, response: ApiResponse, message="Api exception"):
        self.response = response
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n{self.response.code}: [{self.response.type}] {self.response.message}"
