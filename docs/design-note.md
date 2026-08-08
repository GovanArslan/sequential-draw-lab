# Exact-analysis boundary

## Outcome construction
Outcome construction is responsible for constructing all valid ordered draws. It receives the models parameters and produces a collection of all valid ordered draws. It guarantees that no valid outcome is missing or duplicated. It does not calculate payoff, or probabilities, or use random sampling.

## Outcome mapping
Outcome mapping is responsible for mapping a single outcome it receives to at least one statistic, such as "red count" or payoff", which it returns. It must not calculate probabilities, use random sampling, or construct outcomes.

## Exact-probability calculation
Exact-probability calculation receives a complete collection of valid outcomes in addition to an event condition. Assuming draws are fair, it returns the fraction of valid outcomes that satisfy the condition. It must not calculate payoff, use random sampling, or construct outcomes.

## Separation from future random sampling.
The exact-analysis part must not depend on random sampling. It must always return deterministic results from the complete outcome collection, whereas future sampling produces estimates from random trials.
