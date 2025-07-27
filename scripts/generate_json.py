import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.infra.parser import Parser

def generate_json(
    input_dir: str = 'tests/data/HDL',
    output_dir: str = 'tests/data/JSON'
  ) -> None:
  parser = Parser(input_dir=input_dir, output_dir=output_dir)
  parser.parse()

if __name__ == '__main__':
  generate_json()