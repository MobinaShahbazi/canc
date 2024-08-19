from app.dependencies import get_db
from . import APIBaseClass
from ..suggestion.scoring2 import findOptions


class OtherDAO(APIBaseClass):

    def __init__(self):
        super().__init__()

        self.router.add_api_route('/Recom', self.score, methods=['POST'], tags=['Other'])

    def score(self):  # body input
        res = get_db()
        db1 = next(res)
        # result = findOptions(db1, "تهران", "تهران", "20175", "47", (35.764146051683326, 51.345938636790954))
        result = findOptions(db1, "اصفهان", "نحف آباد", "20175", "47", (32.60594419355762, 51.379261001578506))
        result = result[:6]
        return result

