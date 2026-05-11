from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = 'Deviji'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt =10, default = 5, description ='A decimal value representing the cgpa of the student')

new_student = {'age': '20', 'email': 'abc@com'} # Does implicit conversion this is called Type Coercing

student = Student(**new_student)

print((student))