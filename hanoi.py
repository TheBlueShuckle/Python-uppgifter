# Hanoi
A = [4, 3, 2, 1]
B = []
C = []

def hanoi(n, src, dest, aux):
    if src[len(src) - 1] != n:
        hanoi(n-1, src, aux, dest)

    move(src, dest)

    if aux != [] and (aux[len(aux) - 1] < n):
        hanoi(n-1, aux, dest, src)

    if n in dest:
        return
    
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