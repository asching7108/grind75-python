"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        newNode = Node(node.val)
        self.visited[node] = newNode

        newNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return newNode

# Time complexity: O(n + m) where n is the number of nodes and n is the number of edges.
# Space complexity: O(n)