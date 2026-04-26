from app.domain.repositories.employee_repository import EmployeeRepository
from app.domain.entities.employee import Employee
from app.infrastructure.database.models import EmployeeModel
from sqlalchemy.orm import Session
from typing import Optional


class EmployeeRepositoryImpl(EmployeeRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_employee(self, employee_data: dict):
        
        # Create an instance of EmployeeModel with the provided employee data
        employee_model = EmployeeModel(
            name = employee_data["name"],
            email= employee_data["email"],
            phone_number= employee_data["phone_number"],
            position= employee_data["position"]
        )
        
        # Check if an employee with the same email already exists
        query = self.session.query(EmployeeModel).filter(EmployeeModel.email == employee_model.email).first()
        if query is not None:
            raise ValueError("Employee with this email already exists")
        
        # Add the new employee to the session and commit the transaction
        self.session.add(employee_model)
        self.session.commit()
        self.session.refresh(employee_model)

        # Return the created employee as an instance of the Employee entity
        return Employee(
            id = employee_model.id,
            name= employee_model.name,
            email= employee_model.email,
            phone_number= employee_model.phone_number,
            position= employee_model.position
        )

    def get_employee(self, employee_id: int):

        # Query the database for an employee with the specified ID
        query = self.session.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
        
        # If an employee is found, return it as an instance of the Employee entity; otherwise, raise a ValueError
        if query is None:
            raise ValueError("Employee not found")
        
        result = Employee(
            id= query.id,
            name = query.name,
            email= query.email,
            phone_number= query.phone_number,
            position= query.position
        )
        return result
        

    def get_all_employees(self):

        # Query the database for all employee records
        query = self.session.query(EmployeeModel).all()
        
        # If employee records are found, convert them to instances of the Employee entity and return them as a list; otherwise, return an empty list
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
        
    
    def update_employee(self, employee_id: int, employee_data: dict):

        # Query the database for an employee with the specified ID
        query = self.session.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
        
        # If an employee is found, update its attributes with the provided employee data, commit the transaction, 
        # and return the updated employee as an instance of the Employee entity; otherwise, raise a ValueError indicating that the employee was not found
        if query is None:
            raise ValueError("Employee not found")
        
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

        

    def delete_employee(self, employee_id: int):
        
        # Query the database for an employee with the specified ID
        query = self.session.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
        
        # If an employee is found, delete it from the session and commit the transaction; otherwise, raise a ValueError indicating that the employee was not found
        if query is None:
            raise ValueError("Employee not found")
            
        self.session.delete(query)
        self.session.commit()