from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    email: str
    phone_number: str
    position: str
    