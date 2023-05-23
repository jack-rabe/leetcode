class Solution(object):
    def sumNumbers(self, root):
        def helper(root, path, total):
            if not root:
                return 0
            new_path = path + str(root.val)
            if not root.left and not root.right:
                total += int(new_path)
                return total
            return helper(root.left, new_path, total) + helper(
                root.right, new_path, total
            )

        return helper(root, "", 0)
