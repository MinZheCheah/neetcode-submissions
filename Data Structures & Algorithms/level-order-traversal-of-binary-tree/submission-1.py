# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case
        # if tree is empty return empty list
        if not root:
            return []

        # init BFS queue with root node
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue) # capture current level's node count (go though each level)
            level = [] # temp list to collect values of cur level

            # iterate through every level
            for i in range(level_size):
                node = queue.popleft() # dequeue the next node in FIFO order
                level.append(node.val) # append value in the current level list
                # enqueue children for next level (left to right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # append the list into our results
            result.append(level)
        
        return result

        # T: O(n)
        # S: O(n)
        

        
        