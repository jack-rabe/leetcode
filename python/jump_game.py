class Solution(object):
    def canJump(self, nums):
        max_jump = 0
        for idx, num in enumerate(nums):
            if idx == len(nums) - 1:
                return True

            if num == 0 and max_jump <= 0:
                return False
            else:
                max_jump -= 1
                if num > max_jump:
                    max_jump = num - 1
