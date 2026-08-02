# Assumptions
# Elementary outcomes

| ID | Ordered draw | Colour pattern | Payoff | Probability |
|---:|---|---|---:|---:|
| 1 | (R1, R2) | two red tokens | +3 | 1/20 |
| 2 | (R1, B1) | one red and one blue token, in either order | +1 | 1/20 |
| 3 | (R1, B2) | one red and one blue token, in either order | +1 | 1/20 |
| 4 | (R1, B3) | one red and one blue token, in either order | +1 | 1/20 |
| 5 | (R2, R1) | two red tokens | +3 | 1/20 |
| 6 | (R2, B1) | one red and one blue token, in either order | +1 | 1/20 |
| 7 | (R2, B2) | one red and one blue token, in either order | +1 | 1/20 |
| 8 | (R2, B3) | one red and one blue token, in either order | +1 | 1/20 |
| 9 | (B1, R1) | one red and one blue token, in either order | +1 | 1/20 |
| 10 | (B1, R2) | one red and one blue token, in either order | +1 | 1/20 |
| 11 | (B1, B2) | two blue tokens | -2 | 1/20 |
| 12 | (B1, B3) | two blue tokens | -2 | 1/20 |
| 13 | (B2, R1) | one red and one blue token, in either order | +1 | 1/20 |
| 14 | (B2, R2) | one red and one blue token, in either order | +1 | 1/20 |
| 15 | (B2, B1) | two blue tokens | -2 | 1/20 |
| 16 | (B2, B3) | two blue tokens | -2 | 1/20 |
| 17 | (B3, R1) | one red and one blue token, in either order | +1 | 1/20 |
| 18 | (B3, R2) | one red and one blue token, in either order | +1 | 1/20 |
| 19 | (B3, B1) | two blue tokens | -2 | 1/20 |
| 20 | (B3, B2) | two blue tokens | -2 | 1/20 |

There are 20 rows because you draw twice, at first there's 5 tokens to draw, which makes 5 options. The second time you draw, there's 4 tokens to draw, which make 4 options. 4 * 5 = 20.
When you first draw, the probability of whichever token is 1/5, then there's 4 left making the probability of any of the tokens left becoming the second 1/4. Multiplying these 2 gives you 1/20.

# Events
A: 2,3,4,6,7,8,9,10,13,14,17,18
B: 1,2,3,4,5,6,7,8
C: 1,2,3,4,5,6,7,8,9,10,13,14,17,18
D: 1,5
  
# Set operations
A ∩ B:1,2,3,4,5,6,7,8,9,10,13,14,17,18
A ∪ D: 1, 2,3,4, 5,6,7,8,9,10,13,14,17,18
not A: 1,4,11,12,15,16,19,20
A ∩ D: This one is impossible because a draw cannot contain exactly 1 red token while having 2 red tokens at the same time.

# Questions

1. How should an ordered draw be represented in the code?
2. What should happen when the model contains fewer than two tokens?
3. How should the code handle an outcome containing an unknown or repeated token?
