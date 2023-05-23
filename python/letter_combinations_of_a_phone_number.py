class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        d = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        ans = []

        def helper(string, idx=0):
            if idx == len(digits):
                ans.append(string)
                return

            for char in d[int(digits[idx])]:
                helper(string + char, idx + 1)

        helper("")
        return ans
