from abc import ABC, abstractmethod 
from app.domain.entities.employee import Employee
from typing import Optional

class EmployeeRepository(ABC):
    @abstractmethod
    def get_employee(self, employee_id: int) -> Optional[Employee]:
        # Placeholder for method to retrieve an employee by ID
        pass

    @abstractmethod
    def get_all_employees(self) -> list[Employee]:
        # Placeholder for method to retrieve all employees
        pass

    @abstractmethod
    def create_employee(self, employee_data: dict) -> Employee:
        # Placeholder for method to create a new employee
        pass
    @abstractmethod
    def update_employee(self, employee_id: int, employee_data: dict) -> Employee:
        # Placeholder for method to update an existing employee
        pass

    @abstractmethod
    def delete_employee(self, employee_id: int) -> None:
        # Placeholder for method to delete an employee by ID
        pass

    