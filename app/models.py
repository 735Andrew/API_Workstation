from typing import Optional
from pydantic import BaseModel, Field


class Forecast(BaseModel):
    id: Optional[int] = None
    city: str = Field(min_length=2, max_length=100)
    temperature: int = Field(gt=-100, lt=100)
