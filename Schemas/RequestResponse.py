from typing import Self
from dataclasses import dataclass

@dataclass
class RequestResponse:
    hasError: bool
    message: str
    statusCode: int
    data: object

    def __init__(self: Self, hasError: bool = False, message: str = "Requisição processada com sucesso!", statusCode: int = 200, data : object = {}):
        self.hasError = hasError
        self.message = message
        self.statusCode = statusCode
        self.data = data
