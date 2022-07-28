class Solution(object):
    def strStr(self, haystack, needle):
        idx = 0
        pos = 0
        n_length = len(needle)

        while True:
            char = haystack[pos]

            if char == needle[idx]:
                idx += 1
                if idx == n_length:
                    return pos - n_length + 1
            else:
                if idx:
                    pos -= idx
                idx = 0

            pos += 1
            if pos == len(haystack):
                return -1
