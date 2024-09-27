# Hanoi
A = []
B = []
C = []
turn = 0
last_move = ""

def hanoi(n, src, dest, aux):
    if src[len(src) - 1] != n:
        hanoi(n-1, src, aux, dest)

    move(src, dest)

    if aux != [] and (aux[len(aux) - 1] < n):
        hanoi(n-1, aux, dest, src)

    if n in dest:
        return
    
def move(src, dest):
    global turn
    global last_move
    turn += 1
    moved_disc = src[len(src)-1]
    src.pop(len(src)-1)
    dest.append(moved_disc)
    last_move = "Moved disc " + str(moved_disc) + " from " + getPegName(src) + " to " + getPegName(dest)
    render(A, B, C)

def render(peg_a, peg_b, peg_c):
    print("Turn " + str(turn) + ": " + last_move)
    print('A', peg_a)
    print('B', peg_b)
    print('C', peg_c)
    print('-')

def getPegName(peg):
    if peg == A:
        return "A"
    if peg == B:
        return "B"
    if peg == C:
        return "C"
    
def createPegA(n):
    global A

    A = []

    for i in range(n):
        A.insert(0, i+1)

while True:
    createPegA(int(input("Input number of plates: ")))

    render(A, B, C)
    hanoi(len(A), A, B, C)