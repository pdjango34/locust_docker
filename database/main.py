from models import session as db
from  models import User

users = db.query(User).all()
for user in users:
    print(user)