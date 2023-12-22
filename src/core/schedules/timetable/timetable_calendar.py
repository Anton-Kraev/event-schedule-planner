from typing import List

from httpx import AsyncClient, codes

from config import TT_API_BASE_PATH
from ..base_calendar import BaseCalendar
from ..calendar_item import CalendarItem
from .timetable_calendar_item import TimetableCalendarItem
from ..calendar_type import CalendarType
from ...members.member_type import MemberType


class TimetableCalendar(BaseCalendar):
    async def _upload(self) -> List[TimetableCalendarItem]:
        events = []
        async with AsyncClient(base_url=TT_API_BASE_PATH) as client:
            match self.owner_type:
                case MemberType.educator:
                    first_name, last_name, middle_name = self.owner_name.split(" ")
                    educator_find_res = await client.get(
                        "/educator/find",
                        params={
                            "first_name": first_name,
                            "last_name": last_name,
                            "middle_name": middle_name,
                        },
                    )
                    if educator_find_res.status_code == codes.OK:
                        educator_id = int(educator_find_res.text)
                        events_res = await client.get(
                            f"/educator/{educator_id}/events",
                        )
                        events = events_res.json()["events"]
                case MemberType.group:
                    group_find_res = await client.get(
                        "/group/find", params={"name": self.owner_name}
                    )
                    if group_find_res.status_code == codes.OK:
                        group_id = int(group_find_res.text)
                        events_res = await client.get(
                            f"/group/{group_id}/events",
                        )
                        events = events_res.json()["events"]
                case MemberType.classroom:
                    events_res = await client.get(
                        f"/classroom/{self.owner_name}/events",
                    )
                    events = events_res.json()["events"]

        return events or [
            TimetableCalendarItem(
                start_time=e.start_time,
                end_time=e.end_time,
                location=e.location,
                description=e.description,
            )
            for e in events
        ]

    def _standardize(
        self, external_calendar: List[TimetableCalendarItem]
    ) -> List[CalendarItem]:
        return [
            CalendarItem(
                start_time=item.start_time,
                end_time=item.end_time,
                location=item.location,
                description=item.description,
                source=CalendarType.timetable,
            )
            for item in external_calendar
        ]
