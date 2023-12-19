from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional, Dict, Any

from ..members.event_member import EventMember
from ..schedules.calendar_item import CalendarItem


class BaseEvent(ABC):
    def __init__(self, name: str, members: List[EventMember]):
        self.name = name
        self.members = members

    @abstractmethod
    def check_time_slot(self, params: Any) -> Any:
        ...

    @property
    def schedules(self) -> Dict[str, List[CalendarItem]]:
        schedules = {}
        for member in self.members:
            member.actualize_schedule()
            schedules[member.name] = member.schedule
        return schedules

    @property
    def latest_upload(self) -> Optional[datetime]:
        """
        The oldest update time among all calendars of all members,
        or None if one of calendars has never been uploaded
        """
        latest_times = [member.latest_upload for member in self.members]
        return None if None in latest_times else min(latest_times)  # pyright: ignore
