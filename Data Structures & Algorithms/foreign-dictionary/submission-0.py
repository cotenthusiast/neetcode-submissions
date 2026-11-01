
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def insert_edge(a: str, b: str, graph: Dict[str, set[str]]) -> None:
            if a in graph:
                graph[a].add(b)
            else:
                graph[a] = set([b])
        
        def insert_node(a: str, graph: Dict[str, set[str]]) -> None:
            if a not in graph:
                graph[a] = set()

        def dfs(node, alien_alphabet):
            for neigh in graph[node]:
                if states[neigh] == 1:
                    return False
                if states[neigh] == 2:
                    continue
                states[neigh] = 1
                if not dfs(neigh, alien_alphabet):
                    return False
            alien_alphabet.append(node)
            states[node] = 2
            return True
            
        # ====== setting up the graph =====================================================================

        graph = {}

        for c in words[0]:
            insert_node(c, graph)

        for i in range(1, len(words)):
            
            prev = words[i-1]
            current = words[i]
            directed_node = False

            if len(prev) > len(current) and current == prev[0:len(current)]:
                return ""

            for j in range(min(len(prev), len(current))):
                c1 = prev[j]
                c2 = current[j]
                insert_node(c1, graph)
                insert_node(c2, graph)

                if c1 != c2 and not directed_node:
                    insert_edge(c1, c2, graph)
                    directed_node = True

            for k in range(min(len(prev), len(current)), max(len(prev), len(current))):
                if len(prev) <= k:  # current is the longer one
                    insert_node(current[k], graph)
                else:
                    insert_node(prev[k], graph)

        # ====== topological sort ==========================================================================

        states = {}
        alien_alphabet = []

        for node in graph:
            states[node] = 0
        for node in graph:
            if states[node] == 2:
                continue
            states[node] = 1
            if not dfs(node, alien_alphabet):
                return ""
        alien_alphabet = "".join(alien_alphabet)
        return alien_alphabet[::-1]
