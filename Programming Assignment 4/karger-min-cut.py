import random
file = open('kargerMinCut.txt')

adjacencyList = {}
for row in file :
    rowLst= row.split('\t')
    adjacencyList[rowLst[0]] = rowLst[1:-1]
def minCut(graph):
   
    if(len(graph) <= 2):
        return 
    #Merging
    keys = list(graph.keys())
    u = random.choice(keys)
    v = random.choice(graph[u])
    graph[u]= graph[u] + graph[v]
    newVal = []
    for key, value in graph.items():
        if(key == u):
            for i in range(len(value)):
                if(value[i] != v and value[i] != u):
                    newVal.append(value[i])
        else:
            for i in range(len(value)):
                if value[i] == v:
                    value[i]= u
    
    graph[u]  = newVal
    del graph[v]
    return minCut(graph)
minCut(adjacencyList)
min = 10000000
for [key,value] in adjacencyList.items():
    if(len(value) < min):
        min = len(value)
print(min)