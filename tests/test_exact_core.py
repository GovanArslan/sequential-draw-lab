from src.exact_core import enumerate_ordered_draws, payoff_pmf, nonlinear_payoff
from math import factorial
from fractions import Fraction
import pytest

# Postconditions
@pytest.fixture(params=[
    (4, 5, 3),
    (2, 2, 2),
    (0, 4, 3),
    (1, 1, 2)
])
def case(request):
    r, b, k = request.param
    return enumerate_ordered_draws(r, b, k), r, b, k

def test_repeating_draws(case):
    draws, r, b, k = case
    assert len(draws) != len(set(draws))

def test_draw_structure(case):
    draws, r, b, k = case
    assert all(len(draw) == k == len(set(draw)) for draw in draws) 
    assert all(label[0] in ["R", "B"] and int(label[1:]) in range(1, r + 1 if label[0] == "R" else b + 1) for draw in draws for label in draw)

def test_possible_draws(case):
    draws, r, b, k = case
    assert len(draws) == factorial(r + b) // factorial(r + b - k)


# Preconditions

@pytest.mark.parametrize(
    "r, b, k",
    [
        ("4", 5, 3),
        (4, "5", 3),
        (4, 5, "3")
    ]
)
def test_invalid_type(r, b, k):
    with pytest.raises(TypeError):
        enumerate_ordered_draws(r, b, k)


@pytest.mark.parametrize(
    "r, b, k",
    [
        (2, 3, 20),
        (-1, 5, 2),
        (5, -2, 2),
        (2, 5, 1),
    ]
)
def test_invalid_value(r, b, k):
    with pytest.raises(ValueError):
        enumerate_ordered_draws(r, b, k)


# PMF RULE 

@pytest.mark.parametrize(
    "r, b, k, function",
    [
        (3, 4, 2, lambda x: 100 * x),
    ]
) 
def test_payoff_pmf(r, b, k, function):
    assert payoff_pmf(r, b, k, function) == {0: Fraction(12,42), 100: Fraction(24,42), 200: Fraction(6,42)}