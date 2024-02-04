while True:
    n = int(input())
    if n == 0:
        break
    b = list(map(int, input().split()))
    b.sort(reverse=True)
    ans = [0] * 3
    for i in b:
        for j in range(3):
            if ans[j] == min(ans):
                ans[j] += i
                break
        print(ans)
    print(min(ans))
