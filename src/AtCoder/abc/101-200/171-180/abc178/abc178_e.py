N = int(input())
x, y = map(int, input().split(" "))
papb = [x, y]
pamb = [x, y]
mapb = [x, y]
mamb = [x, y]
for i in range(N - 1):
    x, y = map(int, input().split(" "))
    if x + y > papb[0] + papb[1]:
        papb = [x, y]
    if x - y > pamb[0] - pamb[1]:
        pamb = [x, y]
    if 0 - x + y > 0 - mapb[0] + mapb[1]:
        mapb = [x, y]
    if 0 - x - y > 0 - mamb[0] - mamb[1]:
        mamb = [x, y]
print(max(abs(papb[0] - mamb[0]) + abs(papb[1] - mamb[1]), abs(pamb[0] - mapb[0]) + abs(pamb[1] - mapb[1])))
