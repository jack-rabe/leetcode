class Solution(object):
    def generate(self, numRows):
        ans = [[1]]
        for i in range(1, numRows):
            prev = ans[i - 1]
            new = [1]
            for j in range(len(prev) - 1):
                new.append(prev[j] + prev[j + 1])

            new.append(1)
            ans.append(new)
        return ans
