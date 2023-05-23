class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            root = TreeNode(val=val)
            return root
        current = root

        while True:
            if current.val < val:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val=val)
                    break
            elif current.val > val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val=val)
                    break

        return root
