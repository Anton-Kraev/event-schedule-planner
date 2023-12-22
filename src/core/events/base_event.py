from abc import ABC, abstractmethod
from typing import List, Dict, Any

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
    async def schedules(self) -> Dict[str, List[CalendarItem]]:
        return {member.name: await member.schedule for member in self.members}
