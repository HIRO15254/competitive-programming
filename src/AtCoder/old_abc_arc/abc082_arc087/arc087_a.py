from itertools import count
from typing import Counter


N = int(input())
a = list(map(int, input().split(" ")))
a.sort()
now = a[0]
counter = 0
ans = 0
for i in a:
    if i == now:
        counter += 1
    else:
        if counter < now:
            ans += counter
        else:
            ans += counter - now
        counter = 1
        now = i
if counter < now:
    ans += counter
else:
    ans += counter - now
print(ans)
