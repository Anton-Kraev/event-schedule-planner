from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimetableCalendarItem:
    start_time: datetime
    end_time: datetime
    location: str
    description: str
