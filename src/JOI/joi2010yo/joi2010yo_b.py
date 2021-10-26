N, M = map(int, input().split(" "))
su = []
me = []
for i in range(N):
    su.append(int(input()))
for i in range(M):
    me.append(int(input()))
now = 0
ans = 0
while now < N - 1:
    now += me[ans]
    if now < N - 1:
        now += su[now]
    ans += 1
print(ans)
