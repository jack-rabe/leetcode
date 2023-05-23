class Solution(object):
    def findMode(self, root):
        d = {}

        def helper(node):
            if not node:
                return
            if not d.get(node.val):
                d[node.val] = 1
            else:
                d[node.val] += 1

            helper(node.right)
            helper(node.left)

        helper(root)

        max_k = None
        max_v = None
        for k, v in d.items():
            if not max_k or max_v < v:
                max_v = v
                max_k = [k]
            elif max_v == v:
                max_k.append(k)
        return max_k
