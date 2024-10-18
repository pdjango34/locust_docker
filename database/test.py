from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the connection string
DATABASE_URL = "mysql+pymysql://root:root@localhost/test_db"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a model class (table structure)
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

# Create the table in the database
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Example: Adding a new user to the table
# new_user = User(name="John Doe", email="john.doe@example.com")
# session.add(new_user)
# session.commit()

# Querying the table
users = session.query(User).all()
for user in users:
    print(user)