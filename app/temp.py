from app.db import init_speciaity, init_insurer
from app.dependencies import get_db

res = get_db()
db1 = next(res)
# init_speciaity(db1)
# init_insurer(db1)
