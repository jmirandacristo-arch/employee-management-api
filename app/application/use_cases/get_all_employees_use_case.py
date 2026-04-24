from app.domain.repositories.employee_repository import EmployeeRepository
from app.domain.entities.employee import Employee


class GetAllEmployees:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all_employees()
