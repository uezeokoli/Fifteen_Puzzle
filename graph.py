# author: Ugonna Ezeokoli
# date: March 14, 2023
# file: graph.py a Python program that imitates the functionality of a Vertex and Graph abstract data type
# input: takes in key when Vertex is initiated
# output: outputs connection to other verticies 



class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}  #dictonary which the keys are a vertex object and the values are the id of the vertex
        self.color = 'white'

    # 
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight  

    # overides str() function to represent Vertex object with its connection to other verticies
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # returns the verticies that this Vertex is connected to
    def getConnections(self):
        return self.connectedTo.keys()

    # returns the id of this vertex
    def getId(self):
        return self.id

    # returns the weight of a given vertex
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {} #creates a dictionary where the keys are the ids of a vertex and the values are the corresponding vertex
        self.numVertices = 0    #counts total verticies in dictionary 

    def addVertex(self,key):
        self.numVertices += 1   #incremetes everytime vertex added 
        self.vertList[key] = Vertex(key)        #adds vertex to list

    # returns vertex from vertList if vertex found, else it returns None
    def getVertex(self,n):
        if n not in self.vertList:
            return None
        return self.vertList[n]

    # returns a boolean if vertex in the values of dictionary
    def __contains__(self,n):
        return n in self.vertList.values()

    # connects vertex f to vertex t 
    def addEdge(self,f,t,weight=0):
        self.vertList[f].connectedTo[self.vertList[t]] = t

    # returns all verticies ids
    def getVertices(self):
        return self.vertList.keys()

    # Allows you to iterate throug the vertex objects 
    def __iter__(self):
        return iter(self.vertList.values())
    
    def breadth_first_search(self, s):
        # assigns every vertex the color white
        for v in self.vertList.values():
            v.color = 'white'
        queue = []
        path = [] # not a part of BFS, used to check the order of vertices traversed by BFS
        start = self.vertList[ s]
        start.color = 'gray'
        queue.append(start)
        path.append(start.id)
        while len(queue) != 0:
            v = queue.pop(0)
            # checks connected verticies
            for u in v.connectedTo.keys():
                # if white change color and add it too queue
                if u.color == 'white':
                    u.color = 'gray'
                    queue.append(u)
                    path.append(u.id)
            # turns black if vertex cycled through for loop
            v.color = 'black'
        return path # not a part of BFS
    
    def depth_first_search(self):
        # assigns every vertex the color white
        for v in self.vertList.values():
            v.color = 'white'
        path = [] # not a part of DFS, used to check the order of vertices traversed by DFS
        for v in self.vertList.values():
            # calls DFS function if color of vertex white
            if v.color == 'white':
                self.DFS(v.id, path)
        return path
    
    # function that uses recusion to reach depth first
    def DFS(self, vid, path):
        # v is the Vertex with corresponding id
        v = self.vertList[ vid]
        v.color = 'gray'        #changes color from white
        path.append(v.id)   
        # checks the verticies that the Vertex is connected to
        for u in v.connectedTo.keys():
            # if connected vertex color white then recursive called
            if u.color == 'white':
                self.DFS(u.id, path)
        #turns black if vertex cycled through for loop
        v.color = 'black'
        return path

if __name__ == '__main__':

    g = Graph()
    for i in range(6):
        g.addVertex(i)
        
    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)
    for v in g:
        print(v)

    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False
        
    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]