from __future__ import annotations

import math
from typing import Callable, List, Tuple

__all__ = [
    "add",
    "sub",
    "mul",
    "div",
    "pow_",
    "square",
    "sqrt",
    "nth_root",
    "ceil",
    "floor",
    "mod",
    "floordiv",
    "gcd",
    "lcm",
    "hcf",
    "derivative",
    "integrate",
    "mat_add",
    "mat_sub",
    "mat_mul",
    "mat_transpose",
    "mat_det",
    "mat_inverse",
    "mat_solve",
    "c_add",
    "c_sub",
    "c_mul",
    "c_div",
    "c_conj",
    "c_abs",
    "c_phase",
    "c_pow",
]

# -----------------------------
# Basic arithmetic
# -----------------------------


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


def pow_(a: float, b: float) -> float:
    """Return a ** b."""
    return a ** b


def square(a: float) -> float:
    """Return a squared."""
    return a * a


def sqrt(a: float) -> float:
    """Return the non-negative square root of *a*.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("sqrt undefined for negative numbers; use complex equivalents")
    return math.sqrt(a)


def nth_root(a: float, n: int) -> float:
    """Return the real n-th root of *a*.

    For even n, *a* must be non-negative.
    For odd n, negative *a* is allowed and returns a negative real root.
    """
    if n == 0:
        raise ValueError("0th root is undefined")
    if n % 2 == 0 and a < 0:
        raise ValueError("even root of negative number is not real")
    sign = -1.0 if a < 0 and n % 2 == 1 else 1.0
    return sign * (abs(a) ** (1.0 / n))


def ceil(a: float) -> int:
    """Return the ceiling of *a* as int."""
    return math.ceil(a)


def floor(a: float) -> int:
    """Return the floor of *a* as int."""
    return math.floor(a)


def mod(a: float, b: float) -> float:
    """Return a % b. Raises ZeroDivisionError on modulo by zero."""
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b


def floordiv(a: float, b: float) -> int:
    """Return a // b. Raises ZeroDivisionError on division by zero."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return int(a // b)


# -----------------------------
# Number theory
# -----------------------------


def gcd(a: int, b: int) -> int:
    """Greatest common divisor using Euclid's algorithm."""
    a_i, b_i = abs(int(a)), abs(int(b))
    while b_i:
        a_i, b_i = b_i, a_i % b_i
    return a_i


def lcm(a: int, b: int) -> int:
    """Least common multiple."""
    a_i, b_i = abs(int(a)), abs(int(b))
    if a_i == 0 or b_i == 0:
        return 0
    return a_i // gcd(a_i, b_i) * b_i


def hcf(a: int, b: int) -> int:
    """Highest common factor (alias of gcd)."""
    return gcd(a, b)


# -----------------------------
# Calculus
# -----------------------------


def derivative(
    func: Callable[[float], float], x: float, h: float = 1e-6, order: int = 1
) -> float:
    """Numerical derivative of *func* at point *x*.

    Uses central difference for 1st order and a simple stencil for 2nd order.

    Args:
        func: Function f(x).
        x: Point of evaluation.
        h: Step size (positive).
        order: 1 or 2.

    Returns:
        The derivative approximation.

    Raises:
        ValueError: If h <= 0 or order not in {1, 2}.
    """
    if h <= 0:
        raise ValueError("h must be positive")
    if order == 1:
        return (func(x + h) - func(x - h)) / (2.0 * h)
    if order == 2:
        return (func(x + h) - 2.0 * func(x) + func(x - h)) / (h * h)
    raise ValueError("only order 1 or 2 are supported")


def integrate(func: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
    """Numerically integrate *func* from *a* to *b* using Simpson's rule.

    *n* must be an even integer >= 2.

    Raises:
        ValueError: If n is not an even integer >= 2.
    """
    if n < 2 or n % 2 == 1:
        raise ValueError("n must be an even integer >= 2")
    if a == b:
        return 0.0
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n):
        x_i = a + i * h
        s += (4 if i % 2 == 1 else 2) * func(x_i)
    return s * h / 3.0


# -----------------------------
# Linear algebra on dense matrices (lists of lists)
# -----------------------------

Matrix = List[List[float]]
Vector = List[float]


def _shape(A: Matrix) -> Tuple[int, int]:
    rows = len(A)
    cols = len(A[0]) if rows else 0
    for r in A:
        if len(r) != cols:
            raise ValueError("irregular matrix")
    return rows, cols


def mat_add(A: Matrix, B: Matrix) -> Matrix:
    """Elementwise A + B."""
    r1, c1 = _shape(A)
    r2, c2 = _shape(B)
    if (r1, c1) != (r2, c2):
        raise ValueError("shape mismatch for addition")
    return [[A[i][j] + B[i][j] for j in range(c1)] for i in range(r1)]


def mat_sub(A: Matrix, B: Matrix) -> Matrix:
    """Elementwise A - B."""
    r1, c1 = _shape(A)
    r2, c2 = _shape(B)
    if (r1, c1) != (r2, c2):
        raise ValueError("shape mismatch for subtraction")
    return [[A[i][j] - B[i][j] for j in range(c1)] for i in range(r1)]


def mat_mul(A: Matrix, B: Matrix) -> Matrix:
    """Matrix product A @ B."""
    r1, c1 = _shape(A)
    r2, c2 = _shape(B)
    if c1 != r2:
        raise ValueError("shape mismatch for multiplication")
    return [[sum(A[i][k] * B[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]


def mat_transpose(A: Matrix) -> Matrix:
    """Transpose of A."""
    r, c = _shape(A)
    return [[A[i][j] for i in range(r)] for j in range(c)]


def mat_det(A: Matrix) -> float:
    """Determinant via a simple LU-style elimination (with cofactor fallback for <=3)."""
    n, m = _shape(A)
    if n != m:
        raise ValueError("determinant requires a square matrix")
    # Copy
    U = [row[:] for row in A]
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1.0
    det = 1.0
    for k in range(n):
        pivot = U[k][k]
        if pivot == 0:
            # Cofactor expansion is fine for small matrices.
            if n <= 3:
                return _det_via_cofactor(A)
            raise ValueError("singular matrix (zero pivot)")
        det *= pivot
        for i in range(k + 1, n):
            factor = U[i][k] / pivot
            L[i][k] = factor
            for j in range(k, n):
                U[i][j] -= factor * U[k][j]
    return det


def _det_via_cofactor(A: Matrix) -> float:
    n, _ = _shape(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0.0
    for j in range(n):
        minor = [row[:j] + row[j + 1 :] for row in A[1:]]
        det += ((-1) ** j) * A[0][j] * _det_via_cofactor(minor)
    return det


def mat_inverse(A: Matrix) -> Matrix:
    """Inverse via Gauss-Jordan elimination.

    Raises:
        ValueError: if matrix is not square or singular.
    """
    n, m = _shape(A)
    if n != m:
        raise ValueError("inverse requires a square matrix")
    # Augment with identity
    M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    # Forward elimination
    for col in range(n):
        # Partial pivoting (choose largest absolute pivot)
        pivot_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot_row][col]) < 1e-12:
            raise ValueError("singular matrix")
        if pivot_row != col:
            M[col], M[pivot_row] = M[pivot_row], M[col]
        # Normalize pivot row
        pivot = M[col][col]
        inv_pivot = 1.0 / pivot
        M[col] = [v * inv_pivot for v in M[col]]
        # Eliminate other rows
        for r in range(n):
            if r == col:
                continue
            factor = M[r][col]
            if factor != 0.0:
                M[r] = [M[r][c] - factor * M[col][c] for c in range(2 * n)]
    # Extract inverse
    return [row[n:] for row in M]


def mat_solve(A: Matrix, b: Vector) -> Vector:
    """Solve Ax = b using Gaussian elimination with partial pivoting."""
    n, m = _shape(A)
    if n != m:
        raise ValueError("solve requires a square matrix")
    if len(b) != n:
        raise ValueError("dimension mismatch between A and b")
    # Augment
    M = [A[i][:] + [b[i]] for i in range(n)]
    for col in range(n):
        pivot_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot_row][col]) < 1e-12:
            raise ValueError("singular matrix")
        if pivot_row != col:
            M[col], M[pivot_row] = M[pivot_row], M[col]
        # Normalize pivot row
        pivot = M[col][col]
        inv_pivot = 1.0 / pivot
        M[col] = [v * inv_pivot for v in M[col]]
        # Eliminate below
        for r in range(col + 1, n):
            factor = M[r][col]
            if factor != 0.0:
                M[r] = [M[r][c] - factor * M[col][c] for c in range(n + 1)]
    # Back substitution
    x = [0.0 for _ in range(n)]
    for i in reversed(range(n)):
        x[i] = M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))
    return x


# -----------------------------
# Complex number helpers
# -----------------------------


def c_add(a: complex, b: complex) -> complex:
    """Complex addition."""
    return complex(a) + complex(b)


def c_sub(a: complex, b: complex) -> complex:
    """Complex subtraction."""
    return complex(a) - complex(b)


def c_mul(a: complex, b: complex) -> complex:
    """Complex multiplication."""
    return complex(a) * complex(b)


def c_div(a: complex, b: complex) -> complex:
    """Complex division. Raises ZeroDivisionError on division by zero."""
    if b == 0:
        raise ZeroDivisionError("complex division by zero")
    return complex(a) / complex(b)


def c_conj(a: complex) -> complex:
    """Complex conjugate."""
    return complex(a).conjugate()


def c_abs(a: complex) -> float:
    """Complex magnitude (modulus)."""
    return abs(complex(a))


def c_phase(a: complex) -> float:
    """Complex argument (phase), in radians."""
    z = complex(a)
    return math.atan2(z.imag, z.real)


def c_pow(a: complex, b: complex) -> complex:
    """Complex exponentiation."""
    return complex(a) ** complex(b)
