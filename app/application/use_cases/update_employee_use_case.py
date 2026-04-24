from app.domain.repositories.employee_repository import EmployeeRepository
from app.domain.entities.employee import Employee

class UpdateEmployee:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def execute(self, employee_id: int, employee_data: dict):
        return self.repository.update_employee(employee_id, employee_data)