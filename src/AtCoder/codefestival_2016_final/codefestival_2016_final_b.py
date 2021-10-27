N = int(input())
s = 2
while s * (s - 1) / 2 < N:
    s += 1
for i in range(s - 1):
    if N >= (s - i - 1):
        print(s - i - 1)
        N -= s - i - 1
