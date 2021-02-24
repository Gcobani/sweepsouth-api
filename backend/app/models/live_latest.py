from pydantic.main import BaseModel

class Latest (BaseModel):
    base_currency: str
    currency: str