import re

from src.core.chip import Chip, Part


class Parser:
    def parse(self, lines: list[str]) -> Chip:
        parts_section = False
        parts = []
        for line in lines:
            if line.strip() == "PARTS:":
                parts_section = True
                continue
            if parts_section:
                if line.strip() == "}":
                    break
                part_line = line.strip().rstrip(";")
                if not part_line:
                    continue

                if "(" in part_line and ")" in part_line:
                    part_name = part_line.split("(")[0]
                    vars_str = part_line.split("(", 1)[1].split(")", 1)[0]
                    vars_dict = {}
                    for var in vars_str.split(","):
                        if "=" in var:
                            k, v = var.split("=")
                            vars_dict[k.strip()] = v.strip()
                    parts.append({"name": part_name, "vars": vars_dict})

        inputs = re.findall(r"IN\s+([\w\s*,]+);", "".join(lines))
        inputs = [input.strip() for input in inputs[0].split(",")]

        outputs = re.findall(r"OUT\s+([\w\s*,]+);", "".join(lines))
        outputs = [output.strip() for output in outputs[0].split(",")]

        description = {"inputs": inputs, "outputs": outputs, "parts": parts}

        chip = Chip(
            inputs=description["inputs"],
            outputs=description["outputs"],
            parts=[
                Part(name=part["name"], vars=part["vars"])
                for part in description["parts"]
            ],
        )

        return chip
