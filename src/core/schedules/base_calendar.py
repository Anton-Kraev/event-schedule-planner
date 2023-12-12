from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

from .calendar_item import CalendarItem
from ..members.member_type import MemberType


class BaseCalendar[T](ABC):
    """
    An abstract base class to implement fetching and
    storing a calendar from external sources

    Attributes
    ----------
    owner_type : MemberType
        Type of the calendar owner required to receive the calendar
    owner_name : str
        Name of the calendar owner required to receive the calendar
    reserved_slots : Optional[List[CalendarItem]]
        A list of CalendarItems representing events or reservations that occupy time slots
        in the calendar. Can be None if the calendar has not yet been downloaded once
    latest_upload : Optional[datetime]
        Time for which the data from the reserved_slots attribute is relevant
    """

    def __init__(self, owner_name: str, owner_type: MemberType):
        """
        Inits BaseCalendar with owner info and sets None in the variables with calendar information

        Parameters
        ----------
        owner_name : str
            Owner name
        owner_type : str
            Owner type
        """
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.reserved_slots: Optional[List[CalendarItem]] = None
        self.latest_upload: Optional[datetime] = None

    def actualize(self) -> None:
        """
        Updates the calendar (occupied_slots)
        by downloading or synchronizing it with a remote service
        """
        latest_update = self._latest_update()
        if not self.latest_upload or latest_update > self.latest_upload:
            calendar = self._upload()
            self.reserved_slots = self._standardize(calendar)
            self.latest_upload = latest_update

    @abstractmethod
    def _upload(self) -> T:
        """
        Uploads or synchronizes the calendar with a remote service

        Returns
        -------
        T
            Calendar in the external view
        """
        ...

    @abstractmethod
    def _standardize(self, external_calendar: T) -> List[CalendarItem]:
        """
        Converts external calendar to the uniform view

        Parameters
        ----------
        external_calendar : T
            Calendar obtained from an external service

        Returns
        -------
        List[CalendarItem]
            Calendar in the uniform view
        """
        ...

    @abstractmethod
    def _latest_update(self) -> datetime:
        """
        Gets the time of the last update of the external calendar

        Returns
        -------
        datetime
            Time of last update
        """
        ...
