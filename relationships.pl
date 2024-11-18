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

% Contradictions
contradiction(circular_parent) :- parent(X, Y), parent(Y, X).                       % Circular parent-child relationship
contradiction(circular_grandparent) :- grandparent(X, Y), grandparent(Y, X).        % Circular grandparent-grandchild relationship

contradiction(self_child) :- child(X,X).                                            % Self-child contradiction
contradiction(self_parent) :- parent(X, X).                                         % Self-parent contradiction
contradiction(circular_cousin) :- cousin(X, X).                                     % Self-cousin contradiction
contradiction(self_grandparent) :- grandparent(X, X).                               % Self-grandparent contradiction


contradiction(gender_conflict) :- male(X), female(X).                               % Gender contradiction

contradiction(sibling_and_parent) :- sibling(X, Y), parent(X, Y).                   % Sibling-parent contradiction
contradiction(sibling_child) :- sibling(X, Y), child(X, Z), parent(Z, Y).           % Sibling-Child Contradiction

contradiction(parent_gender_mismatch) :- parent(X, Y), male(X), mother(X, Y).       % Gender mismatch of mother
contradiction(parent_gender_mismatch) :- parent(X, Y), female(X), father(X, Y).     % Gender mismatch of father

contradiction(incest_parent_child) :- parent(X, Y), (husband(X, Y) ; wife(X, Y)).        % Incest Parent X Child
contradiction(incest_sibling) :- sibling(X, Y), (husband(X, Y) ; wife(X, Y)).            % Incest Sibling X Sibling
contradiction(incest_grandparent) :- grandparent(X, Y), (husband(X, Y) ; wife(X, Y)).    % Incest Grandparent X Grandchild
contradiction(incest_niece_nephew_parent) :- parent(X, Y), (uncle(Y, X) ; aunt(Y, X) ; niece(Y, X) ; nephew(Y, X)).     % Incest Uncle/Aunt/Niece/Nephew X Uncle/Aunt/Niece/Nephew
contradiction(incest_sibling_extended) :- sibling(X, Y), (uncle(X, Y) ; aunt(X, Y) ; niece(X, Y) ; nephew(X, Y)).       % Incest Sibling = Uncle/Aunt/Niece/Nephew

contradiction(circular_cousin) :- cousin(X, X).                                      % Self-cousin contradiction
contradiction(circular_uncle) :- uncle(X, X).                                        % Self-uncle contradiction
contradiction(circular_aunt) :- aunt(X, X).                                      % Self-aunt contradiction
contradiction(circular_nephew) :- nephew(X, X).                                      % Self-nephew contradiction
contradiction(circular_niece) :- niece(X, X).                                      % Self-niece contradiction
contradiction(circular_spouse) :- spouse(X, X).                                    % Self-spouse contradiction
contradiction(circular_child) :- child(X, X).                                    % Self-child contradiction
contradiction(circular_grandchild) :- grandchild(X, X).                                    % Self-grandchild contradiction
