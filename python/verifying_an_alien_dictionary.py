class Solution(object):
    def isAlienSorted(self, words, order):
        d = {}
        for idx, char in enumerate(order):
            d[char] = idx

        i = 0
        while i < len(words) - 1:
            j = 0
            its = max(len(words[i]), len(words[i + 1]))
            while j < its:
                # correct if the first word is shorter
                if j == len(words[i]):
                    break
                # incorrect if the second word is shorter
                elif j == len(words[i + 1]):
                    return False

                char1 = words[i][j]
                char2 = words[i + 1][j]
                if d[char1] > d[char2]:
                    return False
                elif d[char1] < d[char2]:
                    break
                j += 1

            i += 1
        return True
