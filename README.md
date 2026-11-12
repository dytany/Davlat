# Davlat

A small scratch repository.

## Calculator — `calc.py`

A simple command-line calculator that supports addition, subtraction,
multiplication and division.

### Requirements

Python 3.6 or newer (the script uses only the standard library).

### Usage

```bash
python calc.py <number> <operation> <number>
```

Supported operations: `+`, `-`, `*`, `/`.

### Examples

```bash
python calc.py 2 + 3     # 5.0
python calc.py 10 - 4    # 6.0
python calc.py 3 '*' 7   # 21.0
python calc.py 8 / 2     # 4.0
```

### Notes

- Division by zero and invalid input print an error message and exit with code 1.
- On Windows, quote `*` (`python calc.py 3 "*" 7`) so the shell does not expand it.

## Contents

- `test.txt` — greeting used for repository smoke tests.
- `calc.py` — the calculator script described above.