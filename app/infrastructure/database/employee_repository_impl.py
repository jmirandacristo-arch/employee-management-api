from app.domain.repositories.employee_repository import EmployeeRepository
from app.domain.entities.employee import Employee
from app.infrastructure.database.models import EmployeeModel
from sqlalchemy.orm import Session
from typing import Optional


class EmployeeRepositoryImpl(EmployeeRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_employee(self, employee_id: int):
        query = self.session.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()

        if query is not None:
            result = Employee(
                id= query.id,
                name = query.name,
                email= query.email,
                phone_number= query.phone_number,
                position= query.position

            )
            return result
        return None

    def get_all_employees(self):
        query = self.session.query(EmployeeModel).all()
        
        employees = []
        if query is not None:
            for result in query:

                employee = Employee(
                id= result.id,
                name = result.name,
                email= result.email,
                phone_number= result.phone_number,
                position= result.position
                )
                employees.append(employee)
            return employees

        return []
        
    def create_employee(self, employee_data: dict):

        employee = Employee(
            name = employee_data["name"],
            email= employee_data["email"],
            phone_number= employee_data["phone_number"],
            position= employee_data["position"]

        )

        employee_model = EmployeeModel(
            name = employee.name,
            email = employee.email,
            phone_number = employee.phone_number,
            position = employee.position,
        )
        
        self.session.add(employee_model)
        self.session.commit()
        self.session.refresh(employee_model)

    
        return Employee(
            id = employee_model.id,
            name= employee_model.name,
            email= employee_model.email,
            phone_number= employee_model.phone_number,
            position= employee_model.position
        )
    
    def update_employee(self, employee_id: int, employee_data: dict):

        query = self.session.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()

        if query is not None:
            if employee_data.get("name"):
                query.name = employee_data["name"]
            if employee_data.get("email"):
                query.email = employee_data["email"]
            if employee_data.get("phone_number"):
                query.phone_number = employee_data["phone_number"]
            if employee_data.get("position"):
                query.position = employee_data["position"]
            
            self.session.commit()
            self.session.refresh(query)
            
            return Employee(
                id=query.id,
                name=query.name,
                email=query.email,
                phone_number=query.phone_number,
                position=query.position
            )

        return None

    def delete_employee(self, employee_id: int):
        pass