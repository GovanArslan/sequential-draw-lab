from src.exact_core import enumerate_ordered_draws
from math import factorial
import pytest

# Postconditions

@pytest.fixture
def case():
    r, b, k = 4, 5, 3
    return enumerate_ordered_draws(r, b, k), r, b, k

def test_repeating_draws(case):
    draws, r, b, k = case
    assert len(draws) == len(set(draws))

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