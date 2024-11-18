% Set dynamic facts
:- dynamic male/1.
:- dynamic female/1.
:- dynamic parent/2.
:- dynamic child/2.
:- dynamic grandparent/2.
:- dynamic grandchild/2.
:- dynamic spouse/2.
:- dynamic sibling/2.
:- dynamic uncle/2.
:- dynamic aunt/2.
:- dynamic niece/2.
:- dynamic nephew/2.
:- dynamic cousin/2.

% Molecules with Inferences
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

son(X, Y) :- child(X, Y), male(X).
daughter(X, Y) :- child(X, Y), female(X).
child(X, Y) :- parent(Y, X), X \= Y.

grandfather(X, Y) :- grandparent(X, Y), male(X).
grandmother(X, Y) :- grandparent(X, Y), female(X).
grandparent(X, Y) :- parent(X, P), parent(P, Y), X \= Y.

grandson(X, Y) :- grandchild(X, Y), male(X).
granddaughter(X, Y) :- grandchild(X, Y), female(X).
grandchild(X, Y) :- parent(P, X), parent(Y, P), X \= Y.

husband(X, Y) :- spouse(X, Y), male(X).
wife(X, Y) :- spouse(X, Y), female(X).
spouse(X, Y) :- parent(X, C), parent(Y, C), X \= Y.

brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% Atoms with Inferences
uncle(X, Y) :- sibling(X, Z), parent(Z, Y), male(X).
aunt(X, Y) :- sibling(X, Z), parent(Z, Y), female(X).

nephew(X, Y) :- sibling(Z, Y), parent(Z, X), male(X).
niece(X, Y) :- sibling(Z, Y), parent(Z, X), female(X).

cousin(X, Y) :- child(X, W), child(Y, Z), sibling(W, Z), X \= Y, W \= Z.