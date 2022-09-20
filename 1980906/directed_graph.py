# [] Language: Python3 
import random
import sys
import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np
from pprint import pprint
# import pygraphviz as pgv
os.environ["PATH"] += os.pathsep + 'joaompinto.vscode-graphviz'
######
# Definitions
# Python / Algorithms, directed graphs
# Task: Implement a (directed) graph data structure, as well as some
# searching algorithms to perform a state-space search on the graph.
# Before you choose which data structure to use to represent the graph
# (i.e., adjacency list, adjacency matrix, edge list, etc.), read through the
# whole assignment first, to determine which would be most suitable.

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
    # once in for loop above i = n, we start adding 
    # edges between our generated vertices
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
    dot_file.write('digraph G {layout = "circo"; overlap = scalexy; sep = "+25,25";\n')
    for vertex in graph.get_vertices():
        for connection in vertex.get_connections():
            dot_file.write('\t' + str(vertex.key) + ' -> ' + str(connection.key)  + '\n')
    dot_file.write('}')
    dot_file.close()
    os.system('dot -Tpng random_graph.dot -o random_graph.png')
    os.system('open random_graph.png')

def cost(G,p):
    cost = 0
    for i in range(len(p) -1):
        for edge in p[i].out_edge:
            return 



# create a function to add a weight label to the graph
def add_weight(graph, weight):
    """
    Add a weight label to the graph.
    """
    for vertex in graph.get_vertices():
        for connection in vertex.get_connections():
            connection.weight = weight
            
def get_weight(graph, vertex1, vertex2):
    """
    Get the weight of an edge.
    """
    for connection in vertex1:
        if connection == vertex2:
            return connection.weight

def cost_function(graph, path, weight):
    """
    Cost function.
    """
    cost = 0
    while path:
        cost += get_weight(graph, path[0], weight)
    return cost


def print_cost_path(graph, start, target):
    """
    Print the path from the initial vertex to the target vertex, together with
    the associated total cost of the path.
    """
    path = [target]
    while path[0] != start:
        path.insert(0, path[0].previous)
    # print('Path:', [vertex.key for vertex in path])
    print('Cost:', cost_function(graph, path, target))
    
    
def print_line():
    print('-' * 80)
class Edge:
    """
    Edge class.
    """
    
    def __init__(self, vertex1, vertex2, weight=0): 
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        
    def __str__(self):
        return str(self.vertex1) + ' -> ' + str(self.vertex2) + ' : ' + str(self.weight)


def convert_dot_to_matrix(n):
    try:
        file = open("random_graph.dot").readlines()
    except FileNotFoundError as e:
        print(e)
        exit()

    file.pop(0)
    file.pop()
    adj = [i.strip("\t").strip("\n").split("->") for i in file ] 
    matrix = [[0 for i in range(n)] for j in range(len(adj))] #11
    # pprint(matrix)

    for i in range(len(adj)):
        for j in adj[i]:
            matrix[i][int(j)] = 1
    return matrix


# class to perform searches using the generated matrix and the dictionary

from collections import defaultdict
def bfs(adj, start=0):

    # create a queue
    queue = []
    # create a dictionary to keep track of visited vertices
    visited = defaultdict(lambda: False)

    queue.append(start)

    visited[str(start)] = True
    while queue:
        curr = queue.pop(0)
        # print(len(adj))

        for i in adj[curr]: #11
            if int(i) == 1 and not visited[i]:
                queue.append(int(i))
                visited[i] = True
    print(visited)
    
def dfs(adj, start=0):
    # create a stack
    stack = []
    # create a dictionary to keep track of visited vertices
    visited = defaultdict(lambda: False)

    stack.append(start)

    visited[str(start)] = True
    while stack:
        curr = stack.pop()
        # print(len(adj))

        for i in adj[curr]:
            if int(i) == 1 and not visited[i]:
                stack.append(int(i))
                visited[i] = True
            
    print(visited)

def convert_matrix_to_dict(matrix):
    vertices_dict = {}
    edges_dict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                if i not in vertices_dict:
                    vertices_dict[i] = Vertex(i)
                if j not in vertices_dict:
                    vertices_dict[j] = Vertex(j)
                edges_dict[(i,j)] = i
    return vertices_dict, edges_dict

def main():
    n = int(input('Enter the number of vertices: '))
    # graph = Graph()
    #n=3
    graph = Graph()
    # print the number of vertices and edges in the graph            
    for i in range(n):
        graph.add_vertex(i)
        break
        # add_weight(graph, random.randint(1, 10))
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 2:
                graph.add_edge(i, j)
                
    path = 'random_graph.dot'
    
    

    
    
    # print the graph from the dot file
    random_graph_dot_file(n)
    
    # print the number of vertices and edges in the graph
    print('Number of vertices:', n)
    print('Number of edges:', graph.get_num_edges())
    
    
    # print('Matrix :')
    # pprint(convert_dot_to_matrix(n))
    print_line()
    print('Breath First Search: ')
    bfs(convert_dot_to_matrix(n))
    
     

    
    
if __name__ == '__main__':
    main()



