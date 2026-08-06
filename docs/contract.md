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

