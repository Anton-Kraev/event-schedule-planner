from dataclasses import dataclass
from datetime import datetime

from ..types import CalendarType


@dataclass
class CalendarItem:
    start_time: datetime
    end_time: datetime
    location: str
    description: str
    source: CalendarType
