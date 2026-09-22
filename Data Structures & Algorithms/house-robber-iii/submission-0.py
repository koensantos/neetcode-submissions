# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #Check each house starting from root.
        #If there exists every other house, rob it and store the result
        #Get the max result on each path.

        #If not root
            #return 0
        #if root.left.left does not exist check root.left.right
        #if root.left.left and right do not exist, just return root.val.
        #find max if current result and idk

        def dfs(root):
            if not root:
                return [0,0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
        return max(dfs(root))
        
        

        
        

