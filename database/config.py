import os
from sqlalchemy import create_engine


DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:root@localhost/test_db")

engine = create_engine(DATABASE_URL, echo=True)
