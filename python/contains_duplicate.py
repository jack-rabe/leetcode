class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for num in nums:
            if num in d:
                return True
            d[num] = 1
        return False
