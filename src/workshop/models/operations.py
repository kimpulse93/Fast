from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional
from decimal import Decimal


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'
class Operation(BaseModel):
    id: int
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]

