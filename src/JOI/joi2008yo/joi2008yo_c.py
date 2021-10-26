Taro = []
Hanako = []

N = int(input())
for i in range(N):
    Taro.append(int(input()))
for i in range(2 * N):
    if i + 1 not in Taro:
        Hanako.append(i + 1)

Taro.sort()
Hanako.sort()
turn = True
ba = 0
while len(Taro) != 0 and len(Hanako) != 0:
    i = 0
    if turn:
        for i in Taro:
            if i > ba:
                ba = i
                Taro.remove(i)
                break
        else:
            ba = 0
    else:
        for i in Hanako:
            if i > ba:
                ba = i
                Hanako.remove(i)
                break
        else:
            ba = 0
    turn = not turn
    print(Taro, Hanako)

print(len(Hanako))
print(len(Taro))
