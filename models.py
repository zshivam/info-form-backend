from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel
from sqlalchemy import create_engine

class FormData(Base):
    __tablename__ = "formdata"
    __allow_unmapped__ = True


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    contact = Column(String, index=True)
    image = Column(String, nullable=False)
    
