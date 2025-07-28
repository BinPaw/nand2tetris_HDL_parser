import json
from pathlib import Path

from src.core.chip import Chip, Part


class Reader:
    def __init__(self, input_dir: str) -> None:
        self.input_dir = Path(input_dir)

    def read_chip(self, name: str) -> Chip:
        file = self.input_dir / (name + ".json")
        with open(file, "r") as f:
            description = json.load(f)
        chip = Chip(
            inputs=description["inputs"],
            outputs=description["outputs"],
            parts=[
                Part(name=part["name"], vars=part["vars"])
                for part in description["parts"]
            ],
        )
        return chip

    def read_parts(self, name: str) -> list[Part]:
        chip = self.read_chip(name)
        return chip.parts

    def read_outputs(self, name: str) -> list[str]:
        chip = self.read_chip(name)
        return chip.outputs

    def read_inputs(self, name: str) -> list[str]:
        chip = self.read_chip(name)
        return chip.inputs
