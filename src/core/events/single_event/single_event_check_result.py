from dataclasses import dataclass
from typing import Dict, List

from ...schedules.calendar_item import CalendarItem


@dataclass
class SingleEventCheckResult:
    is_ok: bool
    overlaps: Dict[str, List[CalendarItem]]
