# Exact-analysis boundary

## Outcome construction
Outcome construction is responsible for constructing all valid ordered draws. It receives the model's parameters and produces a collection of all valid ordered draws. It guarantees that no valid outcome is missing or duplicated. It does not calculate payoff, or probabilities, or use random sampling.

## Outcome mapping
Outcome mapping is responsible for mapping a single outcome it receives to at least one statistic, such as `red count` or `payoff`, which it returns. It must not calculate probabilities, use random sampling, or construct outcomes.

## Exact-probability calculation
Exact-probability calculation receives a complete collection of valid outcomes in addition to an event condition. Assuming draws are fair, it returns the fraction of valid outcomes that satisfy the condition. It must not calculate payoff, use random sampling, or construct outcomes.

## Separation from future random sampling.
The exact-analysis part must not depend on random sampling. It must always return deterministic results from the complete outcome collection, whereas future sampling produces estimates from random trials.

## Pre-code review
- Public operation: `enumerate_ordered_draws(r, b, k)`
- Invariants:
  1. No returned draw repeats a label;
  2. Every returned draw has length `k`;
  3. Every possible draw is returned exactly once
- The exact tests that would expose violations when present, the operation is called with the specific valid model `r=4, b=5, k=3`:
  1. Every returned draw is checked to contain exactly 3 distinct labels. If 1 label appears twice or more in the same draw, the draw will count as a violation.
  2. If a draw has a length that is not exactly 3, it will count as a violation.
  4. Exactly 9 * 8 * 7= 504 draws appear in the returned tuple of tuples.
  5. In the returned collection, no draw appears more than once.
  6. Every returned draw is checked against the contract’s valid-label rule: each label must belong to `{R1, R2, R3, R4, B1, B2, B3, B4, B5}`.
