class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(current_node, visited):
            if current_node is None or current_node in visited:
                return visited
            visited.add(current_node)
            for node in graph[current_node]:
                visited = dfs(node, visited)
            return visited
            
        graph = [[] for i in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
                
        visited_ovr = set()
        visited_ths = set()
        count = 0

        for i in range(len(graph)):
            if i in visited_ovr:
                continue
            count += 1
            visited_ths = dfs(i, set())
            visited_ovr = visited_ovr.union(visited_ths)

        return count