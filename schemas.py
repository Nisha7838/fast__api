from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    age: int
    phone: str   # mandatory by default

class PatientResponse(PatientCreate):
    id: int

    class Config:
        orm_mode = True  # userd to work with ORM objects
