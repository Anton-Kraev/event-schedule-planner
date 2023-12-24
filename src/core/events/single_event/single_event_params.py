from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.core.event_options.location import LocationParams


@dataclass
class SingleEventParams:
    start_time: datetime
    end_time: datetime
    location: Optional[LocationParams]
