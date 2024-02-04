N = int(input())
A = list(map(int, input().rstrip().split(" ")))
bit = [0 for i in range(32)]
for i in range(32):
    for i2 in A:
        if (i2 >> i) & 1:
            bit[i] += 1
ans = [0 for i in range(len(A))]
for i in range(32):
    for i2 in range(len(A)):
        if bit[i] % 2 == 0:
            if (A[i2] >> i) & 1:
                ans[i2] += 2 ** i
        else:
            if not (A[i2] >> i) & 1:
                ans[i2] += 2 ** i
print(" ".join(map(str, ans)))
