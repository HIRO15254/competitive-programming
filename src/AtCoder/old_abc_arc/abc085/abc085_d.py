N, H = map(int, input().split(" "))
a = [0] * N
b = [0] * N

for i in range(N):
    a[i], b[i] = map(int, input().split(" "))
a.sort(reverse=True)
b.sort(reverse=True)
c = 0
while(b[c] > a[0]):
    H -= b[c]
    c += 1
    if c == len(b):
        break
    if H <= 0:
        break
if H > 0:
    if (H % a[0] != 0):
        c += 1
    c += H // a[0]
print(c)
