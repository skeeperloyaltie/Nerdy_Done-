import sys

# A: Sets and relations
# A. Sets and relations, as in Database programming

# Implement the following functions in Python.  In a while-loop that retrieves a witness, you may use Python's assignment expression, introduced in Python 3.8.

# 1. Successors map.  Given a set of edges e, as a set of pairs, compute and return a Python dictionary, mapping each vertex that has successors to its set of successors.
#   This is exactly the adjacency list representation of e.


# 2. Graph reachability.  Given a set of edges e, as a set of pairs, and a set of vertices s, compute and return the set of vertices 
# r reachable from those in s by following a sequence of edges in e.  This is as discussed in class, with the slides on "Sets: incrementalize and implement".

# a. Define function "reach_iter" that takes e and s as arguments, and returns r computed by precisely following the algorithm on Slide 46.

# b. Define function "reach_inc_chain" that takes e and s as arguments, and returns r computed by precisely following the algorithm on Slide 53.

# c. Define function "reach_inc_direct" that takes e and s as arguments, and returns r computed by precisely following the algorithm on Slide 55.

# Note that for b and c, you need to use the successors map from 1 to retrieve each successor in constant time.


# 3. Testing and analyzing performance for graph reachability.

# a. Write a script to test your programs on the given data in file reach.in.1000 as well as on a number of randomly generated inputs (report what kinds of inputs you generated, 
# include size and number) and compare the results of the three functions from A.2.

# b. Write a script to measure the running times of your programs on a number of inputs of different sizes (report how you did timing, 
# include what interval you are timing, e.g., from before loading in input to after writing output), plot the results, and conclude what kind of curves you are getting.

def succ_map(e):
  return {}

def reach_iter(e,s):
  return {}

def reach_inc_chain(e,s):
  return {}

def reach_inc_direct(e,s):
  return {}
# The function below is used to test your code. the input is a file name, and the output is a pair of sets.
def reach_read():
  filename = sys.argv[1] if len(sys.argv) > 1 else "reach.in.1000"
  with open(filename) as infile: 
    data= infile.read().replace('}\n{','},{').replace('[','(').replace(']',')')
  e,s = eval(data)
  return e,s

# The reach_test() function is called when the program is run.

def reach_test():
  e,s = reach_read()
  vertices = {x for (x,_) in e} | {y for (_,y) in e}
  print(len(e), len(s), len(vertices))

  rs = reach_iter(e,s)
  print(rs, len(rs))

  e2 = succ_map(e)

  rs2 = reach_inc_chain(e2,s)
  print(rs2 == rs)

  rs3 = reach_inc_direct(e2,s)
  print(rs3 == rs)

reach_test()
