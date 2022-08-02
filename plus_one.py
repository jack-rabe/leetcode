class Solution(object):
    def plusOne(self, digits):
        nums = []
        for digit in digits:
            nums.append(str(digit))
        ans = int("".join(nums))
        ans += 1
        ans = str(ans)
        return [*ans]
