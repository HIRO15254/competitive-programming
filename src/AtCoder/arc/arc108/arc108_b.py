from collections import deque
N = int(input())
s = input()
fox = "fox"
stack = deque()
ans = N
for i in range(N):
    if s[i] == "f":
        stack.append(1)
    elif s[i] == "o":
        if len(stack) != 0 and stack.pop() == 1:
            stack.append(2)
        else:
            stack.clear()
    elif s[i] == "x":
        if len(stack) != 0 and stack.pop() == 2:
            ans -= 3
        else:
            stack.clear()
    else:
        stack.clear()
print(ans)
