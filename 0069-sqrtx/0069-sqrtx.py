class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x >> 1

        while left <= right:
            mid = (left + right) >> 1
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
