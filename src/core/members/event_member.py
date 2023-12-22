from typing import List, Set

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

    @property
    async def schedule(self) -> List[CalendarItem]:
        """
        All calendars combined into one
        """
        return sum(
            [await calendar.get_reserved_slots() for calendar in self.calendars], []
        )
