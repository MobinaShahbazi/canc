from app.db import init_Speciaity, init_Insurer, init_Doctor, init_Medical_Center
from app.dependencies import get_db
from app.suggestion.scoring2 import distance, findOptions

res = get_db()
db1 = next(res)
# init_Speciaity(db1)
# init_Insurer(db1)
# init_Doctor(db1)
# init_Medical_Center(db1)
findOptions(db1, "تهران", "تهران", "20175", "47", (35.764146051683326, 51.345938636790954))
