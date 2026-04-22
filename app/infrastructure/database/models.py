from sqlalchemy import Column, Integer, String
from app.infrastructure.database.database import Base

class EmployeeModel(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    position = Column(String, nullable=False)