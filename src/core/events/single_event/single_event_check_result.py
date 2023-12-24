from dataclasses import dataclass
from typing import Dict, List, Optional

from ...event_options.location import LocationCheckResult
from ...schedules import CalendarItem


@dataclass
class SingleEventCheckResult:
    is_ok: bool
    overlaps: Dict[str, List[CalendarItem]]
    location_overlaps: Optional[LocationCheckResult]
