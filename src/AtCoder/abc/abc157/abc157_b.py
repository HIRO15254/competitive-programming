A = [[0 for i in range(3)]for i2 in range(3)]
c = [[False for i in range(3)]for i2 in range(3)]
A[0] = list(map(int, input().rstrip().split(" ")))
A[1] = list(map(int, input().rstrip().split(" ")))
A[2] = list(map(int, input().rstrip().split(" ")))
int_inp = int(input())
s = 0
for i in range(int_inp):
    s = int(input())
    for i2 in range(9):
        if A[int(i2 / 3)][i2 % 3] == s:
            c[int(i2 / 3)][i2 % 3] = True
ans = False
for i in range(3):
    if c[i][0] and c[i][1] and c[i][2]:
        ans = True
for i in range(3):
    if c[0][i] and c[1][i] and c[2][i]:
        ans = True
if c[0][0] and c[1][1] and c[2][2]:
    ans = True
if c[2][0] and c[1][1] and c[0][2]:
    ans = True
if ans:
    print('Yes')
else:
    print('No')
