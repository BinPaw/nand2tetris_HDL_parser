import re

from src.core.chip import Chip, Part


class Parser:
    def parse(self, lines: list[str]) -> Chip:
        parts_section = False
        parts: list[Part] = []
        for line in lines:
            line = line.strip()
            if line == "PARTS:":
                parts_section = True
                continue
            if parts_section:
                if line == "}":
                    break

                part_name = line.split("(")[0]
                vars_str = line.split("(", 1)[1].split(")", 1)[0]
                vars_dict: dict[str, str] = {}
                for var in vars_str.split(","):
                    if "=" in var:
                        k, v = var.split("=")
                        vars_dict[k.strip()] = v.strip()
                parts.append(Part(name=part_name, vars=vars_dict))

        inputs = re.findall(r"IN\s+([\w\s*,]+);", "".join(lines))
        inputs = [input.strip() for input in inputs[0].split(",")]

        outputs = re.findall(r"OUT\s+([\w\s*,]+);", "".join(lines))
        outputs = [output.strip() for output in outputs[0].split(",")]

        chip = Chip(inputs=inputs, outputs=outputs, parts=parts)

        return chip
