from collections import defaultdict #collection is a module
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)# adding the edges
def generate_edge(graph):#function description
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges        
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')    
print(generate_edge(graph))
