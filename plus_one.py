class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                break

            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
        return digits


print(Solution().plusOne([9, 9, 9]))
