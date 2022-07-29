class Solution(object):
    def addSpaces(self, s, spaces):
        num_spaces = len(spaces)
        ans = []
        i = 0
        more = False

        for idx, char in enumerate(s):
            if i == num_spaces:
                i = idx
                more = True
                break
            if idx == spaces[i]:
                ans += " "
                i += 1
            ans.append(char)

        if more:
            ans.append(s[idx:])
        return "".join(ans)
