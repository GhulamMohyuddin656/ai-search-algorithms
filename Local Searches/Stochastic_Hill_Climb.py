import random
def heuristic(a,b):
    return abs(ord(a)-ord(b))

def stochastic_hill_climb(graph,start,end):
    current=start
    path=[current]
    while current!=end:
        neighbours=graph.get(current,set())
        if not neighbours:
            break
        current_heuristic=heuristic(current,end)
        better_neighbour=[neighbour for neighbour in neighbours 
                          if heuristic(neighbour[0],end)<current_heuristic]
        if not better_neighbour:
            break
        next_node=random.choice(better_neighbour)[0]
        current=next_node
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
end = 'G'
path=stochastic_hill_climb(graph,start,end,)
print(f"Path Found: {' -> '.join(path)}")


