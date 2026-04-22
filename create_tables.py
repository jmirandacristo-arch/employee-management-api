from app.infrastructure.database.database import engine, Base
from app.infrastructure.database.models import EmployeeModel

Base.metadata.create_all(bind=engine)
print("Tables created successfully")