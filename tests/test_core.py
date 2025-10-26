import math

import pytest

from core import (
    add,
    sub,
    mul,
    div,
    pow_,
    square,
    sqrt,
    nth_root,
    ceil,
    floor,
    mod,
    floordiv,
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

# -----------------------------
# Basic arithmetic
# -----------------------------


def test_basic_arithmetic():
    assert add(2, 3) == 5
    assert sub(5, 7) == -2
    assert mul(3, 4) == 12
    assert div(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
    assert pow_(2, 3) == 8
    assert square(5) == 25
    assert sqrt(16) == 4
    with pytest.raises(ValueError):
        sqrt(-1)
    assert pytest.approx(nth_root(27, 3), rel=1e-12) == 3
    assert pytest.approx(nth_root(81, 4), rel=1e-12) == 3
    with pytest.raises(ValueError):
        nth_root(-16, 4)
    assert ceil(3.2) == 4
    assert floor(3.8) == 3
    assert mod(7, 3) == 1
    with pytest.raises(ZeroDivisionError):
        mod(1, 0)
    assert floordiv(7, 2) == 3
    with pytest.raises(ZeroDivisionError):
        floordiv(1, 0)


# -----------------------------
# Number theory
# -----------------------------


def test_number_theory():
    assert gcd(48, 18) == 6
    assert gcd(-48, 18) == 6
    assert lcm(4, 6) == 12
    assert lcm(0, 5) == 0
    assert hcf(100, 85) == 5


# -----------------------------
# Calculus
# -----------------------------


def test_derivative_and_integral():
    f = lambda x: x**3  # noqa: E731
    df_at_2 = derivative(f, 2.0)
    assert pytest.approx(df_at_2, rel=1e-6) == 12.0  # 3*x^2 at x=2
    d2f_at_2 = derivative(f, 2.0, order=2)
    assert pytest.approx(d2f_at_2, rel=1e-5) == 12.0  # 6*x at x=2
    with pytest.raises(ValueError):
        derivative(f, 1.0, h=-1.0)
    with pytest.raises(ValueError):
        derivative(f, 1.0, order=3)

    g = math.sin
    area = integrate(g, 0.0, math.pi, n=1000)
    assert pytest.approx(area, rel=1e-6) == 2.0
    with pytest.raises(ValueError):
        integrate(g, 0.0, 1.0, n=3)  # n must be even


# -----------------------------
# Linear algebra
# -----------------------------


def test_linear_algebra_basic():
    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]
    assert mat_add(A, B) == [[6.0, 8.0], [10.0, 12.0]]
    assert mat_sub(B, A) == [[4.0, 4.0], [4.0, 4.0]]
    assert mat_transpose(A) == [[1.0, 3.0], [2.0, 4.0]]
    assert mat_mul(A, B) == [[19.0, 22.0], [43.0, 50.0]]
    assert pytest.approx(mat_det(A), rel=1e-12) == -2.0


def test_linear_algebra_inverse_and_solve():
    A = [[4.0, 7.0], [2.0, 6.0]]
    inv = mat_inverse(A)
    # A @ inv == I
    I = mat_mul(A, inv)
    assert pytest.approx(I[0][0], rel=1e-9) == 1.0
    assert pytest.approx(I[1][1], rel=1e-9) == 1.0
    assert pytest.approx(I[0][1], abs=1e-9) == 0.0
    assert pytest.approx(I[1][0], abs=1e-9) == 0.0

    b = [1.0, 0.0]
    x = mat_solve(A, b)
    # Verify Ax == b
    Ax = [A[0][0] * x[0] + A[0][1] * x[1], A[1][0] * x[0] + A[1][1] * x[1]]
    assert pytest.approx(Ax[0], rel=1e-9) == b[0]
    assert pytest.approx(Ax[1], rel=1e-9) == b[1]

    # Singular cases
    S = [[1.0, 2.0], [2.0, 4.0]]
    with pytest.raises(ValueError):
        mat_inverse(S)
    with pytest.raises(ValueError):
        mat_solve(S, [1.0, 2.0])


# -----------------------------
# Complex numbers
# -----------------------------


def test_complex_operations():
    a = 1 + 2j
    b = 3 - 4j
    assert c_add(a, b) == (4 - 2j)
    assert c_sub(a, b) == (-2 + 6j)
    assert c_mul(a, b) == (11 + 2j)
    assert c_conj(a) == (1 - 2j)
    assert pytest.approx(c_abs(a), rel=1e-12) == math.hypot(1, 2)
    assert pytest.approx(c_phase(1 + 0j), abs=1e-12) == 0.0
    assert c_pow(1j, 2) == (-1 + 0j)
    q = c_div(a, b)
    # cross-check with Python's complex division
    assert pytest.approx(q.real, rel=1e-12) == (a / b).real
    assert pytest.approx(q.imag, rel=1e-12) == (a / b).imag
    with pytest.raises(ZeroDivisionError):
        c_div(1 + 1j, 0)
