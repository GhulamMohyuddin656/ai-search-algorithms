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
path=FirstChoiceHillClimb(graph,start,end)
print(f"Path From {start} to {end}: {' -> '.join(path)}")
