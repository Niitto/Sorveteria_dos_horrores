# class Vertex:
#     #connections = []
#     def __init__(self, name):
#         self.name = name
#         self.connections = []
    
#     def add(self, name):
#         self.connections.append(name)

# class Graph:
#     def __init__(self, dict):
#         self.dict = dict 


myGraph = {}

with open('caso2.txt', 'r') as file:
    
    f = file.readlines()

for line in f:
    words = line.replace('\n', '').split(' -> ')
    key = words[0]
    value = words[1]
    if key not in myGraph:
        #valueList = [value]
        #print(value)
        myGraph[key] = []

    myGraph[key].append(value)

    if value not in myGraph:
        myGraph.setdefault(value, [])

print("Dicionário:\n", myGraph)

class Vertex:

    def __init__(self, name):
        self.name = name
        self.connections = []
        self.color = 'w'
    def add(self, name):
        self.connections.append(name)

class Graph:
    
    visited = set(())
    combine = []
    combinations = set(())
    
    def __init__(self, dict):
        self.dict = dict 
    
    global twosum_count
    global threesum_count
    #twosum_count = 0
    #threesum_count = 0

    def dfs(self, g, visited):    
        # visited = set(())
        # combine = []
        # combinations = set(())
        #combinations_three = set(())      # [...,i,j,k,...]
        #combinations_two = set(())  
        combine_count = 0 
        twosum_count = 0
        threesum_count = 0
        objective = firstOnes(g)
        for v in objective:
            print("\nIndice: ",i)
            dfs_visit(v, g, visited, combine, combine_count, combinations)
        print("\nTotal de combinações de sorvetes: ")#, combinations)
        for e in combinations:
            if len(e) == 2: 
                twosum_count += 1
            else: 
                threesum_count += 1
            print("\n", e)
        print("\nTotal de combinacoes de 2 sabores: ", twosum_count)
        print("\nTotal de combinacoes de 3 sabores: ", threesum_count)
        
    def dfs_visit(self, vertex, graph, visited, combine, combine_count, combinations): 
        visited.add(vertex)
        combine.append(vertex)
        combine_count += 1
        print("\nSabor: ", vertex)
        print("Combinacoes: ", combine)
        for j in graph[vertex]:
            if j not in visited:
                dfs_visit(j, graph, visited, combine, combine_count, combinations)
            elif j in visited and j not in combine:
                dfs_visit(j, graph, visited, combine, combine_count, combinations)  
        calcula(combine, combinations)
        combine.pop(combine.index(vertex))
        combine_count -= 1
        return vertex

    def firstOnes(self, g):
        k = set(())
        v = set(())
        for i in g:
            #print("\ni: ", i)
            v.update(g[i])
            #print("values: ", v)
            k.add(i)
            print("\nIndex",i,": ", k,"-->", v)
            k.difference_update(v)
            print("\nNew key(s): ", k)
        return list(k)


for i in myGraph:
    print("key - value:")
    print("key: ", i, " --> ", "value: ", myGraph[i])
    # print("Tipo myGraph[i]: ", type(myGraph[i]))
    # print("Tipo myGraph.get(i): ", type(myGraph.get(i)))

print(firstOnes(myGraph))
objetivo = firstOnes(myGraph)
print("\nObjevtive: ",objetivo)
dfs(myGraph)
