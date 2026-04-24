from app.domain.repositories.employee_repository import EmployeeRepository
from app.domain.entities.employee import Employee


class GetEmployee:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository
    
    def execute(self, employee_id: int):
        return self.repository.get_employee(employee_id)

