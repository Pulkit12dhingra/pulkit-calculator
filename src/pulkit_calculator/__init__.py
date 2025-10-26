"""
pulkit_calculator: a tiny example calculator library (scientific).
"""

from .core import (  # noqa: F401
    add,
    sub,
    mul,
    div,
    pow_ as _pow_impl,
    mod,
    floordiv,
    square,
    sqrt,
    nth_root,
    ceil,
    floor,
    gcd,
    lcm,
    hcf,
    derivative,
    integrate,
    mat_add,
    mat_sub,
    mat_mul,
    mat_transpose,
    mat_det,
    mat_inverse,
    mat_solve,
    c_add,
    c_sub,
    c_mul,
    c_div,
    c_conj,
    c_abs,
    c_phase,
    c_pow,
)

# Public version for the package
#__version__ = "0.1.0"

# Expose built-in-like name `pow` that maps to core.pow_
pow = _pow_impl  # noqa: A001

__all__ = [
    "__version__",
    # basic arithmetic
    "add",
    "sub",
    "mul",
    "div",
    "pow",
    "mod",
    "floordiv",
    "square",
    "sqrt",
    "nth_root",
    "ceil",
    "floor",
    # number theory
    "gcd",
    "lcm",
    "hcf",
    # calculus
    "derivative",
    "integrate",
    # linear algebra
    "mat_add",
    "mat_sub",
    "mat_mul",
    "mat_transpose",
    "mat_det",
    "mat_inverse",
    "mat_solve",
    # complex operations
    "c_add",
    "c_sub",
    "c_mul",
    "c_div",
    "c_conj",
    "c_abs",
    "c_phase",
    "c_pow",
]
