def smallestEvenMultiple(n: int) -> int:
    return n if n % 2 == 0 else n * 2
# -----------------------------------------
# if n == 1:
#     return 2
# elif n % 2 == 0:
#     return n
# else:
#     return n * 2
# -------------------------------
from functools import partial
from math import lcm

class Solution:
    n = 87
    print(smallestEvenMultiple(n))
