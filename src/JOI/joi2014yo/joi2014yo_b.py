N, M = map(int, input().split(" "))
cost = []
vote = [0] * N
for _ in range(N):
    cost.append(int(input()))
for _ in range(M):
    bord = int(input())
    for i in range(N):
        if bord >= cost[i]:
            vote[i] += 1
            break
print(vote.index(max(vote)) + 1)
