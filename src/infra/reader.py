import json
from pathlib import Path


class Reader:
    def __init__(self, input_dir: str) -> None:
        self.input_dir = Path(input_dir)

    def read_chip(
        self, name: str
    ) -> dict[str, list[dict[str, str | dict[str, str]]] | list[str]]:
        file = self.input_dir / (name + ".json")
        description: dict[str, list[dict[str, str | dict[str, str]]] | list[str]] = {}
        with open(file, "r") as f:
            description = json.load(f)
        return description

    def read_parts(self, name: str) -> list[dict[str, str | dict[str, str]]]:
        parts: list[dict[str, str | dict[str, str]]] = self.read_chip(name)["parts"]
        return parts

    def read_outputs(self, name: str) -> list[str]:
        outputs: list[str] = self.read_chip(name)["outputs"]
        return outputs

    def read_inputs(self, name: str) -> list[str]:
        inputs: list[str] = self.read_chip(name)["inputs"]
        return inputs
