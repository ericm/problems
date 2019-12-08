class Solution:
    def hammingWeight(self, n: int) -> int:
        w = 0
        for i in range(32):
            w += 1 if 1 & (n>>i) == 1 else 0
        return w
