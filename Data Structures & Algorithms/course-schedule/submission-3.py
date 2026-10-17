class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         
        class Node:

            def __init__(self, val, next):
                self.val = val
                self.next = next

        def backtrack(node, seen, seen_ovr):
            for j in range(len(node.next)):
                if node.next[j] in seen_ovr:
                    continue
                if node.next[j] in seen:
                    return False
                else:
                    seen.add(node.next[j])
                    if not backtrack(node.next[j], seen, seen_ovr):
                        return False
                    seen.remove(node.next[j])
            seen_ovr.add(node)
            return True

        nodes_hashmap = {}
        for prerequisite in prerequisites:
            c1, c2 = prerequisite
            if c1 in nodes_hashmap:
                c1_node = nodes_hashmap[c1]
            else:
                c1_node = Node(c1, [])
                nodes_hashmap[c1] = c1_node
            if c2 in nodes_hashmap:
                c2_node = nodes_hashmap[c2]
            else:
                c2_node = Node(c2, [])
                nodes_hashmap[c2] = c2_node
            c1_node.next.append(c2_node)

        seen_ovr = set()
        for node in nodes_hashmap.values():
            seen = {node}
            if not backtrack(node, seen, seen_ovr):
                return False
        
        return True
                