from sqlalchemy import Integer , String , Boolean , Column 
from ..database import Base

class User(Base):
    __tablename__ = "users" 

    id = Column(Integer , primary_key=True)
    name = Column(String)
    email = Column(String)


    