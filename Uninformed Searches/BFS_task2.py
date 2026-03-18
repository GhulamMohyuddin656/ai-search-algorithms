from collections import deque
def BFS(graph,start,end,Trav):
    queue=deque([start])
    visited=set()
    parent={start:None}
    while queue:
        current=queue.popleft()
        if current not in visited:
            visited.add(current)
            Trav.append(current)
        for i in graph[current]:
            if i not in visited and i not in parent:
                queue.append(i)
                parent[i]=current
        if current==end:
            path=[]
            while current is not None:
                path.append(current)
                current=parent[current]
            return path[::-1]
    return []


graph={1:{2},
       2:{1,3,7},
       3:{2,4,8},
       4:{3,5},
       5:{4,10},
       6:{7,11},
       7:{2,6,12},
       8:{3},
       9:{14},
       10:{5},
       11:{6,12,16},
       12:{7,11},
       13:{},
       14:{9,19},
       15:{},
       16:{11,17},
       17:{16,22},
       18:{23,19},
       19:{18,14,24},
       20:{},
       21:{},
       22:{17,23},
       23:{18,22},
       24:{19,25},
       25:{24},}
Trav=[]
path=[]
path=BFS(graph,1,25,Trav)
if path:
    print("Path is : ",path)
    print("BFS Traversal is : ",Trav)
    print("Time Complexity O(V+E)")
    print("Space Complexity O(V)")
else:
    print("Path not found")         