# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.class Solution(object):
class Solution(object):
    def isHappy(self, n):
        def helper(n, d={}):
            if n in d:
                return False
            elif n == 1:
                return True
            else:
                d[n] = 1

            digitsSum = sum([int(digit) * int(digit) for digit in str(n)])
            return helper(digitsSum)

        return helper(n)


x = Solution()
print(x.isHappy(2))
