import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from pathlib import Path
from src.runner.runner import Runner

def generate_output_file(input_file: Path, output_file: Path):
  name = input_file.stem
  runner = Runner()

  with open(input_file, 'r') as f:
    lines = f.readlines()
  
  vars = [var.strip() for var in lines[0].split('|')[1:-1]]
  for line in lines[1:]:
    vals = [False if val.strip() == '0' else True for val in line.split('|')[1:-1]]
    input = {vars[i]: vals[i] for i in range(len(vars))}
    output = runner.generate_output(name, input)
    print(output)

def generate_output(input_dir: str, output_dir: str) -> None:
  input_dir = Path(input_dir)
  output_dir = Path(output_dir)
  for file in input_dir.iterdir():
    if file.suffix == '.cmp':
      generate_output_file(file, output_dir / (file.stem + '.out'))

if __name__ == '__main__':
  generate_output('tests/data/cmp', 'tests/data/out')