from dataclasses import dataclass


@dataclass
class Part:
    name: str
    vars: dict[str, str]


@dataclass
class Chip:
    inputs: list[str]
    outputs: list[str]
    parts: list[Part]
