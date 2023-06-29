A = [4, 3, 2, 1]
B = []
C = []
N = 3
print(A, B, C)
def move(n, source, target, aux):

    if n > 0:
        move(n - 1, source, aux, target)
        target.append(source.pop())
        move(n-1, aux, target, source)

move(N, A, C, B)

print(A, B, C)