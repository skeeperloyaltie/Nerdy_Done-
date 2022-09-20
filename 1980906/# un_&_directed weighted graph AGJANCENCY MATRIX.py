
import os
import random
from tokenize import Floatnumber
import decimal

def printmatrix(matrix):
    r,c = len(matrix), len(matrix[0])
    for i in range(r):
        for j in range(c):
            '''
            #end ="\t""could be used to improve formatting of output matrix"
            '''
            print(matrix[i][j], end= "\t")
        print() #without this print output will not be correctly formated, matrix rows will not be on seperate lines

print("input graph bastard")
f = open (r'random_graph.dot', 'r') 
print (f.read())
input = f.readlines()
v,e = map(int,input().split())
matrix = [[0]*v for i in range(v)]  # this will generate a matrix size v squared

'''
# UNDIRECTED GRAPH
for i in range(e):
    u,v = map(str,input().split())
    u= ord (u) - ord('A')
    v= ord (v) - ord('A') # lines 12 & 13 we are subtracting Ascii value of A from each element to convert node names A,B,c, .... to index 1,2,3,4...
    matrix[u][v] = 1  # 1 will be displayed in matrix if edge exist
    matrix[v][u] = 1 # this line is required for undirected graph and will result in a symetric matrix
printmatrix(matrix)
'''
# DIRECTED / WEIGHTED GRAPH
for i in range(e):
    u,v,w = map(str, input().split())
    #u = ord(u) - ord('A')
    #v = ord(v) - ord('A')
    u = int(u)
    v = int(v)
    w = decimal.Decimal(w)
    matrix[u][v] = w


printmatrix(matrix)

'''
#Input for undirected graph
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F

# iNPUT FOR DIRECTED GRAPH WITH WEIGHT
 # first digit represents number of nodes A to G in this case, 2nd digit represents number of combinations.
7 7
A  B  4
A  C 2
B  C 5
B  D 10
C  E 3
D  F 11
E  D 4
G  D 1
'''
'''
#From random_graphfor search V12
#number of vertices is 12
12 16 
0 2 0.253
0 0 0.3
1 3 9
2 6 4    
3 9 8    
4 5 1    
4 2 8    
5 4 3    
6 6 6    
6 10 3    
7 5 9    
8 11 3    
8 1 6    
9 5 4    
10 6 2    
11 3 5  

'''
#see also https://www.youtube.com/watch?v=bEotR0Q0sc0  for adjacency list in python