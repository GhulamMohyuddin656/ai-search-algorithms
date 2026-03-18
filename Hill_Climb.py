def heuristic(a, b):
    return abs(ord(a) - ord(b))

def HillClimb(graph, start, goal):
    current = start
    path = [start]
    
    while current != goal:
        neighbours = graph.get(current, set())
        if not neighbours:
            return path
        
        next_node = None
        best_value = heuristic(current, goal)
        
        for neighbour in neighbours:
            value = heuristic(neighbour, goal)
            if value < best_value:
                best_value = value
                next_node = neighbour
        
        if next_node is None:
            return path
        
        current = next_node
        path.append(current)
    
    return path

graph = {
    'A': {'B', 'E'},
    'B': {'A', 'C', 'G'},
    'C': {'B'},
    'D': {'E', 'G'},
    'E': {'A', 'D'},
    'G': {'B', 'D'}
}

start = 'A'
goal = 'G'
print(HillClimb(graph, start, goal))
