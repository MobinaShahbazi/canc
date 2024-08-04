from app.db import init_speciaity, init_insurer
from app.dependencies import get_db
from app.suggestion.scoring import distance, findOptions

res = get_db()
db1 = next(res)
# init_speciaity(db1)
# init_insurer(db1)
findOptions(db1, 1, "Tehran", "15105", "47", (35.764146051683326, 51.345938636790954))
