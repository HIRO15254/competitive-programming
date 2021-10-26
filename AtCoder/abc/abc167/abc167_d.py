N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
A.insert(0, 0)
rireki = [1]
counter = 1
now = 1
flag = [0 for _ in range(N + 1)]
flag[1] = 1
while(flag[A[now]] == 0):
    counter += 1
    rireki.append(A[now])
    flag[A[now]] = counter
    now = A[now]
if K < flag[A[now]]:
    print(rireki[K])
else:
    K += counter - (flag[A[now]] - 1)
    K -= flag[A[now]] - 1
    K %= counter - (flag[A[now]] - 1)
    print(rireki[flag[A[now]] - 1 + K])
