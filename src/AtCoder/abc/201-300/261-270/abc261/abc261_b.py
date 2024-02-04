import sys

N = int(input())
A = []
for i in range(N):
    A.append(list(input()))
for i in range(N):
    for j in range(N):
        if (A[i][j] == 'W' and A[j][i] != 'L') or (A[i][j] == 'D' and A[j][i] != 'D') or (A[i][j] == 'L' and A[j][i] != 'W'):
            print('incorrect')
            sys.exit()
print('correct')
