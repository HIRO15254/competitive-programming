N = int(input())
A = list(map(int, input().split()))
A2 = sorted(A)
border = A2[N // 2 - 1]
border_count = A2[(N // 2):].count(border)
border_now = 0
s = sum(A2[(N // 2):])
A_b = []
for i in range(N // 2):
    now = 0
    for j in range(2):
        if A[i * 2 + j] > border:
            now += 1
        if A[i * 2 + j] == border:
            if border_now < border_count:
                now += 1
            border_now += 1
    A_b.append(now - 1)
A_b_s = [A_b[0]]
()
for i in range(1, N // 2):
    A_b_s.append(A_b_s[-1] + A_b[i])
k = (A_b_s.index(max(A_b_s)) * 2 + 2) % N
print(k, s)
