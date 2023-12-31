from typing import List, Set

from ..schedules import CalendarItem
from ..schedules.timetable import TimetableCalendar
from ..types import MemberType, CalendarType


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
        calendars = []
        for c_type in calendar_types:
            match c_type:
                case CalendarType.timetable:
                    calendars.append(TimetableCalendar(name, member_type))
        self.calendars = calendars

    @property
    async def schedule(self) -> List[CalendarItem]:
        """
        All calendars combined into one

        Returns
        -------
        List[CalendarItem]
            Reserved slots in all of calendars
        """
        return sum(
            [await calendar.get_reserved_slots() for calendar in self.calendars], []
        )
