from abc import ABC
from datetime import datetime
from typing import List, Optional

from ..schedules.base_calendar import BaseCalendar
from ..schedules.calendar_item import CalendarItem


class BaseMember(ABC):
    """
    An abstract base class for implementing classes of
    event participants to store and retrieve their schedules

    Attributes
    ----------
    name : str
        Member name
    calendars : List[BaseCalendar]
        List of member calendars that inherit from the abstract BaseCalendar class
    """

    def __init__(self, name: str, calendars: List[BaseCalendar]):
        """
        Inits BaseMember class with member's name and calendars

        Parameters
        ----------
        name : str
            Member name
        calendars : List[BaseCalendar]
            List of member calendars that inherit from the abstract BaseCalendar class
        """
        self.name = name
        self.calendars = calendars

    def actualize_schedule(self) -> None:
        """
        Actualize all member calendars
        """
        for calendar in self.calendars:
            calendar.actualize()

    @property
    def schedule(self) -> List[CalendarItem]:
        """
        All calendars combined into one
        """
        reserved_slots = [
            calendar.reserved_slots
            for calendar in self.calendars
            if calendar.reserved_slots is not None
        ]
        return sum(reserved_slots, [])

    @property
    def latest_upload(self) -> Optional[datetime]:
        """
        The oldest update time among all calendars,
        or None if one of calendars has never been uploaded
        """
        latest_times = [calendar.latest_upload for calendar in self.calendars]
        return None if None in latest_times else min(latest_times)  # pyright: ignore
