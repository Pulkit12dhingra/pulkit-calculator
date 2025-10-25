from __future__ import annotations
import sys
from typing import Callable, Dict

__version__ = "0.1.0"

def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b

def sub(a: float, b: float) -> float:
    """Return a - b."""
    return a - b

def mul(a: float, b: float) -> float:
    """Return a * b."""
    return a * b

def div(a: float, b: float) -> float:
    """Return a / b. Raises ZeroDivisionError on division by zero."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def _parse_args(argv: list[str]) -> tuple[Callable[[float, float], float], float, float]:
    """
    Parse CLI args: calculator <op> <a> <b>
    where <op> in {add, sub, mul, div}
    """
    if len(argv) != 4:
        raise SystemExit("Usage: calculator <add|sub|mul|div> <a> <b>")

    _, op, a_str, b_str = argv
    ops: Dict[str, Callable[[float, float], float]] = {
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
    }
    if op not in ops:
        raise SystemExit("Error: op must be one of add|sub|mul|div")

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        raise SystemExit("Error: <a> and <b> must be numbers")

    return ops[op], a, b

def main() -> None:
    """Console script entry point."""
    try:
        fn, a, b = _parse_args(sys.argv)
        result = fn(a, b)
        # Print without trailing decimals if integral (e.g., 5.0 -> 5)
        if isinstance(result, float) and result.is_integer():
            print(int(result))
        else:
            print(result)
    except ZeroDivisionError as e:
        print(f"Error: {e}", file=sys.stderr)
        raise SystemExit(1)
    except SystemExit as e:
        # Re-raise after printing help/errors above
        raise e
    except Exception as e:  # fallback for unexpected errors
        print(f"Unexpected error: {e}", file=sys.stderr)
        raise SystemExit(1)
