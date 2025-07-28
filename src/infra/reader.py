from pathlib import Path

from src.core.chip import Chip, Part
from src.core.parser import Parser


class Reader:
    def __init__(self, input_dir: str = "tests/data/HDL") -> None:
        self.input_dir = Path(input_dir)
        self.parser = Parser()

    def read_chip(self, name: str) -> Chip:
        file = self.input_dir / (name + ".hdl")
        with open(file, "r") as f:
            lines = f.readlines()
        chip = self.parser.parse(lines)
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
