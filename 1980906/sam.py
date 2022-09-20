import os
import sys
import random 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.key) + ' connected to: ' + str([x.key for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_dict:
            return self.vert_dict[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vert_dict

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_dict:
            self.add_vertex(f)
        if t not in self.vert_dict:
            self.add_vertex(t)
        self.vert_dict[f].add_neighbor(self.vert_dict[t], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def __iter__(self):
        return iter(self.vert_dict.values())

    
def generate_random_graph(n):
    graph = Graph()
    for i in range(n):
        graph.add_vertex(i)
    for i in range(n):
        for j in range(random.randint(1, 4)):
            graph.add_edge(i, random.randint(0, n-1))
    return graph


def generate_random_graph_dot(n):
    graph = generate_random_graph(n)
    dot_file = open('random_graph.dot', 'w')
    dot_file.write('digraph G {\n')
    for vertex in graph.get_vertices():
        for connection in vertex.get_connections():
            dot_file.write('\t' + str(vertex.key) + ' -> ' + str(connection.key) + ' [label="' + str(vertex.get_weight(connection)) + '"];\n')
    dot_file.write('}')
    dot_file.close()
    os.system('dot -Tpng random_graph.dot -o random_graph.png')
    os.system('open random_graph.png')


def breadth_first_search(graph, initial_vertex, target_vertex):
    queue = []
    queue.append(initial_vertex)
    visited = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            if vertex == target_vertex:
                return visited
            for neighbor in vertex.get_connections():
                if neighbor not in visited:
                    queue.append(neighbor)
    return None


def depth_first_search(graph, initial_vertex, target_vertex):
    stack = []
    stack.append(initial_vertex)
    visited = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if vertex == target_vertex:
                return visited
            for neighbor in vertex.get_connections():
                if neighbor not in visited:
                    stack.append(neighbor)
    return None


def iterative_deepening_search(graph, initial_vertex, target_vertex):
    depth = 0
    while True:
        visited = depth_first_search(graph, initial_vertex, target_vertex)
        if visited:
            return visited
        depth += 1


def a_star_search(graph, initial_vertex, target_vertex):
    queue = []
    queue.append(initial_vertex)
    visited = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            if vertex == target_vertex:
                return visited
            for neighbor in vertex.get_connections():
                if neighbor not in visited:
                    queue.append(neighbor)
    return None


def uniform_cost_search(graph, initial_vertex, target_vertex):
    queue = []
    queue.append(initial_vertex)
    visited = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            if vertex == target_vertex:
                return visited
            for neighbor in vertex.get_connections():
                if neighbor not in visited:
                    queue.append(neighbor)
    return None


def iterative_deepening_a_star_search(graph, initial_vertex, target_vertex):
    depth = 0
    while True:
        visited = a_star_search(graph, initial_vertex, target_vertex)
        if visited:
            return visited
        depth += 1


def main():
    n = (sys.argv)
    if len(n) == 1:
        n = random.randint(5, 10)
    else:
        n = int(n[1])

      
    generate_random_graph_dot(n)
    graph = Graph()
    dot_file = open("random_graph.dot", "r")
    for line in dot_file:
        if "--" in line:
            line = line.split("--")
            graph.add_edge(line[0], line[1])
           
    dot_file.close()
    initial_vertex = random.randint(0, n-1)
    target_vertex = random.randint(0, n-1)
    print("Breadth-first search:")
    print(breadth_first_search(graph, graph.get_vertex(initial_vertex), graph.get_vertex(target_vertex)))
    print("Iterative deepening search:")
    print(iterative_deepening_search(graph, graph.get_vertex(initial_vertex), graph.get_vertex(target_vertex)))
    print("A* search:")
    print(a_star_search(graph, graph.get_vertex(initial_vertex), graph.get_vertex(target_vertex)))
    print("Uniform-cost search:")
    print(uniform_cost_search(graph, graph.get_vertex(initial_vertex), graph.get_vertex(target_vertex)))
    print("Iterative deepening A* search:")
    print(iterative_deepening_a_star_search(graph, graph.get_vertex(initial_vertex), graph.get_vertex(target_vertex)))

    # Draw the graph
    dot_file = open("random_graph.dot", "r")
    dot_file_new = open("random_graph_new.dot", "w")
    dot_file_new.write("graph random_graph {\n")
    for line in dot_file:
        if "--" in line:
            line = line.split("--")
            graph.add_edge(line[0], line[1])
            dot_file_new.write(line[0] + " -- " + line[1] + " [label=" + str(graph.get_vertex(line[0]).get_weight(graph.get_vertex(line[1]))) + "]\n")
        else:
            dot_file_new.write(line)
    dot_file_new.write("}\n")
    dot_file_new.close()
    dot_file.close()
    os.system("dot -Tpng random_graph_new.dot -o random_graph_new.png")
    os.system("xdg-open random_graph_new.png")

if __name__ == "__main__":
    main()