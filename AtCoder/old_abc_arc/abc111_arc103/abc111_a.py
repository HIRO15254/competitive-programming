i = input()
ans = 0
for n in range(3):
    if i[n] == "1":
        ans += 9 * (10 ** (2 - n))
    else:
        ans += 1 * (10 ** (2 - n))
print(ans)
