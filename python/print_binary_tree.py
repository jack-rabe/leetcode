class Solution(object):
    def printTree(self, root):
        def get_height(node):
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        # construct m x n matrix
        ans = []
        h = get_height(root)
        rows = h
        cols = 2**h - 1
        for _i in range(rows):
            ans.append(["" for _x in range(cols)])

        mid = int(cols / 2)

        def insert(node, m, n):
            if not node:
                return
            ans[m][n] = str(node.val)
            insert(node.left, m + 1, n - 2 ** (h - m - 2))
            insert(node.right, m + 1, n + 2 ** (h - m - 2))

        insert(root, 0, mid)
        return ans
