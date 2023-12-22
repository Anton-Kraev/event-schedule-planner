from enum import Enum

from .timetable.timetable_calendar import TimetableCalendar


class CalendarType(Enum):
    timetable = TimetableCalendar
