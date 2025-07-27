import json
from pathlib import Path
import re

class Parser:
  def __init__(self, input_dir: str, output_dir: str) -> None:
    self.input_dir = Path(input_dir)
    self.output_dir = Path(output_dir)
    self.output_dir.mkdir(parents=True, exist_ok=True)

  def parse(self) -> None:
    for file in self.input_dir.iterdir():
      if file.suffix == '.hdl':
        self.parse_file(input_file=file, output_file=self.output_dir / (file.stem + '.json'))

  def parse_file(self, input_file: Path, output_file: Path) -> None:
    with open(input_file, 'r') as f:
      lines = f.readlines()

    parts_section = False
    parts = []
    for line in lines:
      if line.strip() == 'PARTS:':
        parts_section = True
        continue
      if parts_section:
        if line.strip() == '}':
          break
        part_line = line.strip().rstrip(';')
        if not part_line:
          continue

        if '(' in part_line and ')' in part_line:
          part_name = part_line.split('(')[0]
          vars_str = part_line.split('(', 1)[1].split(')', 1)[0]
          vars_dict = {}
          for var in vars_str.split(','):
            if '=' in var:
              k, v = var.split('=')
              vars_dict[k.strip()] = v.strip()
          parts.append({
            'name': part_name,
            'vars': vars_dict
          })

    outputs = re.findall(r'OUT\s+([\w,]+);', ''.join(lines))
    outputs = [output.strip() for output in outputs[0].split(',')]

    description = {
      'outputs': outputs,
      'parts': parts
    }

    with open(output_file, 'w') as f:
      json.dump(description, f, indent=2)


