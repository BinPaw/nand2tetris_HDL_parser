from pathlib import Path

from scripts.generate_output import generate_output, remove_output


def parse_file(file: Path) -> dict[str, list[str]]:
    with open(file, "r") as f:
        lines = f.readlines()

    vars = [var.strip() for var in lines[0].split("|")[1:-1]]
    parsed: dict[str, list[str]] = {var: [] for var in vars}
    for line in lines[1:]:
        for idx, val in enumerate(line.split("|")[1:-1]):
            parsed[vars[idx]].append(val.strip())

    return parsed


def compare_files(cmp_file: Path, out_file: Path) -> None:
    name = cmp_file.stem

    cmp_dict = parse_file(cmp_file)
    out_dict = parse_file(out_file)

    cmp_vars = [var for var in cmp_dict.keys()]
    out_vars = [var for var in out_dict.keys()]

    assert out_vars == cmp_vars
    vars = cmp_vars

    line_n = len(cmp_dict[cmp_vars[0]])
    for var in vars:
        assert len(cmp_dict[var]) == line_n
        assert len(out_dict[var]) == line_n

    for i in range(line_n):
        for var in vars:
            if out_dict[var][i] != cmp_dict[var][i]:
                print(
                    f"mismatch in {name}.out\n"
                    f"output differs on line - {i}, "
                    f"variable - {var}\n"
                    f"expected '{cmp_dict[var][i]}', "
                    f"got '{out_dict[var][i]}'"
                )
            assert out_dict[var][i] == cmp_dict[var][i]


def test_outputs() -> None:
    generate_output()

    cmp_dir = Path("tests/data/cmp")
    out_dir = Path("tests/data/out")

    for cmp_file in cmp_dir.iterdir():
        if cmp_file.suffix == ".cmp":
            out_file = out_dir / (cmp_file.stem + ".out")
            compare_files(cmp_file, out_file)

    remove_output()
