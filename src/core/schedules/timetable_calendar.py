from datetime import datetime
from typing import List

from .base_calendar import BaseCalendar
from .calendar_item import CalendarItem


class TimetableCalendar(BaseCalendar):
    def _upload(self) -> ...:
        ...

    def _standardize(self, external_calendar: ...) -> List[CalendarItem]:
        ...

    def _latest_update(self) -> datetime:
        ...
