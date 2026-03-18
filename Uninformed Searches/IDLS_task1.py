def DLS(graph,start,end,visited,parent,limit):

    if limit < 0:
        return False

    if start not in visited:
        visited.add(start)

        if start == end:
            path=[]
            while start is not None:
                path.append(start)
                start = parent[start]
            print("Path :", path[::-1])
            return True

        for i in graph[start]:
            if i not in visited:
                parent[i] = start
                if DLS(graph,i,end,visited,parent,limit-1):
                    return True

    return False


def IDLS(graph,start,end):

    if end not in graph:
        return False

    limit = 0

    while True:

        visited=set()
        parent={start:None}

        if DLS(graph,start,end,visited,parent,limit):
            return True

        print("Depth limit",limit,"searched")
        limit += 1
        
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
start="Ali"
end="Qasim"

if IDLS(graph,start,end):
    print("Time Complexity O(b^d)")
    print("Space Complexity O(b*d)")
else:
    print("Path not found")