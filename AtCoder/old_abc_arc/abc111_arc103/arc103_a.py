N = int(input())
K = list(map(int, input().rstrip().split(" ")))
Ka = [0] * (10 ** 5 + 1)
Ke = [0] * (10 ** 5 + 1)
Ka2 = []
Ke2 = []

for i in range(N):
    if i % 2 == 0:
        Ka[K[i]] += 1
    else:
        Ke[K[i]] += 1
Ka2 = sorted(Ka, reverse=True)
Ke2 = sorted(Ke, reverse=True)

if Ka.index(Ka2[0]) == Ke.index(Ke2[0]):
    if Ka2[0] - Ka2[1] < Ke2[0] - Ke2[1]:
        print(N - Ka2[1] - Ke2[0])
    else:
        print(N - Ka2[0] - Ke2[1])
else:
    print(N - Ka2[0] - Ke2[0])
