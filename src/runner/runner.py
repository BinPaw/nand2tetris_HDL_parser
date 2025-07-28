from src.core.bit import Bit
from src.core.chip import Part
from src.infra.reader import Reader


class Runner:
    def __init__(self, reader: Reader | None = None) -> None:
        if not reader:
            reader = Reader()
        self.reader = reader

    def run(self, parts: list[Part], vars: dict[str, Bit]) -> None:
        vars["0"] = Bit(False)
        vars["1"] = Bit(True)

        for part in parts:
            part_name = part.name
            part_vars = part.vars
            if part_name == "Nand":
                self._run_nand(part_vars, vars)
            elif part_name == "Not":
                self._run_not(part_vars, vars)
            elif part_name == "And":
                self._run_and(part_vars, vars)
            elif part_name == "Or":
                self._run_or(part_vars, vars)
            else:
                self._run_composite(part_name, part_vars, vars)

    def generate_output(self, name: str, input: dict[str, bool]) -> dict[str, bool]:
        parts = self.reader.read_parts(name)
        inputs = self.reader.read_inputs(name)
        outputs = self.reader.read_outputs(name)
        vars = {k: Bit(v) for k, v in input.items() if k in inputs}
        self.run(parts, vars)
        res = {k: v.val for k, v in vars.items() if k in outputs}
        return res

    def _run_composite(
        self, part_name: str, part_vars: dict[str, str], vars: dict[str, Bit]
    ) -> None:
        next_parts = self.reader.read_parts(name=part_name)
        next_vars = {}
        for k, v in part_vars.items():
            if v not in vars:
                vars[v] = Bit()
            next_vars[k] = vars[v]
        self.run(parts=next_parts, vars=next_vars)

    def _run_nand(self, part_vars: dict[str, str], vars: dict[str, Bit]) -> None:
        a = vars[part_vars["a"]].val
        b = vars[part_vars["b"]].val
        if part_vars["out"] not in vars:
            vars[part_vars["out"]] = Bit()
        vars[part_vars["out"]].nand_(a=a, b=b)

    def _run_not(self, part_vars: dict[str, str], vars: dict[str, Bit]) -> None:
        a = vars[part_vars["in"]].val
        if part_vars["out"] not in vars:
            vars[part_vars["out"]] = Bit()
        vars[part_vars["out"]].not_(a=a)

    def _run_and(self, part_vars: dict[str, str], vars: dict[str, Bit]) -> None:
        a = vars[part_vars["a"]].val
        b = vars[part_vars["b"]].val
        if part_vars["out"] not in vars:
            vars[part_vars["out"]] = Bit()
        vars[part_vars["out"]].and_(a=a, b=b)

    def _run_or(self, part_vars: dict[str, str], vars: dict[str, Bit]) -> None:
        a = vars[part_vars["a"]].val
        b = vars[part_vars["b"]].val
        if part_vars["out"] not in vars:
            vars[part_vars["out"]] = Bit()
        vars[part_vars["out"]].or_(a=a, b=b)
