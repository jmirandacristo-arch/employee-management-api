from fastapi import APIRouter, Depends, HTTPException
from app.infrastructure.database.database import SessionLocal
from app.presentation.schemas.employee_schema import EmployeeCreate, EmployeeResponse, EmployeeUpdate
from app.infrastructure.database.employee_repository_impl import EmployeeRepositoryImpl
from app.application.use_cases.create_employee_use_case import CreateEmployee
from app.application.use_cases.get_employee_use_case import GetEmployee
from app.application.use_cases.get_all_employees_use_case import GetAllEmployees
from app.application.use_cases.update_employee_use_case import UpdateEmployee
from app.application.use_cases.delete_employee_use_case import DeleteEmployee



router = APIRouter()

# Dependency Injection for Use Cases


# Create Employee
def create_use_case():
    session = SessionLocal()
    repository = EmployeeRepositoryImpl(session)
    return CreateEmployee(repository= repository)

# Create Employee Endpoint
@router.post("/employee", response_model= EmployeeResponse)
def create(employee_data: EmployeeCreate, use_case: CreateEmployee = Depends(create_use_case)):
    return use_case.execute(employee_data.model_dump())


# Get Employee Endpoint
def get_use_case():
    session = SessionLocal()
    repository = EmployeeRepositoryImpl(session)
    return GetEmployee(repository= repository)

# Get Employee Endpoint
@router.get("/{employee_id}", response_model= EmployeeResponse)
def get(employee_id: int, use_case: GetEmployee = Depends(get_use_case)):
    return use_case.execute(employee_id)


# Get All Employees
def get_all_use_case():
    session = SessionLocal()
    repository = EmployeeRepositoryImpl(session)
    return GetAllEmployees(repository= repository)

# Get All Employees Endpoint
@router.get("/employees", response_model= list[EmployeeResponse])
def get_all(use_case: GetAllEmployees = Depends(get_all_use_case)):
    return use_case.execute()


# Update Employee 
def update_use_case():
    session = SessionLocal()
    repository = EmployeeRepositoryImpl(session)
    return UpdateEmployee(repository=repository)

# Update Employee Endpoint
@router.put("/{employee_id}", response_model= EmployeeResponse)
def update(employee_id: int, employee_data: EmployeeUpdate, use_case: UpdateEmployee = Depends(update_use_case)):
    return use_case.execute(employee_id, employee_data.model_dump())


# Delete Employee
def delete_use_case():
    session = SessionLocal()
    repository = EmployeeRepositoryImpl(session)
    return DeleteEmployee(repository=repository)

# Delete Employee Endpoint
@router.delete("/{employee_id}", response_model= EmployeeResponse)
def delete(employee_id: int, use_case: DeleteEmployee = Depends(delete_use_case)):
    return use_case.execute(employee_id)





