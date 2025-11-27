import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import shutil

from src.runner.runner import Runner


def generate_output_file(input_file: Path, output_file: Path) -> None:
    name = input_file.stem
    runner = Runner()

    with open(input_file, "r") as f:
        lines = f.readlines()

    input_vars = [var.strip() for var in lines[0].split(";")[0].split(",")]
    output_vars = [var.strip() for var in lines[0].split(";")[1].split(",")]
    result: dict[str, list[str]] = {k: [] for k in input_vars + output_vars}
    for line in lines[1:]:
        input_vals = [
            False if val.strip() == "0" else True
            for val in line.split(";")[0].split(",")
        ]
        input = {input_vars[i]: input_vals[i] for i in range(len(input_vars))}
        output = runner.generate_output(name, input)

        cur_result_bool = input.copy()
        for k, v in output.items():
            cur_result_bool[k] = v
        cur_result = {k: "1" if v else "0" for k, v in cur_result_bool.items()}

        for k, vv in cur_result.items():
            result[k].append(vv)

    with open(output_file, "w") as f:
        f.write(f"{','.join(input_vars)}; {','.join(output_vars)}\n")
        for i in range(len(lines) - 1):
            f.write(
                f"{','.join([f'{result[k][i]}' for k in input_vars])}; "
                f"{','.join([f'{result[k][i]}' for k in output_vars])}\n"
            )


def generate_output(
    input_dir: str = "tests/data/cmp", output_dir: str = "tests/data/out"
) -> None:
    input_dir_p = Path(input_dir)
    output_dir_p = Path(output_dir)
    output_dir_p.mkdir(parents=True, exist_ok=True)
    for file in input_dir_p.iterdir():
        if file.suffix == ".cmp":
            generate_output_file(file, output_dir_p / (file.stem + ".out"))


def remove_output(output_dir: str = "tests/data/out") -> None:
    output_dir_p = Path(output_dir)
    shutil.rmtree(output_dir_p)


if __name__ == "__main__":
    generate_output()
