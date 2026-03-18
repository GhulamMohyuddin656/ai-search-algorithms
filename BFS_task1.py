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


graph = {
    "Ali": {"Hamza"},
    "Hamza": {"Ali", "Hammad", "Fahad", "Akram"},
    "Hammad": {"Hamza", "Bilal"},
    "Bilal": {"Hammad", "Akram"},
    "Akram": {"Bilal", "Hamza", "Qasim", "Shoaib"},
    "Qasim": {"Akram"},
    "Shoaib": {"Akram", "Fahad"},
    "Fahad": {"Hamza", "Shoaib"}
}
Trav=[]
path=[]
path=BFS(graph,"Ali","Qasim",Trav)
if path:
    print("Path is : ",path)
    print("BFS Traversal is : ",Trav)
    print("Time Complexity O(V+E)")
    print("Space Complexity O(V)")
else:
    print("Path not found")         