import random
import sys
import networkx as nx
import matplotlib.pyplot as plt
import os
os.environ["PATH"] += os.pathsep + 'joaompinto.vscode-graphviz'

class Graph:
    """
    Graph class.
    """

    def __init__(self):
        """
        Initialize a graph.
        """
        self.vertices = {}
        self.size = 0

    def add_vertex(self, key):
        """
        Add a vertex to the graph.
        """
        self.size += 1
        vertex = Vertex(key)
        self.vertices[key] = vertex
        return vertex

    def add_edge(self, vertex1, vertex2, weight=0):
        """
        Add an edge to the graph.
        """
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)
        self.vertices[vertex1].add_connection(self.vertices[vertex2], weight)
        
    def populate(self, num_vertices, num_edges):
        """
        Populate a graph.
        """
        for i in range(num_vertices):
            self.add_vertex(i)
        for i in range(num_edges):
            vertex1 = random.choice(list(self.vertices.keys()))
            vertex2 = random.choice(list(self.vertices.keys()))
            self.add_edge(vertex1, vertex2)

    def get_vertex(self, key):
        """
        Get a vertex.
        """
        return self.vertices[key]

    def get_vertices(self):
        """
        Get all vertices.
        """
        return self.vertices.values()

    def __contains__(self, key):
        """
        Check if a vertex is in the graph.
        """
        return key in self.vertices

    def get_num_edges(self):
        """
        Get the number of edges.
        """
        num_edges = 0
        for vertex in self.vertices.values():
            num_edges += vertex.get_num_connections()
        return num_edges / 2


class Vertex:
    """
    Vertex class.
    """

    def __init__(self, key):
        """
        Initialize a vertex.
        """
        self.key = key
        self.connections = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_connection(self, vertex, weight):
        """
        Add a connection to a vertex.
        """
        # assign random weight between 0 & 1 to each edge, weight must be float 
        # therefore random.uniform is used
        # (round(),3) to limit decimal places to 3 by default over 10 d.p. are given 
        weight = (round(random.uniform(0,1),3))
        self.connections[vertex] = weight

    def get_connections(self):
        """
        Get all connections.
        """
        return self.connections.keys()

    def get_num_connections(self):
        """
        Get the number of connections.
        """
        return len(self.connections)

    def get_weight(self, vertex):
        """
        Get the weight of a connection.
        """
        return self.connections[vertex]

    def __str__(self):
        """
        String representation of a vertex.
        """
        return str(self.key) + ' connected to: ' + str([x.key for x in self.connections])
 
def random_graph(n):
    """
    Generate a random graph on n vertices.
    """
    graph = Graph()
    for i in range(n):
        graph.add_vertex(i)
    for i in range(n):
        for j in range(random.randint(1, 4)):
            graph.add_edge(i, random.randint(0, n-1))
    return graph    

def add_edge(graph, vertex1, vertex2, weight=0):
    """
    Add an edge to the graph.
    """
    if vertex1 not in graph.vertices:
        graph.add_vertex(vertex1)
    if vertex2 not in graph.vertices:
        graph.add_vertex(vertex2)
    graph.vertices[vertex1].add_connection(graph.vertices[vertex2], weight)

def random_graph_dot(n):
    """
    Generate a random graph on n vertices.
    """
    graph = Graph()
    for i in range(n):
        graph.add_vertex(i)
  
    for i in range(n):
        for j in range(random.randint(1, 4)):          # random edge from 1 t0 4
            graph.add_edge(i, random.randint(0, n-1))  # n-1 is used since our first vertex is 0
    return graph


def random_graph_dot_file(n):
    """
    Generate a random graph on n vertices and add weight labels.
    """
    graph = random_graph_dot(n)
    dot_file = open('random_graph.dot', 'w')
    dot_file.write('digraph G {\n')
    for vertex in graph.get_vertices():
        for connection in vertex.get_connections():
            dot_file.write('\t' + str(vertex.key) + ' -> ' + str(connection.key) + ' [label="' + str(vertex.get_weight(connection)) + '"];\n')
    dot_file.write('}')
    dot_file.close()
    os.system('dot -Tpng random_graph.dot -o random_graph.png')
    #os.system('open random_graph.png')











def main():
    #n = random.randint(10,14) #n = random number of vertices between 10 & 14
    n=3
    graph = Graph()
    # print the number of vertices and edges in the graph
    print('Number of vertices:', n)
    print('Number of edges:', graph.get_num_edges())
    random_graph_dot_file(n)
    
    for i in range(n):
        graph.add_vertex(i)
        break
        # add_weight(graph, random.randint(1, 10))
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 2:
                graph.add_edge(i, j)
