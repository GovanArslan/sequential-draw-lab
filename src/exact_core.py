from collections import Counter
from collections.abc import Callable
from fractions import Fraction

def create_draws(labels: tuple[str, ...], k: int) -> tuple[tuple[str, ...], ...]: # type: ignore
    if k == 0:
        return ((), )
    results = []
    for i, label in enumerate(labels):
        smaller_draws = create_draws(labels[:i] + labels[i+1:], k - 1)
        for smaller_draw in smaller_draws:
            results.append((label, ) + smaller_draw)
    return tuple(results)
         

def enumerate_ordered_draws(r: int, b: int, k: int) -> tuple[tuple[str, ...], ...]:
    if not all(isinstance(x, int) for x in (r, b, k)):
        raise TypeError("r, b and k must all be integers")
    if r < 0 or b < 0 or k < 2 or k > r + b:
        raise ValueError("Invalid input(s)")
    labels = tuple(f"{color}{number}" for color in ["R", "B"] for number in range(1, r + 1 if color == "R" else b + 1))
    return create_draws(labels, k)


def red_count(draw: tuple[str, ...]) -> int:
    return sum(1 for label in draw if label[0] == "R")

def nonlinear_payoff(x: int) -> int:
    return x**2 - 2 * x - 1

def y_pmf(r: int, b: int, k: int) -> dict:
    support_x = [sum(1 for prev, curr in zip(draw, draw[1:]) if prev[0] != curr[0]) for draw in enumerate_stable_draws(r, b, k)]
    return dict(Counter(support_x))


def payoff_pmf(r: int, b: int, k: int, payoff_rule: Callable[[int], int]) -> dict:
    nonlinear_results = dict(Counter(payoff_rule(red_count(draw)) for draw in enumerate_ordered_draws(r, b, k)))
    return {key: Fraction(value, sum(nonlinear_results.values())) for key, value in nonlinear_results.items()}


def enumerate_stable_draws(r: int, b: int, k: int) -> tuple[tuple[str, ...], ...]:
    if not all(isinstance(x, int) for x in (r, b, k)):
            raise TypeError("r, b and k must all be integers")
    if r < 0 or b < 0 or k < 2 or k > r + b:
        raise ValueError("Invalid input(s)")
    labels = tuple(f"{color}{number}" for color in ("R", "B") for number in range (1, r + 1 if color == "R" else b + 1))
    return create_stable_draws((labels, {"R": 0, "B": 0}, False), k)

def create_stable_draws(package: tuple[tuple[str, ...], dict[str, int], bool], k: int) -> tuple[tuple[str, ...], ...]:
    if k == 0:
        return ((), )
    results = []
    labels, counts, forbidden_adjacent = package
    for i, label in enumerate(labels):
        if label in ("R1", "B1") and forbidden_adjacent == True:
            forbidden_adjacent_copy = False
            continue
        forbidden_adjacent_copy = label in ("R1", "B1")
        if counts[label[0]] == 2:
            continue
        counts_copy = counts.copy()
        counts_copy.update({"R" : counts["R"] + 1, "B": 0} if label[0] == "R" else {"B" : counts["B"] + 1, "R": 0})
        smaller_draws = create_stable_draws((labels[:i] + labels[i+1:], counts_copy, forbidden_adjacent_copy), k - 1)
        for smaller_draw in smaller_draws:
            results.append((label, ) + smaller_draw)
        
    return tuple(results)


print(y_pmf(4, 4, 5))


