# Employee Management API

REST API for managing employees built with FastAPI and PostgreSQL following Clean Architecture principles.

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## Installation

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your database connection:
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/employee_management
   
6. Run the server:
```bash
python -m uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /employee | Create a new employee |
| GET | /employees | Get all employees |
| GET | /{employee_id} | Get employee by ID |
| PUT | /{employee_id} | Update employee |
| DELETE | /{employee_id} | Delete employee |

## Documentation
API documentation available at `http://localhost:8000/docs`
