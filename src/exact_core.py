from itertools import permutations


def enumerate_ordered_draws(r: int, b: int, k: int) -> tuple[tuple[str, ...], ...]:
    if not all(isinstance(x, int) for x in (r, b, k)):
        raise TypeError("r, b and k must all be integers")
    elif r < 0 or b < 0 or k < 2 or k > r + b:
        raise ValueError("Invalid input(s)")
    labels = tuple(f"{color}{number}" for color in ["R", "B"] for number in range(1, r + 1 if color == "R" else b + 1))
    return tuple(permutations(labels, k))

print(enumerate_ordered_draws(4, 5, 3))


