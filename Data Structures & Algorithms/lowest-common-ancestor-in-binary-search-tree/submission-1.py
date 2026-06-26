# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Iteration

        # while cur in not Null
        # if the p value and q value is greater than root value 
        # go down to right subtree
        # if the p value and q value is less than root value 
        # go down left subtree
        # last case: if we find one of the values p or q, means we found our result
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


        
        # T: O(h) height of the tree, visiting one node at a every level
        # S: O(1) not using any DS