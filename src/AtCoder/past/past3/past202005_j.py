def Meg_nib(border, lists):
    ng = -1
    ok = len(lists) - 1
    if len(lists) == 0 or border <= lists[len(lists) - 1]:
        return -2
    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if lists[mid] < border:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N, M = list(map(int, input().rstrip().split(" ")))
    a = tuple(map(int, input().rstrip().split(" ")))
    ans = 0
    border = [0] * N
    for i in a:
        ans = Meg_nib(i, border)
        if ans == -2:
            print(-1)
        else:
            border[ans] = i
            print(ans + 1)


if __name__ == '__main__':
    main()
