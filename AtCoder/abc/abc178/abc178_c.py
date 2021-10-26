N = int(input())
ans = 1
mians = 1
mians2 = 1
for i in range(N):
    ans *= 10
    ans %= 10 ** 9 + 7
for i in range(N):
    mians *= 9
    mians %= 10 ** 9 + 7
for i in range(N):
    mians2 *= 8
    mians2 %= 10 ** 9 + 7
mians = mians * 2 - mians2
if mians < 0:
    mians += 10 ** 9 + 7
mians %= 10 ** 9 + 7
ans -= mians
if ans < 0:
    ans += 10 ** 9 + 7
print(ans)
