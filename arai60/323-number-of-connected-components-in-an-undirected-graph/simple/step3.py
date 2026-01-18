class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for component1, component2 in edges:
            adjacency_list[component1].append(component2)
            adjacency_list[component2].append(component1)
        traversed_components = set()
        def traverse_connected_components(component):
            if component in traversed_components:
                return
            traversed_components.add(component)
            for next_component in adjacency_list[component]:
                traverse_connected_components(next_component)
        
        num_of_connected_components = 0
        for component in range(n):
            if component in traversed_components:
                continue
            traverse_connected_components(component)
            num_of_connected_components += 1
        return num_of_connected_components

class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for component1, component2 in edges:
            adjacency_list[component1].append(component2)
            adjacency_list[component2].append(component1)
        traversed_components = set()
        def traverse_connected_components(component):
            queue = deque([component])
            while queue:
                next_component = queue.popleft()
                if next_component in traversed_components:
                    continue
                traversed_components.add(next_component)
                for neighbor in adjacency_list[next_component]:
                    queue.append(neighbor)
        
        num_of_connected_components = 0
        for component in range(n):
            if component in traversed_components:
                continue
            traverse_connected_components(component)
            num_of_connected_components += 1
        return num_of_connected_components
