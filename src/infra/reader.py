import json
from pathlib import Path

class Reader:
  def __init__(self, input_dir: str) -> None:
    self.input_dir = Path(input_dir)

  def read_chip(self, name: str) -> dict[str, list[dict[str, str | dict[str, str]]] | list[str]]:
    file = self.input_dir / (name + '.json')
    with open(file, 'r') as f:
      description = json.load(f)
    return description

  def read_parts(self, name: str) -> list[dict[str, str | dict[str, str]]]:
    return self.read_chip(name)['parts']

  def read_outputs(self, name: str) -> list[str]:
    return self.read_chip(name)['outputs']

  def read_inputs(self, name: str) -> list[str]:
    return self.read_chip(name)['inputs']