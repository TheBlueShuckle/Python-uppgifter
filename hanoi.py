# Hanoi
A = [4, 3, 2, 1]
B = []
C = []

def hanoi(n, src, dest, aux):
    if (len(src) == 0 and len(aux) == 0):
        return

    move(src, aux)
    move(src, dest)
    move(aux, dest)

    if (len(dest) == 0):
        hanoi()

    hanoi(n, A, B, C)

def move(src, dest):
    movedPiece = src[len(src)-1]
    src.pop(len(src)-1)
    dest.append(movedPiece)
    render(A, B, C)

def render(peg_a, peg_b, peg_c):
    print('A', peg_a)
    print('B', peg_b)
    print('C', peg_c)
    print('-')

render(A, B, C)

hanoi(len(A), A, B, C)