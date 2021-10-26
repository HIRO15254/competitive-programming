L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = (A - 1) // C + 1
F = (B - 1) // D + 1
print(L - max(E, F))
