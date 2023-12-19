from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from ...event_options.classroom.classroom_params import ClassroomParams
from ...event_options.location.location_params import LocationParams


@dataclass
class SingleEventParams:
    start_time: datetime
    end_time: datetime
    location: Optional[LocationParams]
    classroom: Optional[ClassroomParams]
