N = int(input())
prime = [2]
ansans = []
flag = True
counter = 0
now = 3
ans = ""
while len(ansans) != N:
    counter = 0
    flag = True
    while prime[counter] ** 2 <= now:
        if now % prime[counter] == 0:
            flag = False
            break
        counter += 1
    if flag:
        prime.append(now)
        if now % 5 == 1:
            ansans.append(now)
    now += 1
for i in range(N):
    ans += str(ansans[i])
    if i != N - 1:
        ans += " "
print(ans)
