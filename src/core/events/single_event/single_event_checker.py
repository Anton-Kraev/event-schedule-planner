from .single_event_params import SingleEventParams
from .single_event_check_result import SingleEventCheckResult
from ..base_event import BaseEvent


class SingleEventChecker(BaseEvent):
    async def check_time_slot(
        self, params: SingleEventParams
    ) -> SingleEventCheckResult:
        desired_start_time = params.start_time
        desired_end_time = params.end_time

        overlaps = {}
        schedules = await self.schedules
        for member, schedule in schedules.items():
            member_overlaps = [
                event
                for event in schedule
                if desired_start_time <= event.end_time
                and event.start_time <= desired_end_time
            ]
            if member_overlaps:
                overlaps[member] = member_overlaps

        return SingleEventCheckResult(not overlaps, overlaps, None)
