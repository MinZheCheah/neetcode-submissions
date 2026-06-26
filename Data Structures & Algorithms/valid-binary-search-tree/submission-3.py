# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS
        # (min/max bounds) along recursion stack
        # base case: when tree empty return true 
        
        # traverse through left subtree
        # left_valid = check if left subtree nodes value less than root
        # right_valid = check if right subtree nodes value is greater than root

        def dfs(node, min_val, max_val):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            left_valid = dfs(node.left, min_val, node.val)
            right_valid = dfs(node.right, node.val, max_val)

            return left_valid and right_valid


        return dfs(root, float('-inf'), float('+inf'))

    
        # T: O(n)
        # S: O(h) worst case O(n), best case O(log n)