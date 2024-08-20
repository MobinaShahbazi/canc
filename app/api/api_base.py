from fastapi import APIRouter
from abc import ABCMeta


# Base class for creating APIs
class APIBaseClass(metaclass=ABCMeta):

    def __init__(self):
        self.router = APIRouter()
