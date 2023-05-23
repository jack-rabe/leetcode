class Solution(object):
    def isBalanced(self, root):
        def get_height(root):
            if not root:
                return 0
            return max(get_height(root.left), get_height(root.right)) + 1

        if not root:
            return True
        if abs(get_height(root.left) - get_height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
