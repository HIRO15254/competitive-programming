N = int(input())
DS = []
TIME = 0
for i in range(N):
    DS.append(list(map(int, input().split(" "))))
for i in DS:
    TIME += i[0] / i[1]
now = 0
now_p = 0
for i in DS:
    if now + i[0] / i[1] > TIME / 2:
        print(now_p + (TIME / 2 - now) * i[1])
        exit()
    else:
        now += i[0] / i[1]
        now_p += i[0]
