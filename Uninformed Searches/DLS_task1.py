def DLS(graph,start,end,visited,parent,limit):
    if start not in visited:
        visited.add(start)
        if limit<0:return None
        if start==end:
            path=[]
            while start is not None:
                path.append(start)
                start=parent[start]
            return path[::-1]
        for i in graph[start]:
            if i not in visited and i not in parent:
                parent[i]=start
                result=DLS(graph,i,end,visited,parent,limit-1)
                if result:
                    return result

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
path=[]
visited=set()
start = "Ali"
end = "Qasim"
parent={start:None}
limit=15
path=DLS(graph,start,end,visited,parent,limit)
if path:
    print("Path is :",path)
    print("Time Complexity O(b^d)")
    print("Space Complexity O(b*d)")
else:
    print("Path not found within depth limit")         