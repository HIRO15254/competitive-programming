from collections import deque

N = int(input())
A = deque(map(int, input().split()))
fliped = False
while len(A) != 0:
    if fliped:
        if A.pop() == 0:
            A.append(0)
            if A.popleft() == 0:
                A.appendleft(0)
                print("No")
                break
            else:
                fliped = not fliped
    else:
        if A.pop() == 1:
            A.append(1)
            if A.popleft() == 1:
                A.appendleft(0)
                print("No")
                break
            else:
                fliped = not fliped
if len(A) == 0:
    print("Yes")
