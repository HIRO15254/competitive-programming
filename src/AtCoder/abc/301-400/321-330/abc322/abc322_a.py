N = int(input())
S = input()
try:
    ans = S.index("ABC")
    print(ans + 1)
except ValueError:
    print(-1)
