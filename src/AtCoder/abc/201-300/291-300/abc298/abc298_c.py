N = int(input())
Q = int(input())
box = dict()
num = dict()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if query[2] - 1 not in box:
            box[query[2] - 1] = []
        box[query[2] - 1].append(query[1])
        if query[1] - 1 not in num:
            num[query[1] - 1] = set()
        num[query[1] - 1].add(query[2])
    if query[0] == 2:
        print(" ".join(map(str, sorted(box[query[1] - 1]))))
    if query[0] == 3:
        print(" ".join(map(str, sorted(num[query[1] - 1]))))
