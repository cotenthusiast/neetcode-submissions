"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def recursive_copy(node, visited):
            if node is None:
                return

            new_node = Node(node.val)
            neighbors = []
            visited[node] = new_node

            for i in range(len(node.neighbors)):
                if node.neighbors[i] in visited:
                    neighbors.append(visited[node.neighbors[i]])
                else:
                    neighbour = recursive_copy(node.neighbors[i], visited)
                    neighbors.append(neighbour)
                
            new_node.neighbors = neighbors
            return new_node

        return recursive_copy(node, {})