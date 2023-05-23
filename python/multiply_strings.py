# Input: num1 = "2", num2 = "3"
# Output: "6"
class Solution(object):
    def multiply(self, num1, num2):
        total = 0

        pos1 = 1
        for char1 in reversed(num1):
            val1 = int(char1) * pos1
            pos1 *= 10
            pos2 = 1
            for char2 in reversed(num2):
                val2 = int(char2) * pos2
                total += val1 * val2
                pos2 *= 10

        return str(total)
