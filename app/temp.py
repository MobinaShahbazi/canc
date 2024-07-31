from app.db import init_db
from app.dependencies import get_db

res = get_db()
db1 = next(res)
init_db(db1)