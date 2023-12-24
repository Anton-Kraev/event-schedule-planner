from dataclasses import dataclass


@dataclass
class LocationParams:
    ...


@dataclass
class LocationCheckResult:
    ...


def check_location(params: LocationParams) -> LocationCheckResult:
    ...
