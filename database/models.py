from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import engine

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

# Create the table in the database
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Create a session
session = Session()