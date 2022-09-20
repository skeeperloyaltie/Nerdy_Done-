#const n = 8.

% n-Queens encoding

{ q(I,1..n) } == 1 :- I = 1..n.
{ q(1..n,J) } == 1 :- J = 1..n.
:- { q(D-J,J) } >= 2, D =   2..2*n.
:- { q(D+J,J) } >= 2, D = 1-n..n-1.

Implement what we call the n-queens-plus problem in IDP and Clingo.  You may install them or use their online environments, at http://verne.cs.kuleuven.be/idp/ and https://potassco.org/clingo/run/, respectively.

{ q(I,J) } :- q(I,J).
:- { q(D-J,J) } >= 2, D =   2..2*n.
:- { q(D+J,J) } >= 2, D = 1-n..n-1.


