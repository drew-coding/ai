from sys import maxsize
from itertools import permutations
V = 4
def travellingSalesman(graph,s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutations = permutations(vertex)
    for i in next_permutations:
        current_path = 0
        k = s
        for j in i:
            current_path += graph[k][j]
            k = j
        current_path += graph[k][s]
        min_path = min(min_path,current_path)
    return min_path
graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]]
s = 0
print(travellingSalesman(graph,s))
