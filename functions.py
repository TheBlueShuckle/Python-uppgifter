# Doubles given number
def double(n):
    return 2 * n

# Triples given number
def triple(n):
    return 3 * n

# Quadruples given number, using the double function twice
def quadruple(n):
    return double(double(n))

# Triples the first given number and adds it to the quadruple of the second given number
def funky(n, m):
    return triple(n) + quadruple(m)

# Tests
a = 3
b = 14

d1 = double(a)       # 6
d2 = double(b)       # 28

t1 = triple(a)       # 9
t2 = triple(b)       # 42

q1 = quadruple(a)    # 12
q2 = quadruple(b)    # 56

f1 = funky(a, b)     # 65
f2 = funky(b, b)     # 98