def is_kaibun(s):
    for i in range(int(len(s) // 2)):
        if s[i] != s[-1 * (i + 1)]:
            return False
    else:
        return True


N = input()
for i in range(11):
    if is_kaibun(N):
        print("Yes")
        break
    else:
        N = "0" + N
else:
    print("No")
