import random
import sys
import os
os.environ["PATH"] += os.pathsep + 'joaompinto.vscode-graphviz'


def bfs_search(graph, start, target):
    """
    Breadth-first search.
    """
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        vertex.visited = True
        print(vertex.key)
        if vertex.key == target:
            return vertex
        for vertex in vertex.get_connections():
            if not vertex.visited:
                queue.append(vertex)
                
def ucs_search(graph, start, target):
    """
    Uniform cost search.
    """
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        vertex.visited = True
        print(vertex.key)
        if vertex.key == target:
            return vertex
        for vertex in vertex.get_connections():
            if not vertex.visited:
                vertex.distance = vertex.get_weight(vertex) + start.distance
                vertex.previous = start
                queue.append(vertex)
                queue = sorted(queue, key=lambda x: x.distance)


def dfs_search(graph, start, target):
    """
    Depth-first search.
    """
    start.visited = True
    print(start.key)
    if start.key == target:
        return start
    for vertex in start.get_connections():
        if not vertex.visited:
            dfs_search(graph, vertex, target)


def a_star_search(graph, start, target):
    """
    A* search.
    """
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        vertex.visited = True
        print(vertex.key)
        if vertex.key == target:
            return vertex
        for vertex in vertex.get_connections():
            if not vertex.visited:
                vertex.distance = vertex.get_weight(vertex) + start.distance
                vertex.previous = start
                queue.append(vertex)
                queue = sorted(queue, key=lambda x: x.distance)


def cost_function(graph, start, target):
    """
    Uniform cost search.
    """
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        vertex.visited = True
        print(vertex.key)
        if vertex.key == target:
            return vertex
        for vertex in vertex.get_connections():
            if not vertex.visited:
                vertex.distance = vertex.get_weight(vertex) + start.distance
                vertex.previous = start
                queue.append(vertex)
                queue = sorted(queue, key=lambda x: x.distance)


def id_search(graph, start, target):
    """
    Iterative deepening search.
    """
    depth = 0
    while True:
        vertex = dfs_search(graph, start, target)
        if vertex:
            return vertex
        depth += 1

    
def id_a_star_search(graph, start, target):
    """
    Iterative deepening A* search.
    """
    depth = 0
    while True:
        vertex = dfs_search(graph, start, target, depth)
        if vertex:
            return vertex
        depth += 1


#################################################################
#################################################################
def path(p):
    path = []
    for vertex in p:
        path.append(vertex.label)
    return " -> ".join(path)

def cost(G,p):
    cost = 0
    for i in range(len(p) -1):
        for edge in p[i].out_edge:
            return 


##################################################################
##################################################################







