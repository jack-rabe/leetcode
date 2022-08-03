class Solution(object):
    def uniquePaths(self, m, n):
        def helper(x, y, d={}):
            if m - 1 == x and n - 1 == y:
                return 1
            elif (x, y) in d:
                return d[x, y]

            total = 0
            if x + 1 < m:
                total += helper(x + 1, y)
            if y + 1 < n:
                total += helper(x, y + 1)

            d[(x, y)] = total
            return total

        return helper(0, 0)


print(Solution().uniquePaths(3, 7))
