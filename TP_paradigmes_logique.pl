% Définition des faits
homme(pierre).
homme(marc).
homme(paul).
homme(jacques).
femme(sophie).
femme(marie).

parent('pierre', 'sophie').
parent(pierre, paul).
parent(marie, paul).
parent(marc, sophie).
parent(jacques, marc).



% Règles

pere(X, Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).

grandparent(X,Y) :- parent(X,Z), parent(Z,Y).

frere_ou_soeur(X, Y) :- parent(Z, X),parent(Z, Y), X \= Y.
frere(X, Y) :- homme(X), frere_ou_soeur(X, Y).
soeur(X, Y) :- femme(X), frere_ou_soeur(X, Y).


longueur([], 0).
longueur([_ | Queue], N ) :- longueur(Queue, M), N is M + 1.

present(X, [X|_]).
present(X, [_|Queue]) :- present(X, Queue).



% Initialisation
:- initialization(main).

main :-
    (grand_parent(X, paul) ->
        format('Le grand-parent de Paul est ~w.~n', [X]);
        writeln('Paul n\'a pas de grand-parent défini.')
    ).


