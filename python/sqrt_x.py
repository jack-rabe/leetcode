class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        low = 1
        high = x
        while high - 1 > low:
            mid = (high + low + 1) // 2
            ans = mid * mid
            if ans > x:
                high = mid
            elif ans < x:
                low = mid
            else:
                return mid

        return low
