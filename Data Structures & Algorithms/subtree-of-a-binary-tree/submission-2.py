# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root1, root2):
            # Both are empty
            if not root1 and not root2:
                return True

            # One is empty, the other isn't
            if not root1 or not root2:
                return False

            # Values don't match
            if root1.val != root2.val:
                return False

            # Check both subtrees
            return (
                sameTree(root1.left, root2.left)
                and sameTree(root1.right, root2.right)
            )

        if not root:
            return False

        # Check if the current node is the start of subRoot
        if root.val == subRoot.val and sameTree(root, subRoot):
            return True

        # Otherwise keep searching
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )