# Test Strategy

## Valid smallest model
- Checks the smallest valid two-colour model, where only two ordered draws exist.
- `enumerate_ordered_draws(1, 1, 2)`

## One-colour valid model
- Checks that enumeration does not depend on both colours being present.
- `enumerate_ordered_draws(0, 5, 3)`

## Balanced colour counts
- Checks symmetric two-colour label generation and enumeration.
- `enumerate_ordered_draws(3, 3, 3)`

## Unbalanced colour counts
- Checks that having more labels of one colour does not omit, duplicate, or incorrectly assign labels.
- `enumerate_ordered_draws(2, 5, 3)`

## Lower valid boundary for k
- Checks the lowest permitted draw count, `k = 2`, using both colours.
- `enumerate_ordered_draws(4, 5, 2)`

## Upper valid boundary for k
- Checks `k = n`, where every available label must appear in each draw.
- `enumerate_ordered_draws(3, 3, 6)`

## Negative counts
- Checks that negative red and blue counts are rejected independently.
- `enumerate_ordered_draws(-1, 5, 2)`
- `enumerate_ordered_draws(4, -1, 2)`

## k below its valid boundary
- Checks that `k < 2` is rejected.
- `enumerate_ordered_draws(2, 5, 1)`

## Non-integer inputs
- Checks that every public parameter rejects a non-integer value.
- `enumerate_ordered_draws("2", 5, 2)`
- `enumerate_ordered_draws(2, "5", 2)`
- `enumerate_ordered_draws(2, 5, "2")`

## Insufficient total tokens
- Checks a valid-looking `k = 2` when fewer than two tokens exist.
- `enumerate_ordered_draws(0, 1, 2)`

## Malformed or repeated-label outcomes
- Not applicable to `enumerate_ordered_draws`, because callers do not supply outcomes to this operation.
