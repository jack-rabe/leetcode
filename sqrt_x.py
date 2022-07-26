# works but causes memory error on Leetcode for large x
# this happens bc of the range function
class Solution(object):
    def mySqrt(self, x):
        lower = 0
        for i in range(x + 1):
            if i * i > x:
                break
            else:
                lower = i
        return lower
