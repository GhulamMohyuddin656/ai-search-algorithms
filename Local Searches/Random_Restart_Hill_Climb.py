import random
def heuristic(a,b):
    return abs(ord(a)-ord(b))

def FirstChoiceHillClimb(graph,start,end):
    current=start
    path=[current]
    while current!=end:
        neighbours=graph.get(current,set())
        if not neighbours:
            break
        random_neighbour=list(neighbours)
        random.shuffle(random_neighbour)
        found_better=False
        current_heuristic=heuristic(current,end)
        for neighbour in random_neighbour:
            neighbour_node=neighbour[0]
            if heuristic(neighbour_node,end)<current_heuristic:
                current=neighbour_node
                path.append(current)
                found_better=True
                break
        if not found_better:
            break
    return path
        
        
def RandomRestart(graph,start,end,restarts):
    for i in range(1,restarts+1):
        path=FirstChoiceHillClimb(graph,start,end)
        if path[-1]==end:
            print(f"Path found on Random Restart {i}")
            return path
        else:
            print(f"No path found on Random Restart {i}")
    return None
graph = {
    'A': {'B', 'E'},
    'B': {'A', 'C', 'G'},
    'C': {'B'},
    'D': {'E', 'G'},
    'E': {'A', 'D'},
    'G': {'B', 'D'}
}

start = 'A'
end = 'G'
restarts=10
path=RandomRestart(graph,start,end,restarts)
print(f"Path Found: {' -> '.join(path)}")
