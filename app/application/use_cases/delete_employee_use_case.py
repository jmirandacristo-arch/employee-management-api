from app.domain.repositories.employee_repository import EmployeeRepository
from app.domain.entities.employee import Employee

class DeleteEmployee:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository
    
    def execute(self, employee_id: int):
        return self.repository.delete_employee(employee_id)