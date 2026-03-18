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
       25:{24}}

start=1
end=25

if IDLS(graph,start,end):
    print("Time Complexity O(b^d)")
    print("Space Complexity O(b*d)")
else:
    print("Path not found")