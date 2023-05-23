class Solution(object):
    def minTimeToType(self, word):
        ans = 0
        idx = ord("a") % 26

        for char in word:
            new_idx = ord(char) % 26
            diff = abs(new_idx - idx)
            diff = min(diff, 26 - diff)
            ans += diff + 1
            idx = new_idx

        return ans
