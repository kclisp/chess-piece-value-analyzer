# chess-piece-value-analyzer
Chess pieces are commonly said to have values:
- Pawn: 1 point
- Knight and Bishop: 3 points
- Rook: 5 points
- Queen: 9 points

But the value of a piece also heavily depends on the position, so what is the actual value of a piece in a position?

A simple measure of a piece's value is to take the difference between
the evaluation of the position with the piece and the evaluation of the position without the piece.

This repo is a Python script using [python-chess](https://github.com/niklasf/python-chess) and [Stockfish](https://github.com/official-stockfish/Stockfish) to analyze chess piece values.

<details>
<summary> Example: Starting position </summary>

```
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
depth: 12
score: 0.38
Ra1: 9.00
Nb1: 7.53
Bc1: 8.68
Qd1: 12.61
Ke1: N/A
Bf1: 8.22
Ng1: 7.91
Rh1: 9.00
Pa2: 0.86
Pb2: 1.62
Pc2: 1.56
Pd2: 1.45
Pe2: 1.48
Pf2: 1.66
Pg2: 2.23
Ph2: 0.82
pa7: -1.13
pb7: -1.43
pc7: -1.44
pd7: -1.60
pe7: -1.58
pf7: -2.68
pg7: -2.02
ph7: -1.12
ra8: -8.82
nb8: -8.20
bc8: -9.05
qd8: -12.62
ke8: N/A
bf8: -8.99
ng8: -8.08
rh8: -9.19
```
Notice that the pawns at the edge of the board are worth less: they control less of the board and they also block their respective rooks, so they aren't worth as much as other pawns.
</details>


<details>
<summary> Example: Scholar's mate, before blunder </summary>

```
r . b q k b n r
p p p p . p p p
. . n . . . . .
. . . . p . . Q
. . B . P . . .
. . . . . . . .
P P P P . P P P
R N B . K . N R
depth: 12
score: -0.43
Ra1: 8.94
Nb1: 8.08
Bc1: 9.15
Ke1: N/A
Ng1: 7.41
Rh1: 9.40
Pa2: 0.91
Pb2: 1.56
Pc2: 1.67
Pd2: 1.27
Pf2: 1.73
Pg2: 1.98
Ph2: 1.04
Bc4: 9.94
Pe4: 3.43
pe5: -2.01
Qh5: 12.86
nc6: -8.55
pa7: -0.99
pb7: -1.64
pc7: -1.70
pd7: -1.63
pf7: -1.82
pg7: -1.19
ph7: 11.65
ra8: -8.40
bc8: -7.98
qd8: -13.37
ke8: N/A
bf8: -7.61
ng8: -6.54
rh8: -8.47
```
More active pieces are worth slightly more. Notice that the black pawn at h7 is valuable for _white_. Since it's black's turn, if the pawn wasn't there, then the rook could take the queen.
</details>


<details>
<summary> Example: Scholar's mate, after blunder </summary>

```
r . b q k b . r
p p p p . p p p
. . n . . n . .
. . . . p . . Q
. . B . P . . .
. . . . . . . .
P P P P . P P P
R N B . K . N R
depth: 12
score: 99.99
Ra1: 0.00
Nb1: 0.00
Bc1: 0.00
Ke1: N/A
Ng1: 0.00
Rh1: 0.00
Pa2: 0.00
Pb2: 0.00
Pc2: 0.00
Pd2: 0.00
Pf2: 0.00
Pg2: 0.00
Ph2: 0.00
Bc4: 109.77
Pe4: 0.00
pe5: 0.00
Qh5: 112.64
nc6: 0.00
nf6: 0.00
pa7: 0.00
pb7: 0.00
pc7: 0.00
pd7: 0.00
pf7: N/A
pg7: 0.00
ph7: 0.00
ra8: 0.00
bc8: 0.00
qd8: 86.06
ke8: N/A
bf8: 0.00
rh8: 0.00
```
Notice that almost no pieces matter because of the impending checkmate; since it's white's turn, the bishop and queen are needed to perform checkmate, so they are worth very much. Perhaps surprisingly, the black queen is also worth very much for _white_, since it's needed for the mate in one.
</details>

#### TODO:
- CLI?
- GUI?
- web stuff
