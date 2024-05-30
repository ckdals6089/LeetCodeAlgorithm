class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a:int = 1
        b:int = 2

        for i in range(3, n + 1):
            c:int = a + b
            a = b
            b = c

        return b