from  pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional
from decimal import Decimal

class Operation(BaseModel):
    id: int
    date: date
    kind: E
    amount: Decimal
    description: Optional[str]

