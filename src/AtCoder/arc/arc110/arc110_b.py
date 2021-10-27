N = int(input())
T = input()
ans = 0
minus = [0, 1, 1]
if N == 1:
    if T == "1":
        ans = 2 * 10 ** 10
    else:
        ans = 10 ** 10

else:
    for i in range(3):
        if i == 1:
            if T[0] != "0":
                minus[i] = -1
        elif i == 2:
            if T[:2] != "10":
                minus[i] = -1
        for j in range((N - i) // 3):
            if minus[i] == -1:
                break
            if T[i + j * 3:i + j * 3 + 3] != "110":
                minus[i] = -1
            else:
                minus[i] += 1
        else:
            if (N - i) % 3 == 1:
                if T[-1] != "1":
                    minus[i] = -1
            elif (N - i) % 3 == 2:
                if T[-2:] != "11":
                    minus[i] = -1
            else:
                if minus[i] != -1:
                    minus[i] -= 1
            if minus[i] != -1:
                ans = 10 ** 10 - minus[i]
print(ans)
