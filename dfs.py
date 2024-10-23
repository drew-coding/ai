def DFS(graph,node,path=[]):
    path+=[node]
    for neighbour in graph[node]:
        if neighbour not in path:
            path=DFS(graph,neighbour,path)
    return path
graph1={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','E','F'],
    'D':['B','G','H'],
    'E':['B','C','I'],
    'F':['C'],
    'G':['D'],
    'H':['D'],
    'I':['E']
    }

print(DFS(graph1,'A'))            
