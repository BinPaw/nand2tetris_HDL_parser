# HDL Parser and Chip Testing Framework

## Overview

This project is a Python-based framework for parsing HDL (Hardware Description Language) files, simulating digital chips, and automatically testing their behavior against provided test vectors. It supports both built-in primitive gates and user-defined chips described in HDL.

---

## Features

- **HDL Parsing:** Reads and parses HDL files to build an internal model of each chip.
- **Simulation:** Simulates chip behavior, including recursive instantiation of sub-chips.
- **Built-in Gates:** Supports `Nand`, `Not`, `And`, and `Or` as atomic primitives.
- **Automated Testing:** Compares simulation outputs to expected results from test vector files.
- **Test Reporting:** Prints detailed pass/fail results and summary statistics.

---

## Directory Structure

```
nand_final_HDL/
├── src/
│   ├── core/      # Core logic: Bit, Chip, Parser
│   ├── infra/     # File reading and HDL loading
│   └── runner/    # Simulation and test runner
├── scripts/       # Utility scripts (e.g., generate_output.py)
├── tests/
│   ├── data/      # HDL files and test vectors
│   └── test_outputs.py  # Main test file
├── Makefile
├── pyproject.toml
└── README.md
```

---

## Getting Started

This project uses [Poetry](https://python-poetry.org/) for dependency management.

### 1. Install Dependencies

```sh
make install
```

### 2. Run the Test Suite

To run all tests and see detailed output:

```sh
make test
```

This will:
- Generate output files for each chip using the HDL and test vector files.
- Compare the generated outputs to the expected `.cmp` files.
- Print a summary of test results.

### 3. Generate Outputs Manually

To generate `.out` files for all chips (without running the full test suite):

```sh
poetry run python scripts/generate_output.py
```

Output files will be created in `tests/data/out/`.

---

## How It Works

- **HDL files** (in `tests/data/HDL/`) define chips, their inputs, outputs, and internal parts.
- **Test vector files** (in `tests/data/cmp/`) specify input values and expected outputs for each chip.
- The framework parses each HDL file, builds a model, and simulates the chip for each test vector.
- Results are compared to the expected outputs, and a summary is printed.

---

## Example

### HDL File (`tests/data/HDL/Xor.hdl`)

```hdl
CHIP Xor {
    IN a, b;
    OUT out;

    PARTS:
    Not(in=a, out=na);
    Not(in=b, out=nb);
    And(a=a, b=b, out=ab);
    And(a=na, b=nb, out=nanb);
    Or(a=ab, b=nanb, out=eq);
    Not(in=eq, out=out);
}
```

### Test Vector File (`tests/data/cmp/Xor.cmp`)

```csv
a,b; out
0,0; 0
0,1; 1
1,0; 1
1,1; 0
```

---

## Adding New Chips and Tests

1. **Add your HDL file** to `tests/data/HDL/YourChip.hdl`.
2. **Add your test vector file** to `tests/data/cmp/YourChip.cmp`.
3. Run the tests as above. The framework will automatically pick up and test your new chip.

---

## Notes

- Only single-bit inputs/outputs are supported.
- HDL and test vector files must be syntactically correct.
- No error handling for missing or malformed files (by design).