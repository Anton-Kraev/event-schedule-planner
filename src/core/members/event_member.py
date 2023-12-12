from datetime import datetime
from typing import List, Optional, Set

from .member_type import MemberType
from ..schedules.calendar_item import CalendarItem
from ..schedules.calendar_type import CalendarType


class EventMember:
    """
    Class to store and retrieve member's schedule

    Attributes
    ----------
    member_type : MemberType
        Member type
    name : str
        Member name
    calendars : List[BaseCalendar]
        List of member calendars that inherit from the abstract BaseCalendar class
    """

    def __init__(
        self, member_type: MemberType, name: str, calendar_types: Set[CalendarType]
    ):
        """
        Inits EventMember class with member's type, name and calendars

        Parameters
        ----------
        member_type : MemberType
            Member type
        name : str
            Member name
        calendar_types : Set[CalendarType]
            Multiple types of calendars used by this member
        """
        self.member_type = member_type
        self.name = name
        self.calendars = [
            calendar.value(name, member_type) for calendar in calendar_types
        ]

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
