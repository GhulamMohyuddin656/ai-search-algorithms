import heapq
def heuristic(a,b):
    return abs(ord(a)-ord(b))

def A_star(graph,start,goal):
    list=[(0,start,[start])]
    visited=set()
    while list:
        cost,node,path=heapq.heappop(list)
        if node==goal:
            return path
        if node not in visited:
            visited.add(node)
            for weight,neighbour in graph[node]:
                if neighbour not in visited:
                    new_cost=cost+weight+heuristic(neighbour,goal)
                    new_path=path+[neighbour]
                heapq.heappush(list,(new_cost,neighbour,new_path))
    return None 

graph={'A':{(2,'B'),(3,'E')},
       'B':{(2,'A'),(1,'C'),(9,'G')},
       'C':{(1,'B')},
       'D':{(6,'E'),(1,'G')},
       'E':{(3,'A'),(6,'D')},
       'G':{(9,'B'),(1,'D')}
       }
start='A'
goal='G'
path=A_star(graph,start,goal)
print(path)