
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        oldToNew = {}

        def dfs(node):
            # base case
            if node in oldToNew:
                return oldToNew[node]

            # create clone
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # create copies of every single neighbor
            for neighbor in node.neighbors:
                # return created copy and its list of neighbors
                copy.neighbors.append(dfs(neighbor))
            return copy

        # edge case
        # original node could be null
        return dfs(node) if node else None 

        # T: O(V + E)
        # S: O(E)