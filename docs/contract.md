# Sequential Draw Lab contract

## `enumerate_ordered_draws(r, b, k)`

### Input
- r: Amount of red labelled tokens.
- b: Amount of blue labelled tokens.
- k: Amount of tokens drawn.


### Preconditions
- r is an Integer equal to or greater than 0.
- b is an Integer equal to or greater than 0.
- k is an Integer equal to or lesser than `r + b`, and equal to or greater than 2.

### Postconditions 
- Available labels are {R1, ..., Rr} U {B1, ..., Bb}.
- An additional tuple of tuples is returned. Each inner tuple contains 1 draw.
- Each inner tuple consists of a draw, it contains distinct valid labels and represents one ordered draw. No valid draw is missing or repeated.
- Within a draw, no token is repeated.
- The order in which returned draws appear is not part of the public contract.
 
### Invalid inputs
- If r, b or k is not an Integer, a TypeError will be raised.
- If k is greater than `r + b` a ValueError will be raised.
- If r or b is below zero, a ValueError will be raised.
- If k < 2, raise ValueError.

### Side effects
- Does not print, write files, mutate external state, or modify inputs. 

### Pure function
Yes, the function neither has side effects nor returns different results when given the same inputs.

## `red_count(draw)`
Precondition: `draw` is one valid ordered draw produces under the model contract.
Postcondition: returns an Integer from `0` through `len(draw)` equal to the number of labels beginning with `R`.

## `nonlinear_payoff(x)`
Precondition: x is a non-negative integer red count.
Postcondition: returns Y = x^2 - 2x - 1.

The function is pure because its result is deterministic and it has no side effects.

## `payoff_pmf(r, b, k, payoff_rule)`

### Preconditions
- `r`, `b` and `k` must satisfy the preconditions of `enumerate_ordered_draws(r, b, k)`.
- `payoff_rule` must be deterministic, have no side effects, and return a numeric payoff for every red count produced by the model.

### Postconditions
- Returns a mapping from every attained payoff value to its exact probability represented as a `Fraction`.
- Payoff values that can be produced by multiple red counts are represented exactly once, with the sum of their probabilities.
- Every mass is positive and all masses sum to exactly `1`.
- The ordering of entries is not part of the contract.

### Invalid inputs
- Invalid `r`, `b` or `k` values produce the same documented exceptions as `enumerate_ordered_draws(r, b, k)`

The function is pure because its result is deterministic and it has no side effects.
