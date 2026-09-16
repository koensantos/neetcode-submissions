# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val_list = []
        def get_list(root):
            if not root:
                return val_list
            get_list(root.left)
            val_list.append(root.val)
            get_list(root.right)
        
        get_list(root)
        val_list.sort()
        return val_list[k - 1]

            
        