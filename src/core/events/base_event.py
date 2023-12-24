from abc import ABC, abstractmethod
from typing import List, Dict, Any

from ..members import EventMember
from ..schedules import CalendarItem


class BaseEvent(ABC):
    """
    An abstract base class for events implementations

    Attributes
    ----------
    name : str
        Name of event
    members : List[EventMember]
        List of planned members in the event
    """

    def __init__(self, name: str, members: List[EventMember]):
        """
        Inits BaseEvent with event name and members list

        Parameters
        ----------
        name : str
            Name of event
        members : List[EventMember]
            List of planned members in the event
        """
        self.name = name
        self.members = members

    @abstractmethod
    def check_time_slot(self, params: Any) -> Any:
        """
        Checks time slot(s) and gives a detailed answer as to the event can be
        staged at that slot(s), taking into account certain options

        Parameters
        ----------
        params : Any
            Event options

        Returns
        -------
        Any
            Time slot(s) check result
        """
        ...

    @property
    async def schedules(self) -> Dict[str, List[CalendarItem]]:
        """
        Gets the actual schedules of event members

        Returns
        -------
        Dict[str, List[CalendarItem]]
            Schedule for each member
        """
        return {member.name: await member.schedule for member in self.members}
