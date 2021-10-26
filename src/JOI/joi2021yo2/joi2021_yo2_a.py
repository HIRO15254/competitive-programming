N, A = map(int, input().split(" "))
A -= 1
S = list(input())
sh_m = []
sh_a = []
left = 0
for i in range(N):
    if S[i] == "#":
        left += 1
        if i > A:
            sh_a.append(i)
        else:
            sh_m.append(i)
sh_m.reverse()
sh_m += [-1] * (3 * 10**5)
sh_a += [N] * (3 * 10**5)
c_m = 0
c_a = 0
now = A
muki = 0
ans = 0
while left != 0:
    if muki == 0:
        ans += abs(now - sh_a[c_a])
        now = sh_a[c_a]
        muki = 1
        if sh_a[c_a] != N:
            left -= 1
        c_a += 1
    else:
        ans += abs(now - sh_m[c_m])
        now = sh_m[c_m]
        muki = 0
        if sh_m[c_m] != -1:
            left -= 1
        c_m += 1
print(ans)
