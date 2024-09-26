# Hanoi
A = [4, 3, 2, 1]
B = []
C = []

def hanoi(n, src, dest, aux):
    if (len(src) == 0 and len(aux) == 0):
        return

    move(src, aux)

    if (len(dest) != 0):
        hanoi(len(dest)-1, dest, src, aux)

    move(aux, dest)

    hanoi(n, A, B, C)

def move(src, dest):
    temp = src[len(src)-1]
    src.pop(len(src)-1)
    dest.append(temp)
    render(A, B, C)

def render(peg_a, peg_b, peg_c):
    print('A', peg_a)
    print('B', peg_b)
    print('C', peg_c)
    print('-')

render(A, B, C)

hanoi(3, A, B, C)