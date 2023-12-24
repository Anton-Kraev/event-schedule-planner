from enum import Enum

from .timetable import TimetableCalendar


class CalendarType(Enum):
    timetable = TimetableCalendar
