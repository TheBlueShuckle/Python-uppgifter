# Hanoi
A = [4, 3, 2, 1]
B = []
C = []

def hanoi(n, src, dest, aux):
    move(src, aux)
    move(src, dest)
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

hanoi(2, A, B, C)