#This is the program driver run this to launch the program
from random import randint, random
from tracemalloc import start
import graph_generator as graph
import graph_searches as gs


graph = graph.Graph()
start = int(randint(1, 100))
target = int(randint(1, 100))
graph.populate(start, target)
print()

# bfs output
print()
print()
print("Path found using breath-first search : ")
bfs = gs.bfs_search(graph, graph.vertices[0], graph.vertices[9])
if bfs:
        print("Path exist")
        print("Path:", gs.path(bfs))
        print("Path length:", len(bfs)-1)
        print("Path cost:", gs.cost(graph,bfs))
else:
        print("Path nonexistent")
print()
print()

# dfs output
print()
print()
print("Path found using depth-first search : ")
dfs = gs.dfs_search(graph, graph.vertices[0], graph.vertices[9])
if dfs:
        print("Path exist")
        print("Path:", gs.path(dfs))
        print("Path length:", len(dfs))
        print("Path cost:", gs.cost (graph,dfs))
else:
        print("Path nonexistent")
print()
print()

#UCS output
print()
print()
print("Path found using Uniform Cost search : ")
ucs = gs.ucs_search(graph, graph.vertices[0], graph.vertices[9])
if ucs:
        print("Path Exist")
        print("Path:", gs.path(ucs))
        print("Path length:", len(ucs))
        print("Path cost:", gs.cost(graph,ucs))
else:
        print("Path nonexistent")
print()
print()

# A* search output
print()
print()
print("Path found using A* search : ")
a_sta = gs.a_star_search(graph, graph.vertices[0], graph.vertices[9])
if a_sta:
        print("Path exist")
        print("Path:", gs.path(a_sta))
        print("Path length:", len(a_sta))
        print("Path cost:", gs.cost(graph,a_sta))
else:
        print("Path nonexistent")
print()
print()

#Iterative deepening A* search output
print()
print()
print("Path found using A* search : ")
star_a = gs.a_star_search(graph, graph.vertices[0], graph.vertices[9])
if star_a:
        print("Path Exist")
        print("Path:", gs.path(star_a))
        print("Path length:", len(star_a))
        print("Path cost:", gs.cost (graph,star_a))
else:
        print("Path nonexistent")
print()
print()


# generate the dot file
graph.generate_dot_file()