N = int(input())
sho = []
for i in range(N):
    T, D = map(int, input().split())
    # ややこしいが、-1が増えるほう
    sho.append([T - 1, -1])
    sho.append([T + D, 1])
sho.append([10 ** 20, 0])
sho.append([-1, 0])
sho.sort()
ans = 0
i = 1

in_machine = 0
printed = 0
while i < len(sho) - 1:
    new_in = 0
    new_out = 0
    last_time = sho[i - 1][0]
    while True:
        if sho[i][1] == -1:
            new_in += 1
        elif sho[i][1] == 1:
            new_out += 1
        i += 1
        if sho[i][0] != sho[i - 1][0]:
            break
    printed = min(in_machine, printed + sho[i - 1][0] - last_time)

    # print(sho[i - 1][0] - last_time, new_in, new_out, in_machine, printed, ans)
    ans += min(new_out, printed)
    printed -= min(new_out, printed)
    in_machine -= new_out
    in_machine += new_in

print(ans)
