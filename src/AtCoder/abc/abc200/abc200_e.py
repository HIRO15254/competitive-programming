N, K = map(int, input().split(" "))
q = [i for i in range(N + 1)] + [i for i in range(N - 1, 0, -1)]
k = 0
r = [0] * (N + 1)
for i in q:
    k += i
    r.append(k)
r = r + [r[-1] for _ in range(N)]
k = 0
s = [0]
for i in range(N * 3):
    k += r[i + N] - r[i]
    s.append(k)
ng = 3 * N
ok = 0
while(abs(ng - ok) > 1):
    mid = (ok + ng) // 2
    if s[mid] < K:
        ok = mid
    else:
        ng = mid
abc_sum = ng
p_in_sum = K - s[ok]
now_a = max(1, abc_sum - N * 2)
k = q[abc_sum - now_a - 1]
c = abc_sum - now_a - 2
r = False
while p_in_sum > k:
    k += q[c]
    c -= 1
    now_a += 1
now_b = max(abc_sum - now_a - N, 1) - p_in_sum + k
print(now_a, abc_sum - now_a - now_b, now_b)
