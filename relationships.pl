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
:- dynamic relative/2.

relative(X, Y) :- parent(X, Y).      % X is a parent of Y
relative(X, Y) :- parent(Y, X).      % Y is a parent of X
relative(X, Y) :- sibling(X, Y).     % X and Y are siblings
relative(X, Y) :- grandparent(X, Y). % X is a grandparent of Y
relative(X, Y) :- grandchild(X, Y).  % X is a grandchild of Y
relative(X, Y) :- uncle(X, Y).       % X is an uncle of Y
relative(X, Y) :- aunt(X, Y).        % X is an aunt of Y
relative(X, Y) :- cousin(X, Y).      % X is a cousin of Ys

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
contradiction(circular_child) :- child(X, Y), child(Y, X).                          % Circular child relationship
contradiction(circular_uncle) :- uncle(X, Y), uncle(Y, X).                          % Circular uncle relationship
contradiction(circular_aunt) :- aunt(X, Y), aunt(Y, X).                             % Circular aunt relationship
contradiction(circular_niece) :- niece(X, Y), niece(Y, X).                          % Circular niece relationship
contradiction(circular_nephew) :- nephew(X, Y), nephew(Y, X).                       % Circular nephew relationship

contradiction(parent_grandchild) :- parent(X, Y), parent(Y, Z), parent(Z, X).       % Circular extended parent relationship

contradiction(self_child) :- child(X,X).                                            % Self-child contradiction
contradiction(self_parent) :- parent(X, X).                                         % Self-parent contradiction
contradiction(self_cousin) :- cousin(X, X).                                         % Self-cousin contradiction
contradiction(self_grandparent) :- grandparent(X, X).                               % Self-grandparent contradiction
contradiction(self_sibling) :- sibling(X, X).                                       % Self-sibling contradiction
contradiction(self_uncle) :- uncle(X, X).                                           % Self-uncle contradiction
contradiction(self_aunt) :- aunt(X, X).                                             % Self-aunt contradiction
contradiction(self_nephew) :- nephew(X, X).                                         % Self-nephew contradiction
contradiction(self_niece) :- niece(X, X).                                           % Self-niece contradiction
contradiction(self_spouse) :- spouse(X, X).                                         % Self-spouse contradiction
contradiction(self_child) :- child(X, X).                                           % Self-child contradiction
contradiction(self_grandchild) :- grandchild(X, X).                                 % Self-grandchild contradiction

contradiction(sibling_and_parent) :- sibling(X, Y), parent(X, Y).                   % Sibling-parent contradiction
% FIXME: Stops a person from having more than two children
% contradiction(sibling_child) :- sibling(X, Y), child(X, Z), parent(Z, Y).           % Sibling-Child Contradiction

contradiction(gender_conflict) :- male(X), female(X).                               % Gender mismatch
contradiction(parent_gender_mismatch) :- parent(X, Y), male(X), mother(X, Y).       % Gender mismatch of mother
contradiction(parent_gender_mismatch) :- parent(X, Y), female(X), father(X, Y).     % Gender mismatch of father
contradiction(child_gender_mismatch) :- son(X, Y), female(X), parent(Y, X).         % Gender mismatch of son
contradiction(child_gender_mismatch) :- daughter(X, Y), male(X), parent(Y, X).      % Gender mismatch of daughter
contradiction(parent_gender_mismatch) :- father(X, Y), mother(X, Y).                % Gender mismatch of parent

contradiction(incest_parent_child) :- parent(X, Y), (husband(X, Y) ; wife(X, Y)).                                       % Incest Parent X Child
contradiction(incest_sibling) :- sibling(X, Y), (husband(X, Y) ; wife(X, Y)).                                           % Incest Sibling X Sibling
contradiction(incest_grandparent) :- grandparent(X, Y), (husband(X, Y) ; wife(X, Y)).                                   % Incest Grandparent X Grandchild
contradiction(incest_niece_nephew_parent) :- parent(X, Y), (uncle(Y, X) ; aunt(Y, X) ; niece(Y, X) ; nephew(Y, X)).     % Incest Uncle/Aunt/Niece/Nephew X Uncle/Aunt/Niece/Nephew
contradiction(incest_sibling_extended) :- sibling(X, Y), (uncle(X, Y) ; aunt(X, Y) ; niece(X, Y) ; nephew(X, Y)).       % Incest Sibling = Uncle/Aunt/Niece/Nephew

% Family Contradiction

contradiction(cousin_sibling_mismatch) :- cousin(X,Y), sibling(Y,X).                  % Family mismatch of cousin to sibling
contradiction(cousin_child_mismatch) :- cousin(X,Y), child(Y,X).                      % Family mismatch of cousin to child
contradiction(cousin_parent_mismatch) :- cousin(X,Y), parent(Y,X).                    % Family mismatch of cousin to parent
contradiction(cousin_grandparent_mismatch) :- cousin(X,Y), grandparent(Y,X).          % Family mismatch of cousin to grandparent
contradiction(cousin_uncle_mismatch) :- cousin(X,Y), uncle(Y,X).                      % Family mismatch of cousin to uncle
contradiction(cousin_aunt_mismatch) :- cousin(X,Y), aunt(Y,X).                        % Family mismatch of cousin to aunt

contradiction(cousin_sibling_mismatch) :- cousin(X,Y), sibling(X,Y).                  % Family mismatch of cousin to sibling inverse
contradiction(cousin_child_mismatch) :- cousin(X,Y), child(X,Y).                      % Family mismatch of cousin to child inverse
contradiction(cousin_parent_mismatch) :- cousin(X,Y), parent(X,Y).                    % Family mismatch of cousin to parent inverse
contradiction(cousin_grandparent_mismatch) :- cousin(X,Y), grandparent(X,Y).          % Family mismatch of cousin to grandparent inverse
contradiction(cousin_uncle_mismatch) :- cousin(X,Y), uncle(X,Y).                      % Family mismatch of cousin to uncle inverse
contradiction(cousin_aunt_mismatch) :- cousin(X,Y), aunt(X,Y).                        % Family mismatch of cousin to aunt inverse

contradiction(sibling_child_mismatch) :- sibling(X,Y), child(Y,X).                    % Family mismatch of sibling to child
contradiction(sibling_parent_mismatch) :- sibling(X,Y), parent(Y,X).                  % Family mismatch of sibling to parent
contradiction(sibling_grandparent_mismatch) :- sibling(X,Y), grandparent(Y,X).        % Family mismatch of sibling to grandparent
contradiction(sibling_uncle_mismatch) :- sibling(X,Y), uncle(Y,X).                    % Family mismatch of sibling to uncle
contradiction(sibling_aunt_mismatch) :- sibling(X,Y), aunt(Y,X).                      % Family mismatch of sibling to aunt

contradiction(sibling_child_mismatch) :- sibling(X,Y), child(X,Y).                    % Family mismatch of sibling to child inverse
contradiction(sibling_parent_mismatch) :- sibling(X,Y), parent(X,Y).                  % Family mismatch of sibling to parent inverse
contradiction(sibling_grandparent_mismatch) :- sibling(X,Y), grandparent(X,Y).        % Family mismatch of sibling to grandparent inverse
contradiction(sibling_uncle_mismatch) :- sibling(X,Y), uncle(X,Y).                    % Family mismatch of sibling to uncle inverse
contradiction(sibling_aunt_mismatch) :- sibling(X,Y), aunt(X,Y).                      % Family mismatch of sibling to aunt inverse


% contradiction(child_parent_mismatch) :- child(X,Y), parent(Y,X).                      % Family mismatch of child to parent
contradiction(child_grandparent_mismatch) :- child(X,Y), grandparent(Y,X).            % Family mismatch of child to grandparent
contradiction(child_uncle_mismatch) :- child(X,Y), uncle(Y,X).                        % Family mismatch of child to uncle
contradiction(child_aunt_mismatch) :- child(X,Y), aunt(Y,X).                          % Family mismatch of child to aunt

contradiction(child_parent_mismatch) :- child(X,Y), parent(X,Y).                      % Family mismatch of child to parent inverse
contradiction(child_grandparent_mismatch) :- child(X,Y), grandparent(X,Y).            % Family mismatch of child to grandparent inverse
contradiction(child_uncle_mismatch) :- child(X,Y), uncle(X,Y).                        % Family mismatch of child to uncle inverse
contradiction(child_aunt_mismatch) :- child(X,Y), aunt(X,Y).                          % Family mismatch of child to aunt inverse

contradiction(parent_grandparent_mismatch) :- parent(X,Y), grandparent(Y,X).          % Family mismatch of parent to grandparent
contradiction(parent_uncle_mismatch) :- parent(X,Y), uncle(Y,X).                      % Family mismatch of parent to uncle
contradiction(parent_aunt_mismatch) :- parent(X,Y), aunt(Y,X).                        % Family mismatch of parent to aunt

contradiction(parent_grandparent_mismatch) :- parent(X,Y), grandparent(X,Y).          % Family mismatch of parent to grandparent inverse
contradiction(parent_uncle_mismatch) :- parent(X,Y), uncle(X,Y).                      % Family mismatch of parent to uncle inverse
contradiction(parent_aunt_mismatch) :- parent(X,Y), aunt(X,Y).                        % Family mismatch of parent to aunt inverse

contradiction(grandparent_uncle_mismatch) :- grandparent(X,Y), uncle(Y,X).            % Family mismatch of grandparent to uncle
contradiction(grandparent_aunt_mismatch) :- grandparent(X,Y), aunt(Y,X).              % Family mismatch of grandparent to aunt

contradiction(grandparent_uncle_mismatch) :- grandparent(X,Y), uncle(X,Y).            % Family mismatch of grandparent to uncle inverse
contradiction(grandparent_aunt_mismatch) :- grandparent(X,Y), aunt(X,Y).              % Family mismatch of grandparent to aunt inverse

contradiction(uncle_aunt_mismatch) :- uncle(X,Y), aunt(Y,X).                          % Family mismatch of uncle to aunt
contradiction(aunt_uncle_mismatch) :- aunt(Y,X), uncle(Y,X).                          % Family mismatch of aunt to uncle

contradiction(uncle_aunt_mismatch) :- uncle(X,Y), aunt(X,Y).                          % Family mismatch of uncle to aunt inverse
contradiction(aunt_uncle_mismatch) :- aunt(Y,X), uncle(X,Y).                          % Family mismatch of aunt to uncle inverse