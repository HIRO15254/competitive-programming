A, B = 0, 0
I = list(map(int, input().split()))
if len(I) == 1:
    A = I[0]
    B = int(input())
else:
    A = I[0]
    B = I[1]

Ai = list(map(int, input().split()))
Bi = list(map(int, input().split()))

for i in range(A):
    Bi.append(0)

ans = 0
k = 0

for i in range(B):
    k = i
    for j in range(A):
        if Bi[k] == Ai[j]:
            k += 1
    ans = max(ans, k - i)
print(ans)
