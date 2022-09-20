# 1. Append.  You are given a definition of predicate append(Xs,Ys,Zs) meaning that the concatenation of Xs and Yu equals Zs.  You are asked to use it to define two predicates.

append (Xs, Ys, Zs) :-
    append(Xs, Ys, Zs).

# a. Predicate suffix/2, such that querying suffix with two lists Xs and Ys will give false if Xs does not equal a prefix of Ys, and otherwise will print out the suffix of Ys after the prefix that equals Xs, followed by true.  For example, querying 
# suffix([1,2], [1,2,3,4]) will print out [3, 4] followed by true.

predicate suffix(Xs, Ys) :-
    append(Xs, _, Ys).


# b. Predicate cut/1, such that querying cut with a list Xs will print out the list of all cuts of Xs followed by true.  For example, querying cut([1,2,3]) will print out the following followed by true.
# [], [1, 2, 3]
# [1], [2, 3]
# [1, 2], [3]
# [1, 2, 3], []

predicate cut(Xs) :-
    append(_, Xs, _).



# 2. Graph reachability.  Implement the graph reachability problem (take predicates source/1 and edge/2, and define predicate reach/1 to be true for all vertices reachable from the sources following the edges), including input and output functionalities (output all reachable vertices).

# You task is to try different ways of writing the rules, run test and analysis as in A.3, and understand and describe how termination and efficiency are affected by the order of rules, the order of hypotheses, and the use of tabling.

rule reach(X) :-
    edge(X, Y),
    reach(Y).




# 3. Transitive closure and cycle detection.  Consider given edge/2 as in C.2.

# a. Define predicate path(a,b) to be true iff there is a sequence of edges leading from a to b.

def path(a, b) :-
    edge(a, b).

# b. Define predicate cycle(a) to be true iff a is in a cycle.
cycle :-
    edge(a, b),
    path(b, a).

# c. Define predicate transitive_closure(+Edges, -Closure) to be true iff Closure is the transitive closure of the set of edges Edges.  For example, transitive_closure([edge(a,b), edge(b,c), edge(c,d)], Closure) should yield Closure = [edge(a,b), edge(a,c), edge(a,d), edge(b,c), edge(b,d), edge(c,d)].


append([],Ys,Ys).
append([X|Xs],Ys,[X|Zs]) :- append(Xs,Ys,Zs).

   
reach(X) :- source(X).
reach(X) :- reach(Y), edge(Y,X).


