N, K, C = map(int, input().rstrip().split(" "))
S = input()
kinmu = 0
niti = 0
f = []
b = []
kinmu = 0
niti = 0
while kinmu < K and niti < N:
    if S[niti] == "o":
        f.append(niti)
        kinmu += 1
        niti += C
    niti += 1
kinmu = 0
niti = N - 1
while kinmu < K and niti >= 0:
    if S[niti] == "o":
        b.append(niti)
        kinmu += 1
        niti -= C
    niti -= 1
b.reverse()
for i in range(K):
    if f[i] == b[i]:
        print(f[i] + 1)
