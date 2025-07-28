import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pathlib import Path

from src.runner.runner import Runner


def generate_output_file(input_file: Path, output_file: Path) -> None:
    name = input_file.stem
    runner = Runner()

    with open(input_file, "r") as f:
        lines = f.readlines()

    vars = [var.strip() for var in lines[0].split("|")[1:-1]]
    result: dict[str, list[str]] = {k: [] for k in vars}
    for line in lines[1:]:
        vals = [False if val.strip() == "0" else True for val in line.split("|")[1:-1]]
        input = {vars[i]: vals[i] for i in range(len(vars))}
        output = runner.generate_output(name, input)

        cur_result_b = input.copy()
        for k, v in output.items():
            cur_result_b[k] = v
        cur_result: dict[str, str] = {
            k: "1" if v else "0" for k, v in cur_result_b.items()
        }

        for k, vv in cur_result.items():
            result[k].append(vv)

    with open(output_file, "w") as f:
        f.write(
            f"|{
                '|'.join([key if len(key) > 1 else f' {key} ' for key in result.keys()])
            }|\n"
        )
        for i in range(len(lines) - 1):
            f.write(f"|{'|'.join([f' {result[k][i]} ' for k in result.keys()])}|\n")


def generate_output(
    input_dir: str = "tests/data/cmp", output_dir: str = "tests/data/out"
) -> None:
    input_dir_p = Path(input_dir)
    output_dir_p = Path(output_dir)
    for file in input_dir_p.iterdir():
        if file.suffix == ".cmp":
            generate_output_file(file, output_dir_p / (file.stem + ".out"))


if __name__ == "__main__":
    generate_output()
