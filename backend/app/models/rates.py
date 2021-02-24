from datetime import date

from pydantic.main import BaseModel

class Rate (BaseModel):
    symbol: str
    rate: float
    date: date