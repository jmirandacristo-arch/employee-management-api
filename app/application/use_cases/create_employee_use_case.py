from app.domain.repositories.employee_repository import EmployeeRepository
from app.domain.entities.employee import Employee

class CreateEmployee:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository
    
    def execute(self, employee_data: dict):
        return self.repository.create_employee(employee_data)
        