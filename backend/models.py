from sqlmodel import SQLModel, Field
from typing import Optional
import datetime

class PracticeLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date
    duration_minutes: int
    notes: Optional[str] = None