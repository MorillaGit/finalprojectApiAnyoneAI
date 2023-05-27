from pydantic import BaseModel

class CreditInfo(BaseModel):
    age: int
    income: float
    credit_score: int
    debt: float

class Prediction(BaseModel):
    probability: float
    class_: str
