d = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
N = int(input())
if N == 1:
    print("a")
elif N == 2:
    print("aa")
    print("ab")
else:
    ans = [[[]]for _ in range(N - 1)]
    ans[0][0] = [1]
    ans[1][0] = [1, 1]
    ans[1].append([1, 2])
    ansstr = []
    for i in range(N - 2):
        for i2 in range(len(ans[i + 1])):
            for i3 in range(max(ans[i + 1][i2]) + 1):
                if i == N - 3:
                    ansstr.clear()
                    for i4 in range(N - 1):
                        ansstr.append(d[ans[i + 1][i2][i4]])
                    ansstr.append(d[i3 + 1])
                    print("".join(ansstr))
                else:
                    ans[i + 2].append(ans[i + 1][i2] + [i3 + 1])
        if i < N - 3:
            ans[i + 2].pop(0)
