from collections import deque
def DFS(graph,start,end,Trav):
    stack=[start]
    visited=set()
    parent={start:None}
    while stack:
        current=stack.pop()
        if current not in visited:
            visited.add(current)
            Trav.append(current)
        for i in graph[current]:
            if i not in visited and i not in parent:
                stack.append(i)
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
path=DFS(graph,"Ali","Qasim",Trav)
if path:
    print("Path is : ",path)
    print("DFS Traversal is : ",Trav)
    print("Time Complexity O(V+E)")
    print("Space Complexity O(V)")
else:
    print("Path not found")         