from dataclasses import dataclass
from typing import Optional


@dataclass
class TerneoTelemetry:
    current_temperature: Optional[float]
    target_temperature: Optional[int]
    heating: Optional[bool]
    power_off: Optional[bool]


@dataclass
class TerneoDevice:
    ip: str
    serial_number: str