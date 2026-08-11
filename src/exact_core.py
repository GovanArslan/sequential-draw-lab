def create_draws(labels: tuple[str, ...], k: int) -> tuple[tuple[str, ...], ...]:
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



